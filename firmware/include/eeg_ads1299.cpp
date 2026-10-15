#include "eeg_ads1299.h"

ADS1299Driver::ADS1299Driver(uint8_t csPin) : _csPin(csPin) {}

void ADS1299Driver::begin() {
    pinMode(_csPin, OUTPUT);
    digitalWrite(_csPin, HIGH);
    SPI.begin(12, 13, 11, _csPin);
    
    // Reset and initialize ADS1299 registers
    digitalWrite(_csPin, LOW);
    SPI.transfer(0x06); // RESET Command
    delay(10);
    SPI.transfer(0x11); // SDATAC Command (Stop Read Data Continuous)
    digitalWrite(_csPin, HIGH);
}

void ADS1299Driver::startStreaming() {
    digitalWrite(_csPin, LOW);
    SPI.transfer(0x10); // RDATAC Command
    SPI.transfer(0x08); // START Command
    digitalWrite(_csPin, HIGH);
}

void ADS1299Driver::readMicrovolts(float* channelData) {
    digitalWrite(_csPin, LOW);
    for (int i = 0; i < 4; i++) { // 4 channels on temples
        int32_t rawVal = 0;
        rawVal |= (SPI.transfer(0x00) << 16);
        rawVal |= (SPI.transfer(0x00) << 8);
        rawVal |= SPI.transfer(0x00);
        
        // Scale to microvolts (gain conversion)
        channelData[i] = (float)rawVal * (4.5 / 8388607.0) / 24.0 * 1e6;
    }
    digitalWrite(_csPin, HIGH);
}
