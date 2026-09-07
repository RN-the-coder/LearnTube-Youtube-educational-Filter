import os

import joblib
import pandas as pd

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)


BASE_DIR = os.path.dirname(
    os.path.abspath(__file__)
)

DATA_PATH = os.path.join(
    BASE_DIR,
    "real_titles_training.csv"
)

MODEL_PATH = os.path.join(
    BASE_DIR,
    "educational_model.joblib"
)


# -----------------------------------------
# 1. Cargar dataset real
# -----------------------------------------

data = pd.read_csv(DATA_PATH)

titles = data["title"]
labels = data["label"]


print()
print("===== DATASET REAL =====")
print()

print("Total:", len(data))
print(
    "Educativos:",
    (labels == 1).sum()
)
print(
    "No educativos:",
    (labels == 0).sum()
)


# -----------------------------------------
# 2. Separar entrenamiento y prueba
# -----------------------------------------

X_train, X_test, y_train, y_test = (
    train_test_split(
        titles,
        labels,
        test_size=0.20,
        random_state=42,
        stratify=labels,
    )
)


# -----------------------------------------
# 3. TF-IDF
# -----------------------------------------

vectorizer = TfidfVectorizer(
    ngram_range=(1, 2),
    lowercase=True,
    strip_accents="unicode",
)

X_train_vectorized = (
    vectorizer.fit_transform(X_train)
)

X_test_vectorized = (
    vectorizer.transform(X_test)
)


# -----------------------------------------
# 4. Entrenar Logistic Regression
# -----------------------------------------

classifier = LogisticRegression(
    max_iter=1000,
    random_state=42,
)

classifier.fit(
    X_train_vectorized,
    y_train
)


# -----------------------------------------
# 5. Obtener probabilidades
# -----------------------------------------

probabilities = classifier.predict_proba(
    X_test_vectorized
)[:, 1]


# -----------------------------------------
# 6. Evaluar threshold 0.50
# -----------------------------------------

predictions_50 = (
    probabilities >= 0.50
).astype(int)


# -----------------------------------------
# 7. Evaluar threshold 0.55
# -----------------------------------------

predictions_55 = (
    probabilities >= 0.55
).astype(int)


def show_metrics(
    name,
    y_true,
    predictions
):
    accuracy = accuracy_score(
        y_true,
        predictions
    )

    precision = precision_score(
        y_true,
        predictions,
        zero_division=0
    )

    recall = recall_score(
        y_true,
        predictions,
        zero_division=0
    )

    f1 = f1_score(
        y_true,
        predictions,
        zero_division=0
    )

    matrix = confusion_matrix(
        y_true,
        predictions
    )

    print()
    print(
        f"===== {name} ====="
    )
    print()

    print(
        "Accuracy:",
        round(accuracy * 100, 2),
        "%"
    )

    print(
        "Precision:",
        round(precision * 100, 2),
        "%"
    )

    print(
        "Recall:",
        round(recall * 100, 2),
        "%"
    )

    print(
        "F1 Score:",
        round(f1 * 100, 2),
        "%"
    )

    print()
    print("Matriz de confusión:")
    print(matrix)


show_metrics(
    "THRESHOLD 0.50",
    y_test,
    predictions_50
)

show_metrics(
    "THRESHOLD 0.55",
    y_test,
    predictions_55
)


# -----------------------------------------
# 8. Guardar modelo
# -----------------------------------------

model_data = {
    "vectorizer": vectorizer,
    "classifier": classifier,
}

joblib.dump(
    model_data,
    MODEL_PATH
)

print()
print(
    "Modelo guardado en:",
    MODEL_PATH
)