# Day 3: Supervised Learning — Classification
## Section 6: Data Preprocessing for Classification

## Slide 1: Section Opening

# Data Preprocessing for Classification

### Clean data first, train model second

Before training a classification model, we must prepare the data properly.

This is called **data preprocessing**.

Simple meaning:

> **Data preprocessing means cleaning and converting raw data into a format that ML models can understand.**

---

## Slide 2: Why Preprocessing Is Needed

Real-world data is usually messy.

Example student dataset:

| Study Hours | Attendance | Previous Marks | Gender | Internet Access | Result |
|---:|---:|---:|---|---|---|
| 2 | 60 | 40 | Male | Yes | Fail |
| 5 | 85 | 70 | Female | Yes | Pass |
| None | 90 | 80 | Female | No | Pass |
| 1 | None | 25 | Male | No | Fail |

Problems:

```text
Missing values
Text values
Different scales
Duplicate records
Wrong data types
Imbalanced classes
```

---

## Slide 3: ML Models Need Clean Data

Most ML models expect clean numerical input.

Raw data may contain:

- Missing numbers
- Text categories
- Incorrect data types
- Duplicate rows
- Very different feature ranges

So before training:

```text
Raw data → Preprocessing → Clean model-ready data
```

---

## Slide 4: Common Preprocessing Tasks

For classification, common preprocessing steps include:

```text
1. Handling missing values
2. Encoding categorical columns
3. Feature scaling
4. Train-test split
5. Handling class imbalance
6. Removing duplicates
7. Checking data types
```

We will learn these one by one.

---

## Slide 5: Handling Missing Values

Missing values mean some data is absent.

Example:

| Study Hours | Attendance | Previous Marks | Result |
|---:|---:|---:|---|
| 2 | 60 | 40 | Fail |
| None | 85 | 70 | Pass |
| 6 | None | 80 | Pass |

Here:

```text
Study Hours missing in row 2
Attendance missing in row 3
```

ML models usually cannot directly handle missing values.

---

## Slide 6: Ways to Handle Missing Values

Common options:

```text
1. Remove rows with missing values
2. Fill numerical missing values with mean/median
3. Fill categorical missing values with mode
4. Use advanced imputation techniques
```

For beginners:

```text
Numerical columns → fill with mean or median
Categorical columns → fill with mode
```

Example:

```text
Missing attendance → fill with median attendance
Missing gender → fill with most common gender
```

---

## Slide 7: Python Example — Missing Values

```python
import pandas as pd

data = {
    "study_hours": [2, 5, None, 1],
    "attendance": [60, 85, 90, None],
    "previous_marks": [40, 70, 80, 25],
    "result": ["Fail", "Pass", "Pass", "Fail"]
}

df = pd.DataFrame(data)

print(df.isnull().sum())

df["study_hours"] = df["study_hours"].fillna(df["study_hours"].mean())
df["attendance"] = df["attendance"].fillna(df["attendance"].mean())

print(df)
```

---

## Slide 8: Encoding Categorical Columns

Many datasets contain text columns.

Example:

| Gender | Internet Access | Result |
|---|---|---|
| Male | Yes | Fail |
| Female | Yes | Pass |
| Female | No | Pass |

ML models usually need numbers, not text.

So we convert categories into numbers.

This is called **encoding**.

---

## Slide 9: Label Encoding

Label encoding converts categories into numbers.

Example:

```text
No  → 0
Yes → 1
```

For binary columns like:

```text
Internet Access = Yes / No
```

label encoding is fine.

Python:

```python
df["internet_access"] = df["internet_access"].map({
    "No": 0,
    "Yes": 1
})
```

---

## Slide 10: One-Hot Encoding

For columns with more than two categories, one-hot encoding is usually better.

Example:

```text
Learning Mode = Online / Offline / Hybrid
```

One-hot encoding creates separate columns:

| Online | Offline | Hybrid |
|---:|---:|---:|
| 1 | 0 | 0 |
| 0 | 1 | 0 |
| 0 | 0 | 1 |

Python:

```python
df = pd.get_dummies(df, columns=["learning_mode"], drop_first=True)
```

---

## Slide 11: Why Not Always Label Encode?

Suppose:

```text
Online = 0
Offline = 1
Hybrid = 2
```

The model may think:

```text
Hybrid is greater than Offline
Offline is greater than Online
```

But these are just categories.

There is no natural ranking.

So for nominal categories, one-hot encoding is safer.

---

## Slide 12: Feature Scaling

Feature scaling means bringing numerical features to a similar range.

Example:

| Study Hours | Attendance | Previous Marks |
|---:|---:|---:|
| 2 | 60 | 40 |
| 8 | 95 | 90 |

Ranges:

```text
Study Hours: 1 to 8
Attendance: 40 to 100
Previous Marks: 25 to 100
```

Some algorithms are sensitive to scale.

---

## Slide 13: Algorithms Sensitive to Scaling

Scaling is important for:

```text
KNN
SVM
Logistic Regression
Neural Networks
```

Tree-based models usually do not require scaling:

```text
Decision Tree
Random Forest
```

Why?

Because tree models split using conditions like:

```text
attendance <= 70
previous_marks <= 50
```

---

## Slide 14: StandardScaler Example

```python
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

Important:

```text
fit_transform on training data
transform only on test data
```

Why?

Because test data should behave like unseen future data.

---

## Slide 15: Correct Order for Scaling

Correct order:

```text
Split data first
Fit scaler on training data
Transform training data
Transform test data
```

Correct:

```python
X_train, X_test, y_train, y_test = train_test_split(X, y)

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

---

## Slide 16: What Is Data Leakage?

Data leakage means:

> **Information from test data accidentally enters the training process.**

Wrong:

```python
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y)
```

Here, scaler learned from full data, including test data.

---

## Slide 17: Correct Way to Avoid Data Leakage

Correct:

```python
X_train, X_test, y_train, y_test = train_test_split(X, y)

scaler.fit(X_train)

X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

Golden rule:

```text
Learn preprocessing only from training data.
Apply it to test data.
```

---

## Slide 18: Removing Duplicates

Sometimes data has duplicate rows.

Example:

| Study Hours | Attendance | Marks | Result |
|---:|---:|---:|---|
| 5 | 85 | 70 | Pass |
| 5 | 85 | 70 | Pass |

Remove duplicates:

```python
df = df.drop_duplicates()
```

This prevents repeated records from biasing the model.

---

## Slide 19: Checking Data Types

Sometimes numerical columns are read as text.

Example:

```text
"85" instead of 85
```

Check data types:

```python
print(df.dtypes)
```

Convert if needed:

```python
df["attendance"] = pd.to_numeric(df["attendance"], errors="coerce")
```

---

## Slide 20: Complete Example — Imports

```python
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
```

We use:

- pandas for data
- train_test_split for splitting
- StandardScaler for scaling demo
- RandomForestClassifier for model
- classification_report for evaluation

---

## Slide 21: Complete Example — Dataset

```python
data = {
    "study_hours": [2, 5, None, 1, 4, 6, 3, 7],
    "attendance": [60, 85, 90, None, 75, 92, 55, 95],
    "previous_marks": [40, 70, 80, 25, 60, 85, 45, 90],
    "internet_access": ["No", "Yes", "Yes", "No", "Yes", "Yes", "No", "Yes"],
    "learning_mode": ["Offline", "Online", "Online", "Offline", "Hybrid", "Online", "Offline", "Hybrid"],
    "result": ["Fail", "Pass", "Pass", "Fail", "Pass", "Pass", "Fail", "Pass"]
}

df = pd.DataFrame(data)
```

---

## Slide 22: Complete Example — Remove Duplicates

```python
df = df.drop_duplicates()
```

Why?

```text
Duplicate records can bias model learning.
```

This is usually a safe early cleanup step.

---

## Slide 23: Complete Example — Fill Missing Values

```python
df["study_hours"] = df["study_hours"].fillna(df["study_hours"].median())
df["attendance"] = df["attendance"].fillna(df["attendance"].median())
```

Meaning:

```text
Missing study_hours → fill with median study_hours
Missing attendance → fill with median attendance
```

Median is often safer than mean when outliers exist.

---

## Slide 24: Complete Example — Encode Binary Column

```python
df["internet_access"] = df["internet_access"].map({
    "No": 0,
    "Yes": 1
})
```

Meaning:

```text
No  → 0
Yes → 1
```

This is suitable because the column has only two values.

---

## Slide 25: Complete Example — One-Hot Encoding

```python
df = pd.get_dummies(df, columns=["learning_mode"], drop_first=True)
```

This converts:

```text
learning_mode = Offline / Online / Hybrid
```

into numerical dummy columns.

Example output columns may include:

```text
learning_mode_Offline
learning_mode_Online
```

---

## Slide 26: Complete Example — X and y

```python
X = df.drop("result", axis=1)
y = df["result"]
```

Meaning:

```text
X = all input columns except result
y = target column
```

Golden rule:

```text
Target should not be inside features.
```

---

## Slide 27: Complete Example — Train-Test Split

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)
```

Meaning:

```text
75% training
25% testing
```

`stratify=y` keeps Pass/Fail class ratio balanced.

---

## Slide 28: Complete Example — Train Model

```python
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)
```

Random Forest is tree-based, so scaling is usually not required.

---

## Slide 29: Complete Example — Predict and Evaluate

```python
y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred))
```

This shows classification metrics like:

```text
precision
recall
f1-score
support
```

---

## Slide 30: Why No Scaling in Random Forest Example?

Random Forest is tree-based.

Tree-based models split based on conditions like:

```text
attendance <= 70
previous_marks <= 50
```

They do not depend heavily on feature scale.

So for Random Forest:

```text
Scaling usually not required.
```

---

## Slide 31: When Scaling Is Needed

Scaling is important for algorithms like:

```text
KNN
SVM
Logistic Regression
Neural Networks
```

Example:

```python
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

Use scaling when the algorithm is distance-based or gradient-based.

---

## Slide 32: Preprocessing Checklist

Before classification model training, check:

```text
Are missing values handled?
Are text columns encoded?
Are duplicates removed?
Are data types correct?
Are features and target separated?
Is train-test split done properly?
Is scaling needed for this algorithm?
Is class imbalance present?
```

This checklist prevents many ML mistakes.

---

## Slide 33: Final Summary

Remember:

```text
Data preprocessing = preparing raw data for ML model.
```

Main steps:

```text
Handle missing values
Encode categorical columns
Scale features if needed
Remove duplicates
Check data types
Avoid data leakage
Split train/test correctly
```

---

## Slide 34: Memory Hook

```text
Clean data first, train model second.
```

Simple workflow:

```text
Raw data
    ↓
Clean missing values
    ↓
Encode text columns
    ↓
Split train/test
    ↓
Scale if needed
    ↓
Train model
```

Next topic:

# Class Imbalance Introduction
