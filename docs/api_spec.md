# Meta Shades BLE API Specification

- **Service UUID**: `4fa8c241-1802-45e0-82d2-07bb30861413`
- **Characteristic UUID**: `beb5483e-36e1-4688-b7f5-ea07361b26a8`
- **Notification Type**: Read & Notify

### JSON Payload Schema
```json
{
  "timestamp": 1718500000,
  "heart_rate": 72,
  "ir_val": 134200,
  "eeg_ch1": 14.5,
  "eeg_ch2": 12.1,
  "ecg_peak_ms": 120,
  "ppg_peak_ms": 240
}
