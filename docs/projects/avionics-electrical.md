# Avionics Electrical

Our electrical subteam designs and builds sophisticated electronic systems for
the rocket, including custom flight computers and communication systems.

## Blaze-NT Avionics System

Blaze-NT is UCSC Rocketry's next-generation flight computer, providing
comprehensive flight data logging, sensor monitoring, and telemetry
capabilities.

### Main System Schematic

<div class="kicanvas-container">
<kicanvas-embed controls="full">
    <kicanvas-source src="https://raw.githubusercontent.com/UCSCRocketry/blaze-nt-hardware/refs/heads/main/Blaze-NT.kicad_prj"></kicanvas-source>
    <kicanvas-source src="https://raw.githubusercontent.com/UCSCRocketry/blaze-nt-hardware/refs/heads/main/Blaze-NT.kicad_sch"></kicanvas-source>
    <kicanvas-source src="https://raw.githubusercontent.com/UCSCRocketry/blaze-nt-hardware/refs/heads/main/Blaze-NT.kicad_pcb"></kicanvas-source>
    <kicanvas-source src="https://raw.githubusercontent.com/UCSCRocketry/blaze-nt-hardware/refs/heads/main/power-managment.kicad_sch"></kicanvas-source>
    <kicanvas-source src="https://raw.githubusercontent.com/UCSCRocketry/blaze-nt-hardware/refs/heads/main/microcontroller.kicad_sch"></kicanvas-source>
    <kicanvas-source src="https://raw.githubusercontent.com/UCSCRocketry/blaze-nt-hardware/refs/heads/main/VBATT_Sense.kicad_sch"></kicanvas-source>
    <kicanvas-source src="https://raw.githubusercontent.com/UCSCRocketry/blaze-nt-hardware/refs/heads/main/Radio.kicad_sch"></kicanvas-source>
    <kicanvas-source src="https://raw.githubusercontent.com/UCSCRocketry/blaze-nt-hardware/refs/heads/main/sensors.kicad_sch"></kicanvas-source>
    <kicanvas-source src="https://raw.githubusercontent.com/UCSCRocketry/blaze-nt-hardware/refs/heads/main/barometer.kicad_sch"></kicanvas-source>
    <kicanvas-source src="https://raw.githubusercontent.com/UCSCRocketry/blaze-nt-hardware/refs/heads/main/accelerometer.kicad_sch"></kicanvas-source>
    <kicanvas-source src="https://raw.githubusercontent.com/UCSCRocketry/blaze-nt-hardware/refs/heads/main/imu.kicad_sch"></kicanvas-source>
</kicanvas-embed>
</div>

### Blaze-NT Technical Specifications

- **Processor**: STM32F411 ARM Cortex-M4
- **RF Frequency**: 433MHz telemetry
- **Sensor Suite**: 9-axis IMU, barometer, high-g accelerometer
- **Power Management**: Integrated buck regulators, battery monitoring
- **Data Rate**: High-rate sensor acquisition and storage
- **Framework**: Arduino-compatible firmware
- **Status**: Flight-tested prototype hardware

## 2025 Blaze Radio Project

The Blaze Radio is our custom-designed communication and telemetry system. Using
the same form factor as the popular HopeRF RFM69HCW it serves as a drop in
replacement with up to 20x the transmit power.

### Main Radio Schematic

<div class="kicanvas-container">
<kicanvas-embed controls="full">
        <kicanvas-source src="https://raw.githubusercontent.com/UCSCRocketry/2025-blaze-radio/main/blaze-radio.kicad_sch"></kicanvas-source>
        <kicanvas-source src="https://raw.githubusercontent.com/UCSCRocketry/2025-blaze-radio/main/blaze-radio.kicad_pcb"></kicanvas-source>
        <kicanvas-source src="https://raw.githubusercontent.com/UCSCRocketry/2025-blaze-radio/main/power-amp.kicad_sch"></kicanvas-source>
        <kicanvas-source src="https://raw.githubusercontent.com/UCSCRocketry/2025-blaze-radio/main/transceiver.kicad_sch"></kicanvas-source>
</kicanvas-embed>
</div>

### Blaze Radio Technical Specifications

- **RF Frequency**: 433MHz
- **Output Power**: Up to 2W
- **Data Rate**: 1 Mbps telemetry
- **Power Consumption**: < 500mA @ 3.3V nominal
