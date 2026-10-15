#ifndef EEG_ADS1299_H
#define EEG_ADS1299_H

#include <Arduino.h>
#include <SPI.h>

class ADS1299Driver {
public:
    ADS1299Driver(uint8_t csPin);
    void begin();
    void startStreaming();
    void stopStreaming();
    void readMicrovolts(float* channelData);

private:
    uint8_t _csPin;
    void writeRegister(uint8_t reg, uint8_t value);
    uint8_t readRegister(uint8_t reg);
};

#endif
