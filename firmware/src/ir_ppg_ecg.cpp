#include <Arduino.h>
#include <Wire.h>
#include "MAX30105.h"

MAX30105 particleSensor;

void setupIRPPG() {
    Wire.begin(8, 9);
    if (!particleSensor.begin(Wire, I2C_SPEED_FAST)) {
        Serial.println("PPG/NIR Sensor not found.");
        while (1);
    }
    
    // Configure NIR (880nm/940nm) sub-surface penetration
    byte powerLevel = 0x1F; 
    byte sampleAverage = 4; 
    byte ledMode = 3; // Red + IR + Green
    int sampleRate = 400; 
    int pulseWidth = 411; 
    int adcRange = 4096; 

    particleSensor.setup(powerLevel, sampleAverage, ledMode, sampleRate, pulseWidth, adcRange);
}

uint32_t readSubSurfaceNIR() {
    return particleSensor.getIR(); // Returns NIR penetration depth raw count
}
