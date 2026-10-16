#include <Arduino.h>
#include <freertos/FreeRTOS.h>
#include <freertos/task.h>

// Forward declarations for your tasks and functions
void sensorTask(void *pvParameters);
void sendTelemetryBLE();

void setup() {
    // Initialize serial communication and peripherals
    Serial.begin(115200);
    delay(1000);
    Serial.println("Initializing Meta-Shades Firmware...");

    // Example: Create the FreeRTOS task that was throwing the undefined reference error
    xTaskCreate(
        sensorTask,          // Task function
        "SensorTask",        // Task name
        4096,                // Stack size (bytes)
        NULL,                // Parameters
        1,                   // Task priority
        NULL                 // Task handle
    );
}

void loop() {
    // Keep loop empty or handle lightweight periodic tasks 
    // if your architecture relies primarily on FreeRTOS tasks.
    vTaskDelay(pdMS_TO_TICKS(1000));
}
