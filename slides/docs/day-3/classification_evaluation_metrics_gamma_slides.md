# Day 3: Supervised Learning — Classification
## Section 8: Classification Evaluation Metrics

## Slide 1: Section Opening

# Classification Evaluation Metrics

### Accuracy, Precision, Recall, and F1-score

In classification, the model predicts categories like:

- Pass / Fail
- Spam / Not Spam
- Fraud / Not Fraud
- Disease / No Disease

After prediction, we must ask:

> **How good is the classification model?**

That is where classification evaluation metrics help.

---

## Slide 2: Why Evaluation Metrics Are Needed

Suppose a model predicts student result.

| Student | Actual Result | Predicted Result |
|---|---|---|
| Student 1 | Pass | Pass |
| Student 2 | Fail | Pass |
| Student 3 | Pass | Pass |
| Student 4 | Fail | Fail |

Some predictions are correct.

Some predictions are wrong.

We need proper metrics to measure model performance.

---

## Slide 3: Common Classification Metrics

In this topic, we learn:

```text
Accuracy
Precision
Recall
F1-score
```

These are the most common beginner-friendly classification metrics.

We also understand the **confusion matrix**, because these metrics come from it.

---

## Slide 4: Confusion Matrix Idea

For binary classification, assume:

```text
Positive class = Pass
Negative class = Fail
```

The model can make four types of outcomes:

```text
True Positive
True Negative
False Positive
False Negative
```

These four outcomes form the confusion matrix.

---

## Slide 5: True Positive

True Positive means:

> **Actual is Positive, and model also predicted Positive.**

Example:

```text
Actual = Pass
Predicted = Pass
```

This is correct.

Short form:

```text
TP
```

---

## Slide 6: True Negative

True Negative means:

> **Actual is Negative, and model also predicted Negative.**

Example:

```text
Actual = Fail
Predicted = Fail
```

This is correct.

Short form:

```text
TN
```

---

## Slide 7: False Positive

False Positive means:

> **Actual is Negative, but model predicted Positive.**

Example:

```text
Actual = Fail
Predicted = Pass
```

This is wrong.

Short form:

```text
FP
```

Student meaning:

```text
Model says student will pass, but actually student fails.
```

---

## Slide 8: False Negative

False Negative means:

> **Actual is Positive, but model predicted Negative.**

Example:

```text
Actual = Pass
Predicted = Fail
```

This is wrong.

Short form:

```text
FN
```

Student meaning:

```text
Model says student will fail, but actually student passes.
```

---

## Slide 9: Confusion Matrix Table

For Pass/Fail:

```text
                 Predicted Fail   Predicted Pass
Actual Fail           TN               FP
Actual Pass           FN               TP
```

Example:

|  | Predicted Fail | Predicted Pass |
|---|---:|---:|
| Actual Fail | 8 | 2 |
| Actual Pass | 1 | 9 |

Here:

```text
TN = 8
FP = 2
FN = 1
TP = 9
```

---

## Slide 10: Accuracy

Accuracy means:

> **Out of all predictions, how many were correct?**

Formula:

```text
Accuracy = (TP + TN) / (TP + TN + FP + FN)
```

Using our example:

```text
TP = 9
TN = 8
FP = 2
FN = 1
```

Accuracy:

```text
Accuracy = (9 + 8) / (9 + 8 + 2 + 1)
Accuracy = 17 / 20
Accuracy = 0.85
```

So:

```text
Accuracy = 85%
```

---

## Slide 11: Accuracy Interpretation

If:

```text
Accuracy = 85%
```

It means:

```text
The model correctly predicted 85 out of 100 cases.
```

Accuracy is easy to understand.

But remember:

```text
Accuracy can be misleading when classes are imbalanced.
```

---

## Slide 12: Accuracy Trap

Example:

```text
95 Pass students
5 Fail students
Model predicts everyone as Pass
```

Accuracy:

```text
95%
```

But the model finds:

```text
0 Fail students
```

So accuracy alone is not enough.

---

## Slide 13: Precision

Precision answers:

> **Out of all predicted positive cases, how many were actually positive?**

Formula:

```text
Precision = TP / (TP + FP)
```

In student example:

```text
Out of all students predicted as Pass, how many actually passed?
```

---

## Slide 14: Precision Calculation

Using values:

```text
TP = 9
FP = 2
```

Precision:

```text
Precision = 9 / (9 + 2)
Precision = 9 / 11
Precision = 0.82
```

So:

```text
Precision = 82%
```

---

## Slide 15: Precision Interpretation

If precision is high:

```text
When model predicts Pass, it is usually correct.
```

Low precision means:

```text
Model is predicting too many false positives.
```

Example:

```text
Model says many students will pass, but many actually fail.
```

---

## Slide 16: Where Precision Matters

Business examples where precision matters:

```text
Fraud alert: avoid too many false alarms
Loan approval: avoid approving risky customers
Medical alert: avoid unnecessary panic
Email spam: avoid marking good emails as spam
```

Precision is about the **quality of positive predictions**.

---

## Slide 17: Recall

Recall answers:

> **Out of all actual positive cases, how many did the model correctly find?**

Formula:

```text
Recall = TP / (TP + FN)
```

In student example:

```text
Out of all actual Pass students, how many did model find as Pass?
```

---

## Slide 18: Recall Calculation

Using values:

```text
TP = 9
FN = 1
```

Recall:

```text
Recall = 9 / (9 + 1)
Recall = 9 / 10
Recall = 0.90
```

So:

```text
Recall = 90%
```

---

## Slide 19: Recall Interpretation

If recall is high:

```text
The model is good at finding actual positive cases.
```

Low recall means:

```text
The model is missing many actual positive cases.
```

Recall is about **coverage of actual positives**.

---

## Slide 20: Where Recall Matters

Examples where recall matters:

```text
Disease detection: do not miss sick patients
Fraud detection: do not miss fraud cases
Student risk detection: do not miss failing students
Cybersecurity: do not miss attacks
```

In high-risk domains, recall is often very important.

---

## Slide 21: Precision vs Recall

Precision and recall answer different questions.

## Precision

```text
When model says Positive, is it correct?
```

## Recall

```text
Out of all actual Positives, how many did model find?
```

Simple memory:

```text
Precision = quality of positive predictions
Recall = coverage of actual positive cases
```

---

## Slide 22: Hospital Example

Suppose model predicts disease.

## High Precision

```text
When model says Disease, it is usually correct.
```

This avoids false alarms.

## High Recall

```text
The model finds most actual disease patients.
```

This avoids missing sick patients.

In healthcare, recall is often very important.

---

## Slide 23: F1-score

F1-score balances precision and recall.

Simple meaning:

> **F1-score gives one score that balances both precision and recall.**

Formula:

```text
F1 = 2 × (Precision × Recall) / (Precision + Recall)
```

If either precision or recall is very low, F1-score becomes low.

---

## Slide 24: F1-score Example

Suppose:

```text
Precision = 0.82
Recall = 0.90
```

F1:

```text
F1 = 2 × (0.82 × 0.90) / (0.82 + 0.90)
F1 ≈ 0.86
```

So:

```text
F1-score = 86%
```

---

## Slide 25: When to Use F1-score

Use F1-score when:

```text
Data is imbalanced
You care about both precision and recall
Accuracy is not enough
False positives and false negatives both matter
```

Example:

In fraud detection:

```text
Precision: fraud alerts should be meaningful
Recall: fraud cases should not be missed
F1: balance between both
```

---

## Slide 26: Metric Direction

| Metric | Meaning | Better Direction |
|---|---|---|
| Accuracy | Overall correct predictions | Higher is better |
| Precision | Correctness of positive predictions | Higher is better |
| Recall | Finding actual positives | Higher is better |
| F1-score | Balance of precision and recall | Higher is better |

For all these metrics:

```text
Higher is usually better.
```

---

## Slide 27: Python Metrics Example

```python
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score

actual = ["Pass", "Fail", "Pass", "Fail", "Pass", "Pass"]
predicted = ["Pass", "Pass", "Pass", "Fail", "Fail", "Pass"]

accuracy = accuracy_score(actual, predicted)

precision = precision_score(actual, predicted, pos_label="Pass")
recall = recall_score(actual, predicted, pos_label="Pass")
f1 = f1_score(actual, predicted, pos_label="Pass")

print("Accuracy :", accuracy)
print("Precision:", precision)
print("Recall   :", recall)
print("F1-score :", f1)
```

---

## Slide 28: Classification Report

Scikit-learn gives a very useful report:

```python
from sklearn.metrics import classification_report

print(classification_report(actual, predicted))
```

It shows:

```text
precision
recall
f1-score
support
```

for each class.

Support means:

```text
How many actual records belong to that class.
```

---

## Slide 29: Complete Model Evaluation — Imports

```python
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)
```

---

## Slide 30: Complete Model Evaluation — Dataset

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

## Slide 31: Complete Model Evaluation — Train

```python
X = df[["study_hours", "attendance", "previous_marks"]]
y = df["result"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

---

## Slide 32: Complete Model Evaluation — Metrics

```python
print("Accuracy :", accuracy_score(y_test, y_pred))
print("Precision:", precision_score(y_test, y_pred, pos_label="Pass"))
print("Recall   :", recall_score(y_test, y_pred, pos_label="Pass"))
print("F1-score :", f1_score(y_test, y_pred, pos_label="Pass"))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("Classification Report:")
print(classification_report(y_test, y_pred))
```

---

## Slide 33: Multi-class Classification Metrics

For multi-class classification, use `average`:

```python
precision_score(y_test, y_pred, average="macro")
recall_score(y_test, y_pred, average="macro")
f1_score(y_test, y_pred, average="macro")
```

Common average options:

```text
macro = treat all classes equally
weighted = consider class size/support
```

For beginners:

```text
Use classification_report()
```

It is easier to understand.

---

## Slide 34: Trainer Explanation

Use this in class:

```text
Accuracy tells overall correctness.
Precision tells how trustworthy positive predictions are.
Recall tells how many actual positives were found.
F1-score balances precision and recall.
```

For imbalanced data:

```text
Do not depend only on accuracy.
Check precision, recall, F1-score, and confusion matrix.
```

---

## Slide 35: Final Summary

Remember:

```text
Accuracy = overall correctness
Precision = correctness of positive predictions
Recall = ability to find positives
F1-score = balance between precision and recall
```

---

## Slide 36: Memory Hook

```text
Accuracy = How many total correct?
Precision = When model says yes, is it right?
Recall = Did model find all actual yes cases?
F1 = Balance between precision and recall
```

Next topic:

# Hands-on Classification Model Building Using Scikit-learn
