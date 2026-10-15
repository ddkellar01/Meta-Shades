import numpy as np
from scipy.signal import welch

class EEGProcessor:
    def __init__(self, sampling_rate: int = 250):
        self.fs = sampling_rate

    def extract_band_ratios(self, signal: list) -> dict:
        data = np.array(signal)
        freqs, psd = welch(data, fs=self.fs, nperseg=len(data))

        def get_power(f_low, f_high):
            idx = np.logical_and(freqs >= f_low, freqs <= f_high)
            return np.sum(psd[idx])

        alpha = get_power(8, 12)
        beta = get_power(13, 30)
        theta = get_power(4, 7)

        engagement = beta / (alpha + theta + 1e-6)

        return {
            "alpha": float(alpha),
            "beta": float(beta),
            "theta": float(theta),
            "engagement_index": float(engagement),
            "state": "Focused" if engagement > 1.0 else "Relaxed"
        }
