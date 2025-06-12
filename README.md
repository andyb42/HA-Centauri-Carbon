This is an integration into Home Assistant that will allow you to add sensors, controls, and the camera for the Elegoo Centauri Carbon into Home Assistant via your local network.
I am selling my Centauri Carbon relatively soon so I will not be able to provide updates. Hopefully Elegoo doesn't break it!

Currently Supported Sensors:

Centauri Camera
Current Layer
Total Layers
Elapsed Print Time
Remaining Print Time
Print Progress
Print Status
Current Layer
Total Layers
Print Speed
Z Offset
Temperature - Nozzle
Temperature - Bed
Temperature - Enclosure
Temperature Target - Bed
Temperature Target - Nozzle
Fan Speed - Model
Fan Speed - Auxilliary
Fan Speed - Enclosure

Currently Supported Controls:

Chamber Light
Fan Speed - Model
Fan Speed - Auxilliary
Fan Speed - Enclosure
Print Speed
Target Bed Temperature
Target Nozzle Temperature

![image](https://github.com/user-attachments/assets/35b886d5-1a51-46b8-921e-33a7854503e6)

Here is an example entities card for what I use.

type: entities
entities:
  - entity: sensor.print_status
  - entity: sensor.print_progress
  - entity: sensor.remaining_print_time
  - entity: sensor.elapsed_print_time
  - entity: sensor.current_layer
  - entity: sensor.total_layers
  - entity: sensor.z_offset
  - entity: light.chamber_light
  - entity: select.print_speed
  - entity: number.target_bed_temp
  - entity: number.target_nozzle_temp
  - entity: fan.fan_speed_model
  - entity: fan.fan_speed_auxiliary
  - entity: fan.fan_speed_enclosure
