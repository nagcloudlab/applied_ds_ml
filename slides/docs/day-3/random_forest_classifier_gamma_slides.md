# Day 3: Supervised Learning — Classification
## Section 5: Random Forest Classifier

## Slide 1: Section Opening

# Random Forest Classifier

### Many decision trees working together

In the previous section, we learned **Decision Tree Classifier**.

Decision Tree thinks like this:

```text
Ask questions step by step → reach final class
```

Random Forest thinks like this:

```text
Use many decision trees → combine their answers → final class
```

---

## Slide 2: What Is Random Forest Classifier?

Random Forest Classifier is a classification algorithm.

Simple meaning:

> **Random Forest Classifier uses many Decision Trees together to predict a category.**

One decision tree may make mistakes.

So Random Forest builds many trees and combines their predictions.

For classification, the final answer is usually decided by **majority voting**.

---

## Slide 3: Simple Analogy

Imagine one teacher predicts whether a student will pass or fail.

One teacher may say:

```text
Pass
```

But maybe that teacher is wrong.

Now imagine asking 100 teachers.

```text
Teacher 1 → Pass
Teacher 2 → Pass
Teacher 3 → Fail
Teacher 4 → Pass
Teacher 5 → Pass
...
```

If most teachers say **Pass**, final prediction is:

```text
Pass
```

---

## Slide 4: Decision Tree vs Random Forest Analogy

```text
Decision Tree = one teacher
Random Forest = group of teachers
```

One teacher gives one opinion.

Many teachers give many opinions.

The final answer is based on majority opinion.

---

## Slide 5: Why Is It Called Random Forest?

It is called **Forest** because it contains many trees.

```text
Decision Tree = one tree
Random Forest = many trees
```

It is called **Random** because each tree is trained slightly differently.

Each tree may see:

- Different rows of data
- Different features
- Different split decisions

This makes the forest more stable than one single tree.

---

## Slide 6: Decision Tree vs Random Forest

| Point | Decision Tree Classifier | Random Forest Classifier |
|---|---|---|
| Number of trees | One tree | Many trees |
| Prediction style | One tree decides | Many trees vote |
| Overfitting risk | Higher | Lower |
| Stability | Less stable | More stable |
| Explainability | Easier | Medium |
| Performance | Good baseline | Often better |

Simple memory:

```text
Decision Tree = one opinion
Random Forest = many opinions
```

---

## Slide 7: Running Example

We want to predict:

```text
Pass or Fail
```

Features:

```text
Study Hours
Attendance
Previous Marks
```

Target:

```text
Result
```

Random Forest builds many decision trees using this data.

---

## Slide 8: Student Dataset

| Study Hours | Attendance | Previous Marks | Result |
|---:|---:|---:|---|
| 2 | 60 | 40 | Fail |
| 5 | 85 | 70 | Pass |
| 6 | 90 | 80 | Pass |
| 1 | 45 | 25 | Fail |
| 4 | 75 | 60 | Pass |
| 3 | 55 | 45 | Fail |

This is a binary classification problem.

Target classes:

```text
Pass
Fail
```

---

## Slide 9: How Random Forest Predicts

Suppose we have a new student:

```text
Study Hours = 5
Attendance = 82
Previous Marks = 72
```

Different trees may predict:

| Tree | Prediction |
|---|---|
| Tree 1 | Pass |
| Tree 2 | Pass |
| Tree 3 | Fail |
| Tree 4 | Pass |
| Tree 5 | Pass |

Voting:

```text
Pass = 4 votes
Fail = 1 vote
```

Final prediction:

```text
Pass
```

---

## Slide 10: Majority Voting

Random Forest Classifier uses **majority voting**.

For classification:

```text
Each tree gives one class prediction.
The class with the most votes becomes the final prediction.
```

Example:

```text
Tree 1 → Pass
Tree 2 → Pass
Tree 3 → Fail
Tree 4 → Pass
Tree 5 → Fail
```

Final:

```text
Pass
```

---

## Slide 11: Why Random Forest Is Better Than One Decision Tree

A single Decision Tree can overfit.

It may learn very specific rules like:

```text
If study_hours = 4.5 and attendance = 70 and previous_marks = 58 → Pass
```

This may work on training data but fail on new data.

Random Forest reduces this problem because it combines many trees.

One tree may overfit.

Many trees together usually give a more reliable answer.

---

## Slide 12: Important Parameter — n_estimators

In Scikit-learn, Random Forest uses:

```python
n_estimators=100
```

Meaning:

```text
Build 100 decision trees.
```

Example:

```python
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
```

More trees may improve stability, but training can become slower.

---

## Slide 13: Important Parameter — max_depth

Like Decision Tree, Random Forest trees can also become deep.

```python
max_depth=3
```

Meaning:

```text
Each tree can grow only up to 3 levels.
```

This helps reduce overfitting.

Example:

```python
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=3,
    random_state=42
)
```

---

## Slide 14: Random Forest Classifier in Python

Basic code:

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    max_depth=3,
    random_state=42
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
```

Meaning:

```text
Create forest
Train many trees
Predict class using voting
```

---

## Slide 15: Complete Demo — Imports

```python
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
```

We use:

- pandas for data
- train_test_split for data split
- RandomForestClassifier for model
- metrics for evaluation

---

## Slide 16: Complete Demo — Dataset

```python
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 1.5, 2.5, 3.5, 4.5],
    "attendance": [40, 50, 55, 65, 75, 85, 90, 95, 45, 52, 60, 70],
    "previous_marks": [25, 35, 45, 55, 65, 75, 85, 90, 30, 38, 48, 58],
    "result": ["Fail", "Fail", "Fail", "Pass", "Pass", "Pass",
               "Pass", "Pass", "Fail", "Fail", "Fail", "Pass"]
}

df = pd.DataFrame(data)
```

---

## Slide 17: Complete Demo — Features and Target

```python
X = df[["study_hours", "attendance", "previous_marks"]]
y = df["result"]
```

Here:

```text
X = input features
y = target class
```

The model learns:

```text
study_hours + attendance + previous_marks → Pass/Fail
```

---

## Slide 18: Complete Demo — Train-Test Split

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
75% data → training
25% data → testing
```

`stratify=y` keeps Pass/Fail ratio balanced.

---

## Slide 19: Complete Demo — Create and Train Model

```python
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=3,
    random_state=42
)

model.fit(X_train, y_train)
```

Meaning:

```text
Create 100 trees
Limit each tree depth to 3
Train the forest
```

Simple memory:

```text
fit = learn
```

---

## Slide 20: Complete Demo — Predict

```python
y_pred = model.predict(X_test)

print("Actual:", list(y_test))
print("Predicted:", list(y_pred))
```

Meaning:

```text
Use the trained forest to predict Pass/Fail for test students.
```

Then compare actual class and predicted class.

---

## Slide 21: Complete Demo — Evaluation

```python
print("Accuracy:", accuracy_score(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("Classification Report:")
print(classification_report(y_test, y_pred))
```

This helps us check how good the classifier is.

---

## Slide 22: Predict New Student — Pass Example

```python
new_student = pd.DataFrame({
    "study_hours": [5],
    "attendance": [82],
    "previous_marks": [72]
})

prediction = model.predict(new_student)

print("Prediction:", prediction[0])
```

Expected idea:

```text
Pass
```

---

## Slide 23: Predict New Student — Fail Example

```python
new_student = pd.DataFrame({
    "study_hours": [2],
    "attendance": [50],
    "previous_marks": [35]
})

prediction = model.predict(new_student)

print("Prediction:", prediction[0])
```

Expected idea:

```text
Fail
```

---

## Slide 24: Prediction Probability

Random Forest can give probabilities.

```python
probabilities = model.predict_proba(new_student)

print("Classes:", model.classes_)
print("Probabilities:", probabilities)
```

Example output:

```text
Classes: ['Fail', 'Pass']
Probabilities: [[0.85, 0.15]]
```

Meaning:

```text
Fail probability = 0.85
Pass probability = 0.15
```

---

## Slide 25: Feature Importance

Random Forest can show which features were more useful.

```python
importance = pd.DataFrame({
    "Feature": X.columns,
    "Importance": model.feature_importances_
})

print(importance)
```

Possible output:

| Feature | Importance |
|---|---:|
| previous_marks | 0.45 |
| attendance | 0.35 |
| study_hours | 0.20 |

---

## Slide 26: Why Feature Importance Is Useful

Feature importance helps answer:

```text
Which input columns influenced the model more?
```

For student result prediction:

```text
Did previous marks matter more?
Did attendance matter more?
Did study hours matter more?
```

For business:

```text
Which customer features affect churn?
Which transaction features affect fraud?
Which patient features affect risk?
```

---

## Slide 27: Strengths of Random Forest Classifier

Random Forest is useful because:

- Usually more accurate than one Decision Tree
- Reduces overfitting
- Works for binary and multi-class classification
- Handles non-linear patterns well
- Can show feature importance
- Does not usually require feature scaling
- Stable and practical

It is one of the most commonly used classical ML algorithms.

---

## Slide 28: Limitations of Random Forest Classifier

Random Forest also has limitations:

- Less explainable than a single Decision Tree
- Can be slower because it builds many trees
- Model file can be larger
- Not ideal when very simple explanation is required
- May still need tuning for best performance

So:

```text
Decision Tree = easier to explain
Random Forest = usually stronger performance
```

---

## Slide 29: When to Use Random Forest Classifier

Use Random Forest when:

- You want strong baseline performance
- You have tabular data
- You want to reduce overfitting
- You want feature importance
- You need binary or multi-class classification

Examples:

- Student pass/fail prediction
- Loan approval prediction
- Fraud detection
- Customer churn prediction
- Disease risk classification
- Ticket priority prediction

---

## Slide 30: Teaching Explanation

Use this in class:

```text
Decision Tree is like asking one expert.
Random Forest is like asking many experts and taking the majority opinion.
```

For classification:

```text
Each tree votes for a class.
The class with the highest votes becomes final prediction.
```

---

## Slide 31: Final Summary

Remember:

```text
Random Forest Classifier = many Decision Trees working together for classification.
```

It works like:

```text
Tree 1 → Pass
Tree 2 → Pass
Tree 3 → Fail
Tree 4 → Pass

Final prediction → Pass
```

---

## Slide 32: Memory Hook

```text
Decision Tree = one flowchart
Random Forest = many flowcharts voting
```

Simple explanation:

```text
Build many trees.
Collect their votes.
Choose the majority class.
```

Next topic:

# Data Preprocessing for Classification
