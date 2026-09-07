import os

import joblib


BASE_DIR = os.path.dirname(
    os.path.dirname(
        os.path.dirname(
            os.path.abspath(__file__)
        )
    )
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "ml",
    "educational_model.joblib"
)

model_data = joblib.load(MODEL_PATH)

vectorizer = model_data["vectorizer"]
classifier = model_data["classifier"]


def classify_text(text):
    if not text or not text.strip():
        return {
            "educational": False,
            "score": 0.0,
        }

    X = vectorizer.transform([text])

    probabilities = classifier.predict_proba(X)[0]

    educational_score = float(probabilities[1])

    return {
        "educational": educational_score >= 0.55,
        "score": educational_score,
    }