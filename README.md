# Meta Shades 🕶️🧠⚡

[![C/C++ CI](https://github.com/username/meta-shades/actions/workflows/c-cpp.yml/badge.svg)](https://github.com/username/meta-shades/actions/workflows/c-cpp.yml)
[![Docker Image CI](https://github.com/username/meta-shades/actions/workflows/docker-image.yml/badge.svg)](https://github.com/username/meta-shades/actions/workflows/docker-image.yml)
[![Python CI](https://github.com/username/meta-shades/actions/workflows/python-ci.yml/badge.svg)](https://github.com/username/meta-shades/actions/workflows/python-ci.yml)

---

## What is this about?
**Meta Shades** is an open-source, smart wearable glasses ecosystem[span_1](start_span)[span_1](end_span) that merges biometric edge sensing[span_2](start_span)[span_2](end_span), cranial EEG brainwave acquisition[span_3](start_span)[span_3](end_span), cuffless blood pressure tracking[span_4](start_span)[span_4](end_span), infrared (IR) vision[span_5](start_span)[span_5](end_span), and multi-modal AI orchestration[span_6](start_span)[span_6](end_span). Powered by an ESP32-S3 microcontroller and a FastAPI Python backend, it bridges physiological monitoring with cloud AI intelligence (Google Gemini[span_7](start_span)[span_7](end_span) and Alexa[span_8](start_span)[span_8](end_span)) and private bone-conduction audio[span_9](start_span)[span_9](end_span).

---

## What this does?
* **Senses Biometrics:** Captures real-time NIR optical pulse (PPG) data, cranial microvolt EEG signals (Alpha, Beta, Theta, Delta), and IR optical frames[span_10](start_span)[span_10](end_span).
* **Computes Edge Metrics:** Calculates real-time Blood Pressure via Pulse Wave Transit Time (PWTT) and evaluates cognitive focus states at 100Hz[span_11](start_span)[span_11](end_span).
* **Executes Hybrid AI Decisions:** Routes smart home commands to Alexa and physiological/vision reasoning queries to Google Gemini[span_12](start_span)[span_12](end_span).
* **Delivers Actionable Feedback:** Provides instant acoustic feedback through bone-conduction transducers[span_13](start_span)[span_13](end_span).

---

## How does this work?
1. **Sensing:** The ESP32-S3 hardware collects optical pulse, EEG brainwave voltages, and timing streams using specialized sensor integrations[span_14](start_span)[span_14](end_span).
2. **Edge Processing:** Raw packets are processed locally or streamed via WebSockets to compute real-time blood pressure (PWTT) and engagement metrics[span_15](start_span)[span_15](end_span).
3. **Hybrid AI Decision:** The backend engine evaluates user transcripts and bio-context, routing tasks appropriately between local logic, Alexa, and Google Gemini[span_16](start_span)[span_16](end_span).
4. **Action:** Spatial bone-conduction audio delivers instant feedback or voice responses directly to the user[span_17](start_span)[span_17](end_span).

---

## How to set this up?

### 1. Hardware Assembly
* Follow the `docs/bill_of_materials.md` to source components (ESP32-S3, MAX30105, ADS1299, etc.)[span_18](start_span)[span_18](end_span).
* 3D print the frame and temple arms using the `.scad` or `.stl` files in the `cad/` directory[span_19](start_span)[span_19](end_span).
* Wire the sensors according to `docs/wiring_diagram.md`[span_20](start_span)[span_20](end_span) and place EEG electrodes per `docs/eeg_electrode_placement.md`[span_21](start_span)[span_21](end_span).

### 2. Firmware Setup (PlatformIO)
```bash
cd firmware
pio run
pio run --target upload

3. Backend Setup (Docker)

cd hub-backend
cp .env.example .env
# Add your GEMINI_API_KEY to .env
docker-compose up --build

### Why is this cool? (15 Reasons)
1. Real-Time Brainwave Tracking: Unlocks cranial EEG telemetry using a dedicated 4-channel low-noise ADC (ADS1299).  
2. Cuffless Blood Pressure: Estimates systolic and diastolic blood pressure passively using Pulse Wave Transit Time (PWTT).  
3. Sub-Surface NIR Vision: Employs infrared optical pulse sensors and custom CLAHE histogram equalization for enhanced vein detection.  
4. Hybrid AI Architecture: Seamlessly orchestrates local routines with cloud intelligence via Google Gemini and Alexa integrations.  
5. Private Bone-Conduction Audio: Delivers audio straight to your inner ear via vibration without blocking ambient sounds.  
6. Fully Parametric 3D CAD Design: Custom OpenSCAD frame generators allow you to resize and tweak glasses dimensions on the fly.  
7. Automated CI/CD Pipelines: Fully tested with GitHub Actions workflows verifying C++ firmware builds, Python tests, and Docker containers.  
8. Voice Activity Detection (VAD): Smart audio processing triggers voice commands locally before hitting cloud services.  
9. Low-Latency BLE Streaming: Streams telemetry reliably over Bluetooth Low Energy with custom structured JSON payloads.  
10. FreeRTOS Multitasking: Leverages ESP32-S3 multi-core capabilities to run sensor loops and communication tasks concurrently.  
11. Scalable Async Backend: Built on FastAPI and WebSockets to handle high-frequency biometric data streams effortlessly.  
12. Containerized Security: Docker configuration runs under non-root user permissions with integrated health checks.  
13. Comprehensive Documentation: Includes explicit BLE API specs, wiring pinouts, calibration guides, and bills of materials.  
14. Modular Codebase: Clean separation between firmware headers/sources, ML processing packages, and client connectors.  
15. Open-Source Health Tech: Freely licensed under the MIT License for community experimentation and research.  

### What problems this solves? (15 Solutions)
1. Eliminates Bulky Medical Gear: Replaces arm-squeezing blood pressure cuffs with comfortable, continuous eyewear monitoring.  
2. Breaks Closed-Source Lock-In: Solves the restriction of proprietary fitness wearables by offering an open-source hardware/software stack.  
3. Resolves Audio Isolation: Overcomes traditional headphone safety hazards by using open-ear bone-conduction transducers.  
4. Prevents Silent Firmware Bugs: Catches compilation errors early using automated PlatformIO GitHub Actions workflows.  
5. Stops Backend Regression: Ensures API reliability through automated ⁠pytest⁠ suites and strict type annotations.  
6. Simplifies Hardware Prototyping: Solves component fit issues with ready-to-print OpenSCAD parametric eyewear designs.  
7. Bridges IoT Fragmentation: Unites smart home control (Alexa) and advanced AI reasoning (Gemini) under a single router.  
8. Removes Calibration Guesswork: Provides a formalized 30-day cuffless blood pressure calibration protocol.  
9. Overcomes Low-Light Vision Hurdles: Enhances near-infrared camera frames in the dark using advanced computer vision filters.  
10. Prevents Microcontroller Overload: Offloads heavy machine learning feature extraction (FFT/PSD band power) to a Python backend.  
11. Eliminates Environment Dependency Issues: Standardizes development and deployment environments using Docker containers.  
12. Stops Sensor Misplacement: Provides precise electrode placement maps to ensure accurate brainwave capture.  
13. Mitigates Wireless Data Loss: Buffers and structures telemetry packets to prevent dropped BLE data frames.  
14. Reduces Code Clutter: Separates concerns cleanly across dedicated modules for audio, EEG, camera, and sensors.  
15. Eases Developer Onboarding: Removes setup friction with clear directory structures, requirements files, and installation guides.  

### How to install this?

Clone the repository:

git clone [https://github.com/ddkellar01/meta-shades.git](https://github.com/username/meta-shades.git)
cd meta-shades

Install Backend Dependencies:

cd hub-backend
pip install -r requirements.txt

Run Tests:

pytest

Requirements?
 Hardware:
 ESP32-S3-DevKitC / Seeed Studio XIAO ESP32-S3  
 MAX30105 Optical Sensor  
 ADS1299 4-Channel Low-Noise ADC  
 ICS-43434 I2S Digital Microphone  
 MAX98357A DAC Amplifier + Bone Conduction Transducer  
 3.7V LiPo Battery (150mAh)  
 Software:
 PlatformIO (for C++ firmware)
 Python 3.10+  
 Docker & Docker Compose (for backend deployment)

Full Project Structure Tree
meta-shades/
├── .github/
│   └── workflows/
│       ├── c-cpp.yml             # C/C++ firmware build CI[span_59](start_span)[span_59](end_span)
│       ├── docker-image.yml      # Docker image build CI[span_60](start_span)[span_60](end_span)
│       └── python-ci.yml         # Python backend test CI[span_61](start_span)[span_61](end_span)
├── cad/
│   ├── frame_generator.scad      # Parametric OpenSCAD glass frame[span_62](start_span)[span_62](end_span)
│   ├── ir_lens_inserts.scad      # IR transmissive lens insert script[span_63](start_span)[span_63](end_span)
│   ├── meta_shades_front_frame.stl # 3D model front enclosure[span_64](start_span)[span_64](end_span)
│   ├── temple_arm_left.stl       # Left temple arm housing ESP32 & LiPo[span_65](start_span)[span_65](end_span)
│   └── temple_arm_right.stl      # Right temple arm housing DAC & Mic[span_66](start_span)[span_66](end_span)
├── docs/
│   ├── api_spec.md               # BLE UUIDs and JSON payload schema[span_67](start_span)[span_67](end_span)
│   ├── bill_of_materials.md      # Full component BOM and part numbers[span_68](start_span)[span_68](end_span)
│   ├── eeg_electrode_placement.md # EEG pin and electrode guide[span_69](start_span)[span_69](end_span)
│   ├── pwtt_bp_calibration.md    # Blood pressure calibration protocol[span_70](start_span)[span_70](end_span)
│   └── wiring_diagram.md         # Hardware pinout & bus specifications[span_71](start_span)[span_71](end_span)
├── firmware/
│   ├── include/
│   │   ├── audio.h               # I2S audio header
│   │   ├── config.h              # Global pin definitions & baud rates[span_72](start_span)[span_72](end_span)
│   │   ├── eeg_ads1299.h         # ADS1299 EEG driver header
│   │   ├── ir_camera.h           # IR camera capture header
│   │   ├── ir_sensor.h           # MAX30105 optical sensor header
│   │   └── wifi_ble.h            # BLE telemetry broadcasting header
│   ├── src/
│   │   ├── audio.cpp             # I2S configuration & driver setup[span_73](start_span)[span_73](end_span)
│   │   ├── audio_vad.cpp         # Voice Activity Detection logic[span_74](start_span)[span_74](end_span)
│   │   ├── eeg_ads1299.cpp       # SPI communication for brainwaves[span_75](start_span)[span_75](end_span)
│   │   ├── firmware_misc.cpp     # FreeRTOS telemetry task runner[span_76](start_span)[span_76](end_span)
│   │   ├── ir_camera.cpp         # OV2640 / NIR camera settings[span_77](start_span)[span_77](end_span)
│   │   ├── ir_ppg_ecg.cpp        # PPG/ECG pulse wave routines[span_78](start_span)[span_78](end_span)
│   │   ├── ir_sensor.cpp         # Optical sensor initialization[span_79](start_span)[span_79](end_span)
│   │   └── main.cpp              # Core setup and task scheduler[span_80](start_span)[span_80](end_span)
│   └── platformio.ini            # PlatformIO project configuration[span_81](start_span)[span_81](end_span)
├── hub-backend/
│   ├── src/
│   │   ├── ml_engine/
│   │   │   ├── __init__.py
│   │   │   ├── blood_pressure.py # PWTT blood pressure estimator[span_82](start_span)[span_82](end_span)
│   │   │   ├── eeg.py            # EEG signal feature extraction[span_83](start_span)[span_83](end_span)
│   │   │   ├── eeg_processor.py  # PSD and band power calculations[span_84](start_span)[span_84](end_span)
│   │   │   └── ir_vision_engine.py # CLAHE histogram eye vein processing[span_85](start_span)[span_85](end_span)
│   │   ├── alexa_client.py       # Alexa Voice Service stub integration[span_86](start_span)[span_86](end_span)
│   │   ├── client_simulator.py   # WebSocket telemetry simulator[span_87](start_span)[span_87](end_span)
│   │   ├── gemini_client.py      # Google Gemini multimodal client[span_88](start_span)[span_88](end_span)
│   │   ├── main.py               # FastAPI app & WebSocket endpoint[span_89](start_span)[span_89](end_span)
│   │   ├── router.py             # Intelligent AI assistant router[span_90](start_span)[span_90](end_span)
│   │   └── tts_engine.py         # Text-to-speech output engine[span_91](start_span)[span_91](end_span)
│   ├── tests/
│   │   ├── __init__.py
│   │   └── test_backend.py       # Pytest unit tests for ML & APIs[span_92](start_span)[span_92](end_span)
│   ├── .dockerignore
│   ├── Dockerfile                # Secure multi-stage Python container[span_93](start_span)[span_93](end_span)
│   ├── pyproject.toml
│   ├── pytest.ini
│   └── requirements.txt          # Python dependencies (FastAPI, NumPy, etc.)[span_94](start_span)[span_94](end_span)
├── .gitignore
├── LICENSE                       # MIT License[span_95](start_span)[span_95](end_span)
├── README.md                     # Project documentation[span_96](start_span)[span_96](end_span)
├── docker-compose.yml            # Local container orchestrator[span_97](start_span)[span_97](end_span)
├── pyproject.toml
└── pytest.ini

