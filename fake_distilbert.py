import numpy as np

class FakeDistilBERT:
    def encode(self, text: str):
        # Simulate 768-dim embedding like real DistilBERT
        return np.random.rand(768)
