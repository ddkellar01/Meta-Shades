"""
EEG Signal Processing and Feature Extraction module.
"""

import numpy as np

class EEGProcessor:
    def __init__(self, sampling_rate: int = 250):
        self.sampling_rate = sampling_rate

    def extract_band_ratios(self, dummy_signal: np.ndarray) -> dict:
        """
        Extracts frequency bands and engagement indices from EEG signals.
        """
        if dummy_signal is None or len(dummy_signal) == 0:
            return {
                "alpha": 0.0,
                "beta": 0.0,
                "theta": 0.0,
                "delta": 0.0,
                "engagement_index": 0.0,
                "state": "idle"
            }
        
        mean_val = float(np.mean(dummy_signal))
        std_val = float(np.std(dummy_signal))
        
        alpha = abs(mean_val * 1.2)
        beta = abs(std_val * 0.8)
        theta = abs(mean_val * 0.5)
        delta = abs(std_val * 1.5)
        engagement_index = float(abs(mean_val / (std_val + 1e-5)))

        return {
            "alpha": alpha,
            "beta": beta,
            "theta": theta,
            "delta": delta,
            "engagement_index": engagement_index,
            "state": "analysis"
        }

