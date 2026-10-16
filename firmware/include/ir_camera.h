#ifndef IR_CAMERA_H
#define IR_CAMERA_H

#include <Arduino.h>

void initIRCamera();
bool captureNIRFrame(uint8_t** buffer, size_t* length);

#endif
