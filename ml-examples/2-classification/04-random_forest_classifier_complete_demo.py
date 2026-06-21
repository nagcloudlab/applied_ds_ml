"""
Random Forest Classifier Complete Demo
Problem: Student Pass / Fail Prediction

This demo covers:
1. Dataset creation
2. Features and target
3. Train-test split
4. RandomForestClassifier
5. Accuracy, confusion matrix, classification report
6. New student prediction
7. Prediction probability
8. Feature importance

Install:
    pip install pandas scikit-learn
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    confusion_matrix,
    classification_report,
)


# ------------------------------------------------------------
# 1. Create sample dataset
# ------------------------------------------------------------

data = {
    "study_hours": [
        1, 2, 3, 4, 5, 6, 7, 8,
        1.5, 2.5, 3.5, 4.5,
        5.5, 6.5, 7.5, 8.5,
        2, 3, 5, 6, 1, 4, 7, 8,
        2.2, 3.2, 4.2, 5.2, 6.2, 7.2
    ],
    "attendance": [
        40, 50, 55, 65, 75, 85, 90, 95,
        45, 52, 60, 70,
        80, 88, 92, 96,
        48, 58, 78, 84, 42, 68, 91, 94,
        51, 59, 69, 79, 86, 93
    ],
    "previous_marks": [
        25, 35, 45, 55, 65, 75, 85, 90,
        30, 38, 48, 58,
        68, 78, 88, 92,
        32, 42, 70, 76, 28, 56, 86, 91,
        36, 44, 57, 66, 79, 89
    ],
    "result": [
        "Fail", "Fail", "Fail", "Pass", "Pass", "Pass", "Pass", "Pass",
        "Fail", "Fail", "Fail", "Pass",
        "Pass", "Pass", "Pass", "Pass",
        "Fail", "Fail", "Pass", "Pass", "Fail", "Pass", "Pass", "Pass",
        "Fail", "Fail", "Pass", "Pass", "Pass", "Pass"
    ],
}

df = pd.DataFrame(data)

print("\nDataset:")
print(df)

print("\nClass distribution:")
print(df["result"].value_counts())


# ------------------------------------------------------------
# 2. Separate features and target
# ------------------------------------------------------------

X = df[["study_hours", "attendance", "previous_marks"]]
y = df["result"]

print("\nFeatures:")
print(X.head())

print("\nTarget:")
print(y.head())


# ------------------------------------------------------------
# 3. Train-test split
# ------------------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y,
)

print("\nTraining rows:", len(X_train))
print("Testing rows:", len(X_test))


# ------------------------------------------------------------
# 4. Create Random Forest Classifier
# ------------------------------------------------------------

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=3,
    random_state=42,
)


# ------------------------------------------------------------
# 5. Train the model
# ------------------------------------------------------------

model.fit(X_train, y_train)


# ------------------------------------------------------------
# 6. Predict test data
# ------------------------------------------------------------

y_pred = model.predict(X_test)

print("\nActual results:")
print(list(y_test))

print("\nPredicted results:")
print(list(y_pred))


# ------------------------------------------------------------
# 7. Evaluate model
# ------------------------------------------------------------

accuracy = accuracy_score(y_test, y_pred)

print("\nModel Evaluation:")
print("Accuracy:", round(accuracy, 2))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# ------------------------------------------------------------
# 8. Predict new students
# ------------------------------------------------------------

new_students = pd.DataFrame({
    "study_hours": [5, 2, 7, 3.5],
    "attendance": [82, 50, 90, 58],
    "previous_marks": [72, 35, 88, 45],
})

new_predictions = model.predict(new_students)

print("\nNew Students:")
print(new_students)

print("\nPredicted Results:")
for i, prediction in enumerate(new_predictions, start=1):
    print(f"Student {i}: {prediction}")


# ------------------------------------------------------------
# 9. Predict probabilities
# ------------------------------------------------------------

probabilities = model.predict_proba(new_students)

print("\nClass order:")
print(model.classes_)

print("\nPrediction probabilities:")
print(probabilities)


# ------------------------------------------------------------
# 10. Feature importance
# ------------------------------------------------------------

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_,
}).sort_values(by="Importance", ascending=False)

print("\nFeature Importance:")
print(importance)


# ------------------------------------------------------------
# 11. Simple trainer summary
# ------------------------------------------------------------

print("\nSummary:")
print("""
Random Forest Classifier:
- Uses many Decision Trees.
- Each tree predicts a class.
- Final prediction is based on majority voting.
- Usually more stable than a single Decision Tree.
- Can show feature importance.
""")
