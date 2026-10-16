"""Blood pressure estimation module."""


class BloodPressureEstimator:
    """Basic interface for a future blood pressure estimator."""

    def __init__(self):
        self.is_fitted = False

    def fit(self, features, targets):
        """Placeholder for model training."""
        raise NotImplementedError(
            "A validated training implementation is required."
        )

    def predict(self, features):
        """Placeholder for model predictions."""
        raise NotImplementedError(
            "A validated prediction implementation is required."
        )