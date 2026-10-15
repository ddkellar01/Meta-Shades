#ifndef WIFI_BLE_H
#define WIFI_BLE_H

#include <Arduino.h>

void initBLE();
void sendTelemetryBLE(const char* payload);

#endif
