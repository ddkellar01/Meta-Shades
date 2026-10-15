import numpy as np

class BloodPressureEstimator:
    """Calculates cuffless blood pressure via PWTT (Pulse Wave Transit Time)"""
    def __init__(self):
        # Baseline calibration parameters
        self.a = -0.5
        self.b = 180.0

    def estimate_bp(self, pwtt_ms: float, heart_rate: int) -> dict:
        sbp = self.a * pwtt_ms + self.b
        dbp = sbp * 0.65
        
        return {
            "systolic": round(float(sbp), 1),
            "diastolic": round(float(dbp), 1),
            "pwtt": pwtt_ms,
            "hr": heart_rate
        }
