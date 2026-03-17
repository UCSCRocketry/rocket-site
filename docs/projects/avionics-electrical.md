---
template: avionics-electrical.html
avionics_electrical:
  systems:
    - name: Blaze-NT Avionics System
      slug: blaze-nt-avionics-system
      image: /assets/projects/blaze-nt.gif
      description: Blaze-NT is UCSC Rocketry's next-generation flight computer, providing comprehensive flight data logging, sensor monitoring, and telemetry capabilities.
      specs:
        - label: Processor
          value: STM32F411 ARM Cortex-M4
        - label: Radio Telemetry
          value: 433MHz telemetry, up to 20km range
        - label: Sensor Suite
          value: 9-axis IMU, barometer, high-g accelerometer
        - label: Data logging
          value: Built in 128mbit NOR flash, expandable with latching micro sd card

    - name: Blaze Radio
      slug: blaze-radio
      image: /assets/projects/blaze-radio.gif
      description: Blaze Radio is our custom-designed communication and telemetry system. Using the same form factor as the popular HopeRF RFM69HCW it serves as a drop in replacement with up to 20x the transmit power.
      specs:
        - label: RF Frequency
          value: 433MHz
        - label: Output Power
          value: Up to 2W
        - label: Data Rate
          value: 1 Mbps telemetry
        - label: Power Consumption
          value: "< 500mA @ 3.3V nominal"
        - label: Size
          value: 0.63"x0.63"

    - name: Pebble GPS Locator
      slug: pebble
      image: /assets/projects/pebble.gif
      description: The landing site of a high power rocket is up to the wind, which can carry rockets at high altitudes multiple miles away. In order to ease recovery of a flown rocket, the Pebbble GPS Locator relays the location of the rocket to a hand held reciever.
      specs:
        - label: Small Form Factor
          value: 1.2"x0.6", smallest location designed for rocketry
        - label: Long Range
          value: 100km design range
        - label: Unlicensed ISM band
          value: No radio operator license required to operate
        - label: Low Cost
          value: Under $20 to manufacture one locator
---

# Avionics Electrical

## Blaze-NT Avionics System

## Blaze Radio

## Pebble
