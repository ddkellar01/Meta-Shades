#ifndef CONFIG_H
#define CONFIG_H

// System Configuration
#define DEVICE_NAME "MetaShades-v1"
#define BAUDRATE 115200

// I2C Pins for MAX30102 PPG & ADS1299 EEG
#define I2C_SDA_PIN 8
#define I2C_SCL_PIN 9

// I2S Audio Pinouts (Microphone & DAC Amplifier)
#define I2S_MIC_WS   4
#define I2S_MIC_SCK  5
#define I2S_MIC_SD   6

#define I2S_SPK_LRC  25
#define I2S_SPK_BCLK 26
#define I2S_SPK_DIN  22

// SPI Pins for ADS1299 EEG ADC Chip
#define SPI_MOSI 11
#define SPI_MISO 13
#define SPI_SCK  12
#define ADS1299_CS 10

// NIR Optical Pulse Settings
#define PPG_SAMPLE_RATE 400
#define PPG_PULSE_WIDTH 411

#endif
