import random

class FakeExtraTrees:
    def predict_proba(self, embedding):
        # Simulate binary classification (Low vs High Risk)
        prob_high = random.random()
        prob_low = 1 - prob_high
        return [[prob_low, prob_high]]
