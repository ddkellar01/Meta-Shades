# Cuffless Blood Pressure Calibration Protocol (PWTT)

Pulse Wave Transit Time (PWTT) correlates electrical heart activity (ECG R-Peak) with peripheral optical pulse arrival (NIR PPG Nosepad Peak).

### Calibration Steps:
1. Take a baseline medical-grade arm cuff blood pressure reading.
2. Record simultaneous ECG R-Peak timestamps and NIR pulse wave arrivals over a 60-second window.
3. Fit linear regression coefficients ($a$ and $b$) in `blood_pressure.py` using:
   $$\text{SBP} = a \cdot \text{PWTT} + b$$
4. Re-calibrate every 30 days for optimal accuracy.
