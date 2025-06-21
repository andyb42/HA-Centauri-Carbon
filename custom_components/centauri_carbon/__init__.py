from homeassistant.config_entries import ConfigEntry
from homeassistant.const import EVENT_HOMEASSISTANT_STARTED
from homeassistant.core import HomeAssistant
from .ws_client import CentauriWebSocketClient
from .const import DOMAIN

async def async_setup(hass: HomeAssistant, config: dict):
    return True

async def async_setup_entry(hass: HomeAssistant, entry: ConfigEntry):
    ws_client = CentauriWebSocketClient(hass, entry.data["ip"])
    hass.data[DOMAIN] = ws_client

    def start_ws(event=None):
        hass.loop.create_task(ws_client.connect())

    if hass.is_running:
        start_ws()
    else:
        hass.bus.async_listen_once(EVENT_HOMEASSISTANT_STARTED, start_ws)

    await hass.config_entries.async_forward_entry_setups(
        entry, ["sensor", "camera", "fan", "light", "number", "select"]
    )
    return True