#include <Arduino.h>
#include "config.h"
#include "wifi_ble.h"
#include "ir_sensor.h"

TaskHandle_t SensorTaskHandle = NULL;

void sensorTask(void *pvParameters) {
    while (1) {
        uint32_t irValue = getIRReading();
        char payload[64];
        snprintf(payload, sizeof(payload), "{\"ir_val\":%lu}", irValue);
        sendTelemetryBLE(payload);
        vTaskDelay(pdMS_TO_TICKS(10)); // 100Hz loop
    }
}

void setup() {
    Serial.begin(BAUDRATE);
    delay(1000); // Stabilize serial connection
    initBLE();
    initIRSensor();

    // Create FreeRTOS task for real-time sensor streaming on Core 0
    xTaskCreatePinnedToCore(
        sensorTask,
        "SensorTask",
        4096,
        NULL,
        1,
        &SensorTaskHandle,
        0
    );
    
    Serial.println("MetaShades Firmware Initialized Successfully.");
}

void loop() {
    // Main loop remains lean; tasks handled asynchronously via FreeRTOS
    vTaskDelay(pdMS_TO_TICKS(1000));
}
