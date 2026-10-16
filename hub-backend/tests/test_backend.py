import pytest
from ml_engine.blood_pressure import BloodPressureEstimator
from ml_engine.eeg_processor import EEGProcessor

def test_blood_pressure_estimation():
    estimator = BloodPressureEstimator()
    result = estimator.estimate_bp(pwtt_ms=120.0, heart_rate=75)
    
    assert "systolic" in result
    assert "diastolic" in result
    assert result["systolic"] > result["diastolic"]

def test_eeg_processing():
    processor = EEGProcessor(sampling_rate=250)
    dummy_signal = [0.1 * i for i in range(500)]
    analysis = processor.extract_band_ratios(dummy_signal)
    
    assert "engagement_index" in analysis
    assert "state" in analysis
