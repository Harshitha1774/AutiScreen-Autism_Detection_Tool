from Autism_backend.fake_distilbert import FakeDistilBERT
from Autism_backend.fake_extraTrees import FakeExtraTrees

class FakeModelPipeline:
    def __init__(self):
        self.encoder = FakeDistilBERT()
        self.classifier = FakeExtraTrees()

    def predict(self, text: str):
        # Step 1: Encode text to fake embedding
        embedding = self.encoder.encode(text)

        # Step 2: Pass embedding to fake classifier
        probs = self.classifier.predict_proba(embedding)[0]

        # Step 3: Return result
        label = "High Risk" if probs[1] > 0.5 else "Low Risk"
        return {
            "label": label,
            "probability": round(float(probs[1]), 4)  # probability of High Risk
        }

# export single model instance
model = FakeModelPipeline()
