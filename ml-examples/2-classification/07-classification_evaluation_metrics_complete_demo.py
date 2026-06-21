"""
Classification Evaluation Metrics - Complete Demo

Problem:
Evaluate a Pass / Fail classification model.

This demo covers:
1. Confusion matrix concepts
2. Accuracy
3. Precision
4. Recall
5. F1-score
6. classification_report
7. Binary classification metrics
8. Multi-class classification metrics
9. Imbalanced accuracy trap

Install:
    pip install pandas scikit-learn
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)


# ------------------------------------------------------------
# PART 1: Manual metric calculation example
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("PART 1: MANUAL METRIC EXAMPLE")
print("=" * 70)

actual = ["Pass", "Fail", "Pass", "Fail", "Pass", "Pass"]
predicted = ["Pass", "Pass", "Pass", "Fail", "Fail", "Pass"]

print("\nActual:")
print(actual)

print("\nPredicted:")
print(predicted)

print("\nConfusion Matrix:")
print(confusion_matrix(actual, predicted, labels=["Fail", "Pass"]))

accuracy = accuracy_score(actual, predicted)
precision = precision_score(actual, predicted, pos_label="Pass")
recall = recall_score(actual, predicted, pos_label="Pass")
f1 = f1_score(actual, predicted, pos_label="Pass")

print("\nMetrics when positive class = Pass:")
print("Accuracy :", round(accuracy, 2))
print("Precision:", round(precision, 2))
print("Recall   :", round(recall, 2))
print("F1-score :", round(f1, 2))

print("\nClassification Report:")
print(classification_report(actual, predicted, zero_division=0))


# ------------------------------------------------------------
# PART 2: Binary classification model evaluation
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("PART 2: BINARY CLASSIFICATION MODEL EVALUATION")
print("=" * 70)

data = {
    "study_hours": [
        1, 2, 3, 4, 5, 6, 7, 8,
        1.5, 2.5, 3.5, 4.5,
        5.5, 6.5, 7.5, 8.5,
        2, 3, 5, 6, 1, 4, 7, 8
    ],
    "attendance": [
        40, 50, 55, 65, 75, 85, 90, 95,
        45, 52, 60, 70,
        80, 88, 92, 96,
        48, 58, 78, 84, 42, 68, 91, 94
    ],
    "previous_marks": [
        25, 35, 45, 55, 65, 75, 85, 90,
        30, 38, 48, 58,
        68, 78, 88, 92,
        32, 42, 70, 76, 28, 56, 86, 91
    ],
    "result": [
        "Fail", "Fail", "Fail", "Pass", "Pass", "Pass", "Pass", "Pass",
        "Fail", "Fail", "Fail", "Pass",
        "Pass", "Pass", "Pass", "Pass",
        "Fail", "Fail", "Pass", "Pass", "Fail", "Pass", "Pass", "Pass"
    ],
}

df = pd.DataFrame(data)

print("\nDataset:")
print(df)

print("\nClass distribution:")
print(df["result"].value_counts())

X = df[["study_hours", "attendance", "previous_marks"]]
y = df["result"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\nActual:")
print(list(y_test))

print("\nPredicted:")
print(list(y_pred))

print("\nBinary Classification Metrics:")
print("Accuracy :", round(accuracy_score(y_test, y_pred), 2))
print("Precision:", round(precision_score(y_test, y_pred, pos_label="Pass"), 2))
print("Recall   :", round(recall_score(y_test, y_pred, pos_label="Pass"), 2))
print("F1-score :", round(f1_score(y_test, y_pred, pos_label="Pass"), 2))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred, labels=["Fail", "Pass"]))

print("\nClassification Report:")
print(classification_report(y_test, y_pred, zero_division=0))


# ------------------------------------------------------------
# PART 3: Multi-class classification metrics
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("PART 3: MULTI-CLASS CLASSIFICATION METRICS")
print("=" * 70)

multi_data = {
    "study_hours": [
        1, 2, 3, 4, 5, 6, 7, 8,
        1.5, 2.5, 3.5, 4.5,
        5.5, 6.5, 7.5, 8.5,
        2, 3, 5, 6, 1, 4, 7, 8
    ],
    "attendance": [
        40, 50, 55, 65, 75, 85, 90, 95,
        45, 52, 60, 70,
        80, 88, 92, 96,
        48, 58, 78, 84, 42, 68, 91, 94
    ],
    "previous_marks": [
        25, 35, 45, 55, 65, 75, 85, 90,
        30, 38, 48, 58,
        68, 78, 88, 92,
        32, 42, 70, 76, 28, 56, 86, 91
    ],
    "grade": [
        "D", "D", "C", "C", "B", "B", "A", "A",
        "D", "D", "C", "C",
        "B", "B", "A", "A",
        "D", "C", "B", "B", "D", "C", "A", "A"
    ],
}

multi_df = pd.DataFrame(multi_data)

X_multi = multi_df[["study_hours", "attendance", "previous_marks"]]
y_multi = multi_df["grade"]

X_train_multi, X_test_multi, y_train_multi, y_test_multi = train_test_split(
    X_multi,
    y_multi,
    test_size=0.25,
    random_state=42,
    stratify=y_multi,
)

multi_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
)

multi_model.fit(X_train_multi, y_train_multi)

y_pred_multi = multi_model.predict(X_test_multi)

print("\nActual grades:")
print(list(y_test_multi))

print("\nPredicted grades:")
print(list(y_pred_multi))

print("\nMulti-class Metrics:")
print("Accuracy        :", round(accuracy_score(y_test_multi, y_pred_multi), 2))
print("Macro Precision :", round(precision_score(y_test_multi, y_pred_multi, average="macro", zero_division=0), 2))
print("Macro Recall    :", round(recall_score(y_test_multi, y_pred_multi, average="macro", zero_division=0), 2))
print("Macro F1-score  :", round(f1_score(y_test_multi, y_pred_multi, average="macro", zero_division=0), 2))
print("Weighted F1     :", round(f1_score(y_test_multi, y_pred_multi, average="weighted", zero_division=0), 2))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test_multi, y_pred_multi))

print("\nClassification Report:")
print(classification_report(y_test_multi, y_pred_multi, zero_division=0))


# ------------------------------------------------------------
# PART 4: Imbalanced accuracy trap
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("PART 4: IMBALANCED DATA ACCURACY TRAP")
print("=" * 70)

imbalanced_data = {
    "study_hours": [6, 7, 8, 5, 6, 7, 8, 6, 7, 2],
    "attendance": [80, 85, 90, 75, 82, 88, 95, 84, 90, 40],
    "previous_marks": [70, 75, 85, 65, 72, 80, 90, 78, 88, 30],
    "result": ["Pass", "Pass", "Pass", "Pass", "Pass",
               "Pass", "Pass", "Pass", "Pass", "Fail"]
}

imb_df = pd.DataFrame(imbalanced_data)

X_imb = imb_df[["study_hours", "attendance", "previous_marks"]]
y_imb = imb_df["result"]

print("\nClass distribution:")
print(y_imb.value_counts())

# Dummy model always predicts majority class
dummy = DummyClassifier(strategy="most_frequent")
dummy.fit(X_imb, y_imb)
dummy_pred = dummy.predict(X_imb)

print("\nDummy model predictions:")
print(list(dummy_pred))

print("\nDummy model metrics:")
print("Accuracy :", round(accuracy_score(y_imb, dummy_pred), 2))
print("Precision:", round(precision_score(y_imb, dummy_pred, pos_label="Fail", zero_division=0), 2))
print("Recall   :", round(recall_score(y_imb, dummy_pred, pos_label="Fail", zero_division=0), 2))
print("F1-score :", round(f1_score(y_imb, dummy_pred, pos_label="Fail", zero_division=0), 2))

print("\nClassification Report:")
print(classification_report(y_imb, dummy_pred, zero_division=0))

print("""
Trainer note:
The dummy model gets high accuracy by predicting the majority class.
But for the minority class 'Fail', recall and F1-score are 0.
This proves accuracy alone can be misleading.
""")


# ------------------------------------------------------------
# PART 5: Summary
# ------------------------------------------------------------

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("""
Accuracy:
- Overall correct predictions.

Precision:
- When model says positive, how often is it correct?

Recall:
- Out of all actual positives, how many did model find?

F1-score:
- Balance between precision and recall.

For imbalanced data:
- Do not trust accuracy alone.
- Check precision, recall, F1-score, and confusion matrix.
""")
