"""
Class Imbalance Introduction - Complete Demo

Problem:
Predict student Pass / Fail where Fail is the minority class.

This demo covers:
1. Creating an imbalanced classification dataset
2. Checking class distribution
3. Accuracy trap with a dummy majority-class model
4. Train-test split with stratify
5. RandomForestClassifier without class_weight
6. RandomForestClassifier with class_weight="balanced"
7. Precision, recall, F1-score, confusion matrix
8. Simple oversampling demonstration

Install:
    pip install pandas scikit-learn
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
)


# ------------------------------------------------------------
# 1. Create imbalanced dataset
# ------------------------------------------------------------

# Majority class: Pass
# Minority class: Fail

data = {
    "study_hours": [
        6, 7, 8, 5, 6, 7, 8, 6, 7, 8,
        5, 6, 7, 8, 6, 7, 5, 8, 7, 6,
        2, 1.5, 2.5
    ],
    "attendance": [
        80, 85, 90, 75, 82, 88, 95, 84, 90, 93,
        78, 81, 87, 94, 83, 89, 76, 96, 91, 85,
        42, 38, 45
    ],
    "previous_marks": [
        70, 75, 85, 65, 72, 80, 90, 78, 88, 92,
        68, 74, 82, 91, 76, 86, 66, 94, 89, 79,
        30, 25, 35
    ],
    "result": [
        "Pass", "Pass", "Pass", "Pass", "Pass",
        "Pass", "Pass", "Pass", "Pass", "Pass",
        "Pass", "Pass", "Pass", "Pass", "Pass",
        "Pass", "Pass", "Pass", "Pass", "Pass",
        "Fail", "Fail", "Fail"
    ],
}

df = pd.DataFrame(data)

print("\nDataset:")
print(df)

print("\nClass distribution:")
print(df["result"].value_counts())

print("\nClass percentage:")
print(df["result"].value_counts(normalize=True) * 100)


# ------------------------------------------------------------
# 2. Separate features and target
# ------------------------------------------------------------

X = df[["study_hours", "attendance", "previous_marks"]]
y = df["result"]


# ------------------------------------------------------------
# 3. Train-test split with stratify
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.35,
    random_state=42,
    stratify=y,
)

print("\nTraining class distribution:")
print(y_train.value_counts())

print("\nTesting class distribution:")
print(y_test.value_counts())


# ------------------------------------------------------------
# 4. Accuracy trap using DummyClassifier
# ------------------------------------------------------------
# This model always predicts the majority class.

dummy_model = DummyClassifier(strategy="most_frequent")

dummy_model.fit(X_train, y_train)

dummy_pred = dummy_model.predict(X_test)

print("\n" + "=" * 70)
print("DUMMY MODEL: ALWAYS PREDICTS MAJORITY CLASS")
print("=" * 70)

print("\nActual results:")
print(list(y_test))

print("\nDummy predictions:")
print(list(dummy_pred))

print("\nAccuracy:", round(accuracy_score(y_test, dummy_pred), 2))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, dummy_pred))

print("\nClassification Report:")
print(classification_report(y_test, dummy_pred, zero_division=0))

print("""
Trainer note:
The dummy model may show good accuracy because most students are Pass.
But it usually fails to identify the minority class: Fail.
""")


# ------------------------------------------------------------
# 5. Random Forest without class_weight
# ------------------------------------------------------------

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

print("\n" + "=" * 70)
print("RANDOM FOREST WITHOUT CLASS_WEIGHT")
print("=" * 70)

print("\nAccuracy:", round(accuracy_score(y_test, rf_pred), 2))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, rf_pred))

print("\nClassification Report:")
print(classification_report(y_test, rf_pred, zero_division=0))


# ------------------------------------------------------------
# 6. Random Forest with class_weight="balanced"
# ------------------------------------------------------------

balanced_rf_model = RandomForestClassifier(
    n_estimators=100,
    class_weight="balanced",
    random_state=42,
)

balanced_rf_model.fit(X_train, y_train)

balanced_rf_pred = balanced_rf_model.predict(X_test)

print("\n" + "=" * 70)
print('RANDOM FOREST WITH class_weight="balanced"')
print("=" * 70)

print("\nAccuracy:", round(accuracy_score(y_test, balanced_rf_pred), 2))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, balanced_rf_pred))

print("\nClassification Report:")
print(classification_report(y_test, balanced_rf_pred, zero_division=0))


# ------------------------------------------------------------
# 7. Simple oversampling demonstration
# ------------------------------------------------------------
# This is a beginner-friendly manual oversampling example.
# We duplicate minority class rows in the TRAINING DATA only.

train_df = X_train.copy()
train_df["result"] = y_train.values

majority_df = train_df[train_df["result"] == "Pass"]
minority_df = train_df[train_df["result"] == "Fail"]

print("\n" + "=" * 70)
print("OVERSAMPLING DEMO")
print("=" * 70)

print("\nBefore oversampling:")
print(train_df["result"].value_counts())

# Oversample minority class by sampling with replacement
minority_oversampled = minority_df.sample(
    n=len(majority_df),
    replace=True,
    random_state=42,
)

oversampled_train_df = pd.concat(
    [majority_df, minority_oversampled],
    axis=0,
).sample(frac=1, random_state=42)

print("\nAfter oversampling:")
print(oversampled_train_df["result"].value_counts())

X_train_over = oversampled_train_df[["study_hours", "attendance", "previous_marks"]]
y_train_over = oversampled_train_df["result"]

oversampled_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
)

oversampled_model.fit(X_train_over, y_train_over)

oversampled_pred = oversampled_model.predict(X_test)

print("\nOversampled Random Forest Results:")

print("\nAccuracy:", round(accuracy_score(y_test, oversampled_pred), 2))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, oversampled_pred))

print("\nClassification Report:")
print(classification_report(y_test, oversampled_pred, zero_division=0))


# ------------------------------------------------------------
# 8. Predict new students
# ------------------------------------------------------------

new_students = pd.DataFrame({
    "study_hours": [7, 2],
    "attendance": [90, 40],
    "previous_marks": [88, 30],
})

new_predictions = balanced_rf_model.predict(new_students)

print("\nNew students:")
print(new_students)

print("\nPredictions using balanced Random Forest:")
for i, pred in enumerate(new_predictions, start=1):
    print(f"Student {i}: {pred}")


# ------------------------------------------------------------
# 9. Simple trainer summary
# ------------------------------------------------------------

print("\nSummary:")
print("""
Class imbalance means one class has many records and another class has very few.

Danger:
- Accuracy can look high.
- Model may ignore minority class.

What to do:
- Check value_counts()
- Use stratify=y
- Check precision, recall, and F1-score
- Try class_weight="balanced"
- Try oversampling minority class
- Collect more minority class data when possible

Memory:
High accuracy is not always a good model.
Check minority class performance.
""")
