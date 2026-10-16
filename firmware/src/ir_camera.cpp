#include "ir_camera.h"
#include "esp_camera.h"

// Camera pin configuration for ESP32-S3 Camera Module (OV2640 / No IR-Cut)
#define CAM_PIN_PWDN     -1
#define CAM_PIN_RESET    -1
#define CAM_PIN_XCLK     15
#define CAM_PIN_SIOD     4
#define CAM_PIN_SIOC     5
#define CAM_PIN_D7       36
#define CAM_PIN_D6       37
#define CAM_PIN_D5       38
#define CAM_PIN_D4       39
#define CAM_PIN_D3       35
#define CAM_PIN_D2       14
#define CAM_PIN_D1       13
#define CAM_PIN_D0       34
#define CAM_PIN_VSYNC    21
#define CAM_PIN_HREF     22
#define CAM_PIN_PCLK     25

void initIRCamera() {
    camera_config_t config;
    config.ledc_channel = LEDC_CHANNEL_0;
    config.ledc_timer = LEDC_TIMER_0;
    config.pin_d0 = CAM_PIN_D0;
    config.pin_d1 = CAM_PIN_D1;
    config.pin_d2 = CAM_PIN_D2;
    config.pin_d3 = CAM_PIN_D3;
    config.pin_d4 = CAM_PIN_D4;
    config.pin_d5 = CAM_PIN_D5;
    config.pin_d6 = CAM_PIN_D6;
    config.pin_d7 = CAM_PIN_D7;
    config.pin_xclk = CAM_PIN_XCLK;
    config.pin_pclk = CAM_PIN_PCLK;
    config.pin_vsync = CAM_PIN_VSYNC;
    config.pin_href = CAM_PIN_HREF;
    config.pin_sccb_sda = CAM_PIN_SIOD;
    config.pin_sccb_scl = CAM_PIN_SIOC;
    config.pin_pwdn = CAM_PIN_PWDN;
    config.pin_reset = CAM_PIN_RESET;
    config.xclk_freq_hz = 20000000;
    config.pixel_format = PIXFORMAT_GRAYSCALE; // Optimized for NIR vein detection
    config.frame_size = FRAMESIZE_QQVGA;
    config.jpeg_quality = 12;
    config.fb_count = 1;

    esp_camera_init(&config);
}

bool captureNIRFrame(uint8_t** buffer, size_t* length) {
    camera_fb_t * fb = esp_camera_fb_get();
    if (!fb) return false;
    
    *buffer = fb->buf;
    *length = fb->len;
    return true;
}
