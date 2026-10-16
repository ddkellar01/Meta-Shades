#include "ir_sensor.h"
#include <Wire.h>
#include "MAX30105.h"

static MAX30105 irSensor;

void initIRSensor() {
    Wire.begin(8, 9);
    if (!irSensor.begin(Wire, I2C_SPEED_FAST)) {
        Serial.println("NIR Optical Sensor initialization failed.");
        return;
    }
    irSensor.setup(0x1F, 4, 3, 400, 411, 4096);
}

uint32_t getIRReading() {
    return irSensor.getIR();
}
