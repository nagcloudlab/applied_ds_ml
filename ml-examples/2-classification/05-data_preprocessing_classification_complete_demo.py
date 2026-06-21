"""
Data Preprocessing for Classification - Complete Demo

Problem:
Predict whether a student will Pass or Fail.

This demo covers:
1. Missing value handling
2. Duplicate removal
3. Data type checking
4. Encoding categorical columns
5. Train-test split
6. Optional feature scaling
7. RandomForestClassifier training
8. Evaluation
9. New student prediction with same preprocessing

Install:
    pip install pandas scikit-learn
"""

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score


# ------------------------------------------------------------
# 1. Create messy sample dataset
# ------------------------------------------------------------

data = {
    "study_hours": [2, 5, None, 1, 4, 6, 3, 7, 5, 5],
    "attendance": [60, 85, 90, None, 75, 92, 55, 95, 85, 85],
    "previous_marks": [40, 70, 80, 25, 60, 85, 45, 90, 70, 70],
    "internet_access": ["No", "Yes", "Yes", "No", "Yes", "Yes", "No", "Yes", "Yes", "Yes"],
    "learning_mode": ["Offline", "Online", "Online", "Offline", "Hybrid", "Online", "Offline", "Hybrid", "Online", "Online"],
    "result": ["Fail", "Pass", "Pass", "Fail", "Pass", "Pass", "Fail", "Pass", "Pass", "Pass"],
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:")
print(df)

print("\nOriginal shape:", df.shape)

print("\nMissing values:")
print(df.isnull().sum())

print("\nData types:")
print(df.dtypes)


# ------------------------------------------------------------
# 2. Remove duplicate rows
# ------------------------------------------------------------

df = df.drop_duplicates()

print("\nAfter removing duplicates:")
print(df)

print("\nShape after duplicate removal:", df.shape)


# ------------------------------------------------------------
# 3. Handle missing values
# ------------------------------------------------------------

# Numerical missing values: fill with median
df["study_hours"] = df["study_hours"].fillna(df["study_hours"].median())
df["attendance"] = df["attendance"].fillna(df["attendance"].median())

# If categorical columns had missing values, fill with mode like this:
# df["internet_access"] = df["internet_access"].fillna(df["internet_access"].mode()[0])

print("\nAfter handling missing values:")
print(df)

print("\nMissing values after cleanup:")
print(df.isnull().sum())


# ------------------------------------------------------------
# 4. Encode categorical columns
# ------------------------------------------------------------

# Binary category: Yes/No -> 1/0
df["internet_access"] = df["internet_access"].map({
    "No": 0,
    "Yes": 1,
})

# Multi-category column: one-hot encoding
df = pd.get_dummies(
    df,
    columns=["learning_mode"],
    drop_first=True,
)

print("\nAfter encoding categorical columns:")
print(df)

print("\nColumns after encoding:")
print(df.columns.tolist())


# ------------------------------------------------------------
# 5. Separate features and target
# ------------------------------------------------------------

X = df.drop("result", axis=1)
y = df["result"]

print("\nFeatures:")
print(X)

print("\nTarget:")
print(y)


# ------------------------------------------------------------
# 6. Train-test split
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
# 7. Train Random Forest Classifier
# ------------------------------------------------------------
# Random Forest is tree-based, so scaling is usually not required.

rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
)

rf_model.fit(X_train, y_train)

rf_pred = rf_model.predict(X_test)

print("\nRandom Forest Results:")
print("Accuracy:", round(accuracy_score(y_test, rf_pred), 2))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, rf_pred))

print("\nClassification Report:")
print(classification_report(y_test, rf_pred, zero_division=0))


# ------------------------------------------------------------
# 8. Optional scaling example with Logistic Regression
# ------------------------------------------------------------
# Logistic Regression benefits from scaling.

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

log_model = LogisticRegression(
    random_state=42,
    max_iter=1000,
)

log_model.fit(X_train_scaled, y_train)

log_pred = log_model.predict(X_test_scaled)

print("\nLogistic Regression with Scaling Results:")
print("Accuracy:", round(accuracy_score(y_test, log_pred), 2))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, log_pred))

print("\nClassification Report:")
print(classification_report(y_test, log_pred, zero_division=0))


# ------------------------------------------------------------
# 9. Feature importance from Random Forest
# ------------------------------------------------------------

importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": rf_model.feature_importances_,
}).sort_values(by="Importance", ascending=False)

print("\nRandom Forest Feature Importance:")
print(importance)


# ------------------------------------------------------------
# 10. Predict new student
# ------------------------------------------------------------
# Important:
# New data must go through the SAME preprocessing steps:
# 1. encode internet_access
# 2. one-hot encode learning_mode
# 3. align columns with training data

new_student_raw = pd.DataFrame({
    "study_hours": [5],
    "attendance": [82],
    "previous_marks": [72],
    "internet_access": ["Yes"],
    "learning_mode": ["Online"],
})

print("\nRaw new student:")
print(new_student_raw)

# Encode binary column
new_student = new_student_raw.copy()

new_student["internet_access"] = new_student["internet_access"].map({
    "No": 0,
    "Yes": 1,
})

# One-hot encode learning_mode
new_student = pd.get_dummies(
    new_student,
    columns=["learning_mode"],
    drop_first=True,
)

# Align new_student columns with X training columns
# Missing columns are added with 0
new_student = new_student.reindex(columns=X.columns, fill_value=0)

print("\nPreprocessed new student:")
print(new_student)

rf_new_prediction = rf_model.predict(new_student)

print("\nRandom Forest prediction for new student:")
print(rf_new_prediction[0])


# Logistic Regression prediction needs scaled new data
new_student_scaled = scaler.transform(new_student)

log_new_prediction = log_model.predict(new_student_scaled)

print("\nLogistic Regression prediction for new student:")
print(log_new_prediction[0])


# ------------------------------------------------------------
# 11. Simple trainer summary
# ------------------------------------------------------------

print("\nSummary:")
print("""
Data preprocessing means preparing raw data for ML.

Main steps:
- Remove duplicates
- Handle missing values
- Encode categorical columns
- Split train/test correctly
- Scale features if the algorithm needs it
- Apply the same preprocessing to new data before prediction

Memory:
Clean data first, train model second.
""")
