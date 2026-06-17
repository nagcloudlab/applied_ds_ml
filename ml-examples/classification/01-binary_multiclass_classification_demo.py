"""
Day 3 Classification Demo
Binary Classification vs Multi-class Classification

This demo covers:
1. Binary classification: Student Pass / Fail prediction
2. Multi-class classification: Student Grade prediction
3. Train-test split
4. DecisionTreeClassifier
5. Accuracy, Precision, Recall, F1-score
6. Confusion matrix and classification report
7. New data prediction
8. Prediction probabilities

Install:
    pip install pandas scikit-learn
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report,
)


# ============================================================
# PART 1: BINARY CLASSIFICATION
# Problem: Predict Pass or Fail
# ============================================================

print("\n" + "=" * 70)
print("PART 1: BINARY CLASSIFICATION - PASS / FAIL PREDICTION")
print("=" * 70)

binary_data = {
    "study_hours": [
        1, 2, 3, 4, 5, 6, 7, 8,
        1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5,
        2, 3, 5, 6, 1, 4, 7, 8
    ],
    "attendance": [
        40, 50, 55, 65, 75, 85, 90, 95,
        45, 52, 60, 70, 80, 88, 92, 96,
        48, 58, 78, 84, 42, 68, 91, 94
    ],
    "previous_marks": [
        25, 35, 45, 55, 65, 75, 85, 90,
        30, 38, 48, 58, 68, 78, 88, 92,
        32, 42, 70, 76, 28, 56, 86, 91
    ],
    "result": [
        "Fail", "Fail", "Fail", "Pass", "Pass", "Pass", "Pass", "Pass",
        "Fail", "Fail", "Fail", "Pass", "Pass", "Pass", "Pass", "Pass",
        "Fail", "Fail", "Pass", "Pass", "Fail", "Pass", "Pass", "Pass"
    ],
}

binary_df = pd.DataFrame(binary_data)

print("\nBinary classification dataset:")
print(binary_df)

print("\nClass distribution:")
print(binary_df["result"].value_counts())

# Features and target
X_binary = binary_df[["study_hours", "attendance", "previous_marks"]]
y_binary = binary_df["result"]

# Train-test split
X_train_binary, X_test_binary, y_train_binary, y_test_binary = train_test_split(
    X_binary,
    y_binary,
    test_size=0.25,
    random_state=42,
    stratify=y_binary,
)

# Create model
binary_model = DecisionTreeClassifier(
    random_state=42,
    max_depth=3,
)

# Train model
binary_model.fit(X_train_binary, y_train_binary)

# Predict test data
y_pred_binary = binary_model.predict(X_test_binary)

print("\nActual binary results:")
print(list(y_test_binary))

print("\nPredicted binary results:")
print(list(y_pred_binary))

# Evaluation
binary_accuracy = accuracy_score(y_test_binary, y_pred_binary)
binary_precision = precision_score(
    y_test_binary,
    y_pred_binary,
    pos_label="Pass",
)
binary_recall = recall_score(
    y_test_binary,
    y_pred_binary,
    pos_label="Pass",
)
binary_f1 = f1_score(
    y_test_binary,
    y_pred_binary,
    pos_label="Pass",
)

print("\nBinary Classification Evaluation:")
print("Accuracy :", round(binary_accuracy, 2))
print("Precision:", round(binary_precision, 2))
print("Recall   :", round(binary_recall, 2))
print("F1 Score :", round(binary_f1, 2))

print("\nBinary Confusion Matrix:")
print(confusion_matrix(y_test_binary, y_pred_binary))

print("\nBinary Classification Report:")
print(classification_report(y_test_binary, y_pred_binary))

# Predict new students
new_students_binary = pd.DataFrame({
    "study_hours": [2, 5, 7],
    "attendance": [50, 82, 90],
    "previous_marks": [35, 72, 88],
})

new_binary_predictions = binary_model.predict(new_students_binary)
new_binary_probabilities = binary_model.predict_proba(new_students_binary)

print("\nNew students for binary prediction:")
print(new_students_binary)

print("\nPredicted Pass/Fail:")
for i, prediction in enumerate(new_binary_predictions):
    print(f"Student {i + 1}: {prediction}")

print("\nClass order:")
print(binary_model.classes_)

print("\nPrediction probabilities:")
print(new_binary_probabilities)


# ============================================================
# PART 2: MULTI-CLASS CLASSIFICATION
# Problem: Predict Grade A / B / C / D
# ============================================================

print("\n" + "=" * 70)
print("PART 2: MULTI-CLASS CLASSIFICATION - GRADE PREDICTION")
print("=" * 70)

multiclass_data = {
    "study_hours": [
        1, 2, 3, 4, 5, 6, 7, 8,
        1.5, 2.5, 3.5, 4.5, 5.5, 6.5, 7.5, 8.5,
        2, 3, 5, 6, 1, 4, 7, 8
    ],
    "attendance": [
        40, 50, 55, 65, 75, 85, 90, 95,
        45, 52, 60, 70, 80, 88, 92, 96,
        48, 58, 78, 84, 42, 68, 91, 94
    ],
    "previous_marks": [
        25, 35, 45, 55, 65, 75, 85, 90,
        30, 38, 48, 58, 68, 78, 88, 92,
        32, 42, 70, 76, 28, 56, 86, 91
    ],
    "grade": [
        "D", "D", "C", "C", "B", "B", "A", "A",
        "D", "D", "C", "C", "B", "B", "A", "A",
        "D", "C", "B", "B", "D", "C", "A", "A"
    ],
}

multiclass_df = pd.DataFrame(multiclass_data)

print("\nMulti-class classification dataset:")
print(multiclass_df)

print("\nClass distribution:")
print(multiclass_df["grade"].value_counts())

# Features and target
X_multi = multiclass_df[["study_hours", "attendance", "previous_marks"]]
y_multi = multiclass_df["grade"]

# Train-test split
X_train_multi, X_test_multi, y_train_multi, y_test_multi = train_test_split(
    X_multi,
    y_multi,
    test_size=0.25,
    random_state=42,
    stratify=y_multi,
)

# Create model
multi_model = DecisionTreeClassifier(
    random_state=42,
    max_depth=4,
)

# Train model
multi_model.fit(X_train_multi, y_train_multi)

# Predict test data
y_pred_multi = multi_model.predict(X_test_multi)

print("\nActual multi-class grades:")
print(list(y_test_multi))

print("\nPredicted multi-class grades:")
print(list(y_pred_multi))

# Evaluation
multi_accuracy = accuracy_score(y_test_multi, y_pred_multi)

# For multi-class classification, use average="macro" or average="weighted".
# macro = treats all classes equally
# weighted = considers class support/count
multi_precision = precision_score(
    y_test_multi,
    y_pred_multi,
    average="macro",
    zero_division=0,
)
multi_recall = recall_score(
    y_test_multi,
    y_pred_multi,
    average="macro",
    zero_division=0,
)
multi_f1 = f1_score(
    y_test_multi,
    y_pred_multi,
    average="macro",
    zero_division=0,
)

print("\nMulti-class Classification Evaluation:")
print("Accuracy :", round(multi_accuracy, 2))
print("Precision:", round(multi_precision, 2))
print("Recall   :", round(multi_recall, 2))
print("F1 Score :", round(multi_f1, 2))

print("\nMulti-class Confusion Matrix:")
print(confusion_matrix(y_test_multi, y_pred_multi))

print("\nMulti-class Classification Report:")
print(classification_report(y_test_multi, y_pred_multi, zero_division=0))

# Predict new students
new_students_multi = pd.DataFrame({
    "study_hours": [2, 5, 7, 8],
    "attendance": [50, 78, 90, 96],
    "previous_marks": [35, 68, 88, 93],
})

new_multi_predictions = multi_model.predict(new_students_multi)
new_multi_probabilities = multi_model.predict_proba(new_students_multi)

print("\nNew students for multi-class prediction:")
print(new_students_multi)

print("\nPredicted Grades:")
for i, prediction in enumerate(new_multi_predictions):
    print(f"Student {i + 1}: Grade {prediction}")

print("\nClass order:")
print(multi_model.classes_)

print("\nPrediction probabilities:")
print(new_multi_probabilities)


# ============================================================
# PART 3: QUICK SUMMARY
# ============================================================

print("\n" + "=" * 70)
print("SUMMARY")
print("=" * 70)

print("""
Binary Classification:
- Target has exactly 2 classes.
- Example: Pass / Fail.
- Metrics: accuracy, precision, recall, F1-score.

Multi-class Classification:
- Target has 3 or more classes.
- Example: Grade A / B / C / D.
- Use average='macro' or average='weighted' for precision/recall/F1.

Memory:
- Binary = either this or that.
- Multi-class = choose one from many.
""")
