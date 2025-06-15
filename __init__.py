from homeassistant.config_entries import ConfigEntry
from homeassistant.core import HomeAssistant
from homeassistant.const import EVENT_HOMEASSISTANT_STOP
from .ws_client import CentauriWebSocketClient
from .const import DOMAIN, CONF_RETRY_DELAY, DEFAULT_RETRY_DELAY

async def async_setup(hass: HomeAssistant, config: dict):
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    ws_client = CentauriWebSocketClient(
        hass,
        entry.data["ip"],
        retry_delay=entry.data.get(CONF_RETRY_DELAY, DEFAULT_RETRY_DELAY),
    )
    hass.data[DOMAIN] = ws_client
    hass.loop.create_task(ws_client.connect())

    entry.async_on_unload(
        hass.bus.async_listen_once(
            EVENT_HOMEASSISTANT_STOP,
            lambda event: hass.async_create_task(ws_client.async_close())
        )
    )

    await hass.config_entries.async_forward_entry_setups(
        entry, ["sensor", "camera", "fan", "light", "number", "select"]
    )
    return True
