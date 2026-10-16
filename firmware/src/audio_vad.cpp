#include <Arduino.h>
#include <driver/i2s.h>

#define VAD_THRESHOLD 1500 // Energy threshold for voice detection

bool detectVoiceActivity() {
    size_t bytesRead = 0;
    int16_t buffer[256];
    
    i2s_read(I2S_NUM_0, &buffer, sizeof(buffer), &bytesRead, portMAX_DELAY);
    
    long sum = 0;
    int samples = bytesRead / sizeof(int16_t);
    for (int i = 0; i < samples; i++) {
        sum += abs(buffer[i]);
    }
    
    long averageEnergy = samples > 0 ? sum / samples : 0;
    return averageEnergy > VAD_THRESHOLD;
}
