"""
Decision Tree Classifier Complete Demo
Problem: Student Pass / Fail Prediction

This demo covers:
1. Dataset creation
2. Features and target
3. Train-test split
4. DecisionTreeClassifier
5. Accuracy, confusion matrix, classification report
6. New student prediction
7. Prediction probability
8. Printing tree rules

Install:
    pip install pandas scikit-learn
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

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
# 4. Create Decision Tree Classifier
# ------------------------------------------------------------

model = DecisionTreeClassifier(
    random_state=42,
    max_depth=3,
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
    "study_hours": [5, 2, 7],
    "attendance": [82, 50, 90],
    "previous_marks": [72, 35, 88],
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
# 10. Print decision tree rules
# ------------------------------------------------------------

tree_rules = export_text(
    model,
    feature_names=list(X.columns),
)

print("\nDecision Tree Rules:")
print(tree_rules)


# ------------------------------------------------------------
# 11. Simple trainer summary
# ------------------------------------------------------------

print("\nSummary:")
print("""
Decision Tree Classifier:
- Predicts categories/classes.
- Works like a flowchart.
- Asks questions and follows branches.
- Final leaf gives class prediction.
- Easy to explain but can overfit if tree becomes too deep.
""")
