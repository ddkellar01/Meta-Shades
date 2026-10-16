import cv2
import numpy as np

class IRVisionEngine:
    """
    Processes Near-Infrared (NIR) frames captured by the frame camera 
    to enhance sub-surface vascular/vein maps through dark optical glass.
    """
    @staticmethod
    def process_nir_frame(frame_bytes: bytes) -> np.ndarray:
        np_arr = np.frombuffer(frame_bytes, np.uint8)
        img = cv2.imdecode(np_arr, cv2.IMREAD_GRAYSCALE)
        
        # Contrast Limited Adaptive Histogram Equalization (CLAHE) for veins
        clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8, 8))
        enhanced = clahe.apply(img)
        
        # Blur to eliminate high-frequency skin noise
        smoothed = cv2.GaussianBlur(enhanced, (5, 5), 0)
        return smoothed