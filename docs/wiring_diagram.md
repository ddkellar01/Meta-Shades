# Meta Shades Hardware Pinout & Wiring Specification

| Subsystem | Component | ESP32-S3 Pin | Description |
| :--- | :--- | :--- | :--- |
| **I2C Bus** | MAX30102 / NIR Sensor | GPIO 8 (SDA), GPIO 9 (SCL) | Sub-surface optical PPG |
| **SPI Bus** | ADS1299 EEG ADC | GPIO 11 (MOSI), 12 (SCK), 13 (MISO), 10 (CS) | Cranial brainwave acquisition |
| **I2S Audio** | ICS-43434 Microphone | GPIO 4 (WS), 5 (SCK), 6 (SD) | Voice activity detection |
| **I2S Audio** | MAX98357A DAC Amplifier | GPIO 25 (LRC), 26 (BCLK), 22 (DIN) | Bone-conduction / speaker output |
