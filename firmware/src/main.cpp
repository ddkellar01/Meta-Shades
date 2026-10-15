#include <Arduino.h>
#include "config.h"
#include "eeg_ads1299.h"

ADS1299Driver eeg(ADS1299_CS);

void setup() {
    Serial.begin(BAUDRATE);
    eeg.begin();
    eeg.startStreaming();
    Serial.println("MetaShades Hardware Initialized.");
}

void loop() {
    float eegBuffer[4];
    eeg.readMicrovolts(eegBuffer);
    
    // Format JSON Telemetry output over BLE/Serial
    Serial.printf("{\"eeg_ch1\":%.2f, \"eeg_ch2\":%.2f}\n", eegBuffer[0], eegBuffer[1]);
    delay(10); // 100Hz sampling loop
}
