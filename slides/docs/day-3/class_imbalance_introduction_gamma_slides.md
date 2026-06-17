# Day 3: Supervised Learning — Classification
## Section 7: Class Imbalance Introduction

## Slide 1: Section Opening

# Class Imbalance Introduction

### When one class dominates the dataset

In classification, we predict categories like:

- Pass / Fail
- Spam / Not Spam
- Fraud / Not Fraud
- Disease / No Disease

But sometimes, one class has many records and another class has very few records.

That problem is called **class imbalance**.

---

## Slide 2: What Is Class Imbalance?

Class imbalance means:

> **The target classes are not equally represented in the dataset.**

Example:

| Result | Count |
|---|---:|
| Pass | 95 |
| Fail | 5 |

Here:

```text
Pass = 95 students
Fail = 5 students
```

The data is highly imbalanced.

---

## Slide 3: Why Class Imbalance Is Dangerous

The model may mostly learn the majority class:

```text
Pass
```

and ignore the minority class:

```text
Fail
```

This is dangerous because the minority class is often the important class.

Examples:

```text
Fraud
Disease
Fail
Churn
Defect
Cyber attack
```

---

## Slide 4: Simple Student Example

Suppose we have 100 students.

```text
95 students passed
5 students failed
```

If a model predicts **Pass for every student**, then:

```text
Correct predictions = 95
Total students = 100
Accuracy = 95%
```

This looks excellent.

But actually, the model is useless for finding failed students.

---

## Slide 5: Why Accuracy Can Mislead Us

If the model always predicts:

```text
Pass
```

then it never predicts:

```text
Fail
```

So even with 95% accuracy, the model found:

```text
0 failed students
```

This is the danger of class imbalance.

High accuracy does not always mean a good model.

---

## Slide 6: Accuracy Problem Example

| Actual | Prediction |
|---|---|
| Pass | Pass |
| Pass | Pass |
| Pass | Pass |
| Pass | Pass |
| Fail | Pass |

Accuracy:

```text
4 correct out of 5 = 80%
```

But for the Fail class:

```text
Model found 0 failed students
```

So accuracy alone is not enough.

---

## Slide 7: Real-Life Example — Fraud Detection

Fraud detection is usually imbalanced.

Example:

| Transaction Type | Count |
|---|---:|
| Not Fraud | 99,000 |
| Fraud | 1,000 |

Most transactions are normal.

Only a small number are fraud.

---

## Slide 8: Fraud Accuracy Trap

If a model predicts every transaction as:

```text
Not Fraud
```

Accuracy is:

```text
99,000 / 100,000 = 99%
```

Looks amazing.

But it catches:

```text
0 fraud cases
```

That is a terrible fraud detection model.

---

## Slide 9: Real-Life Example — Disease Detection

Disease detection can also be imbalanced.

Example:

| Class | Count |
|---|---:|
| No Disease | 950 |
| Disease | 50 |

If the model predicts everyone as:

```text
No Disease
```

Accuracy is:

```text
950 / 1000 = 95%
```

But it misses all disease patients.

---

## Slide 10: Healthcare Risk

In healthcare, missing positive disease cases can be very serious.

Example:

```text
Actual Disease → Predicted No Disease
```

This is dangerous because the patient may not receive treatment.

So we must check minority class performance carefully.

---

## Slide 11: Majority Class and Minority Class

In imbalanced classification:

```text
Majority class = class with more records
Minority class = class with fewer records
```

Example:

| Class | Count |
|---|---:|
| Not Fraud | 99,000 |
| Fraud | 1,000 |

Here:

```text
Majority class = Not Fraud
Minority class = Fraud
```

---

## Slide 12: Why Minority Class Matters

Usually, the minority class is the more important class.

Examples:

| Domain | Majority Class | Minority Class |
|---|---|---|
| Banking | Not Fraud | Fraud |
| Healthcare | No Disease | Disease |
| Education | Pass | Fail |
| Manufacturing | Good Product | Defective Product |
| Cybersecurity | Normal Activity | Attack |
| Telecom | Customer Stays | Customer Churns |

---

## Slide 13: How to Check Class Imbalance

In Python, check target distribution:

```python
print(df["result"].value_counts())
```

Example output:

```text
Pass    95
Fail     5
Name: result, dtype: int64
```

This shows how many records each class has.

---

## Slide 14: Check Class Percentage

To see percentages:

```python
print(df["result"].value_counts(normalize=True) * 100)
```

Example output:

```text
Pass    95.0
Fail     5.0
Name: result, dtype: float64
```

This tells us whether the dataset is balanced or imbalanced.

---

## Slide 15: Balanced Dataset

Balanced dataset:

| Class | Count |
|---|---:|
| Pass | 50 |
| Fail | 50 |

This is balanced because both classes are equally represented.

A model gets enough examples of both classes.

---

## Slide 16: Slightly Imbalanced Dataset

Slightly imbalanced dataset:

| Class | Count |
|---|---:|
| Pass | 65 |
| Fail | 35 |

This may still be manageable.

But we should still check metrics carefully.

---

## Slide 17: Highly Imbalanced Dataset

Highly imbalanced dataset:

| Class | Count |
|---|---:|
| Pass | 95 |
| Fail | 5 |

This needs special attention.

The model may ignore the minority class.

---

## Slide 18: What Happens If We Ignore Class Imbalance?

If we ignore class imbalance, the model may:

- Predict majority class most of the time
- Show high accuracy
- Perform badly on minority class
- Miss important rare cases
- Give false confidence

Example:

```text
A fraud model with 99% accuracy may still be useless if it catches no fraud.
```

---

## Slide 19: Better Metrics for Imbalanced Data

For imbalanced classification, use:

```text
Precision
Recall
F1-score
Confusion matrix
ROC-AUC
PR-AUC
```

In this ToC, we focus on:

```text
Accuracy
Precision
Recall
F1-score
```

Important:

```text
Accuracy alone is not enough for imbalanced data.
```

---

## Slide 20: Recall for Minority Class

Recall answers:

> **Out of all actual positive cases, how many did the model find?**

Example: fraud detection

```text
Actual fraud cases = 100
Model detected fraud = 80
Recall = 80 / 100 = 80%
```

If recall is low, the model is missing important cases.

---

## Slide 21: Precision for Minority Class

Precision answers:

> **Out of all predicted positive cases, how many were actually positive?**

Example: fraud detection

```text
Model predicted 100 transactions as fraud
Actually fraud = 70
Precision = 70 / 100 = 70%
```

If precision is low, the model raises too many false alarms.

---

## Slide 22: Why F1-Score Helps

F1-score gives a balance between precision and recall.

Use F1-score when:

- You care about both false positives and false negatives
- Data is imbalanced
- Accuracy is misleading

Example:

```text
Precision = How many fraud alerts were correct?
Recall = How many actual fraud cases were found?
F1-score = Balance between both
```

---

## Slide 23: Ways to Handle Class Imbalance

Common techniques:

```text
1. Use better metrics
2. Use stratified train-test split
3. Use class_weight
4. Oversample minority class
5. Undersample majority class
6. Collect more minority class data
```

We will keep this beginner-friendly.

---

## Slide 24: Technique 1 — Use stratify

When splitting classification data, use:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)
```

`stratify=y` keeps class proportions similar in train and test data.

---

## Slide 25: Why stratify Helps

If full data has:

```text
90% Pass
10% Fail
```

then train and test also keep a similar ratio.

Without stratify, the test set may accidentally contain too few minority samples.

That can make evaluation unreliable.

---

## Slide 26: Technique 2 — Use class_weight

Some models support:

```python
class_weight="balanced"
```

Example:

```python
from sklearn.ensemble import RandomForestClassifier

model = RandomForestClassifier(
    n_estimators=100,
    class_weight="balanced",
    random_state=42
)
```

This tells the model:

```text
Give more importance to minority class.
```

---

## Slide 27: Technique 3 — Oversampling

Oversampling means:

> **Increase minority class records.**

Before:

| Class | Count |
|---|---:|
| Pass | 95 |
| Fail | 5 |

After oversampling:

| Class | Count |
|---|---:|
| Pass | 95 |
| Fail | 95 |

Simple beginner idea:

```text
Make minority class more visible to the model.
```

---

## Slide 28: Technique 4 — Undersampling

Undersampling means:

> **Reduce majority class records.**

Before:

| Class | Count |
|---|---:|
| Pass | 95 |
| Fail | 5 |

After undersampling:

| Class | Count |
|---|---:|
| Pass | 5 |
| Fail | 5 |

Problem:

```text
We may lose useful majority-class data.
```

Use carefully.

---

## Slide 29: Technique 5 — Collect More Data

The best solution is often:

```text
Collect more minority class data.
```

Examples:

- More fraud examples
- More disease examples
- More failed student cases
- More defective product records

Better data usually improves model quality more than complex tricks.

---

## Slide 30: Complete Small Example

```python
import pandas as pd

data = {
    "study_hours": [6, 7, 8, 5, 6, 7, 8, 6, 7, 2],
    "attendance": [80, 85, 90, 75, 82, 88, 95, 84, 90, 40],
    "previous_marks": [70, 75, 85, 65, 72, 80, 90, 78, 88, 30],
    "result": ["Pass", "Pass", "Pass", "Pass", "Pass",
               "Pass", "Pass", "Pass", "Pass", "Fail"]
}

df = pd.DataFrame(data)

print(df["result"].value_counts())
print(df["result"].value_counts(normalize=True) * 100)
```

---

## Slide 31: Training with class_weight

```python
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report

X = df[["study_hours", "attendance", "previous_marks"]]
y = df["result"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42,
    stratify=y
)

model = RandomForestClassifier(
    n_estimators=100,
    class_weight="balanced",
    random_state=42
)

model.fit(X_train, y_train)
y_pred = model.predict(X_test)

print(classification_report(y_test, y_pred, zero_division=0))
```

---

## Slide 32: Trainer Explanation

Use this explanation:

```text
In imbalanced data, the model may become lazy.
It may keep predicting the majority class because that gives high accuracy.
But real business value often depends on finding the minority class.
```

Examples:

```text
Fraud cases are rare, but important.
Disease cases may be rare, but critical.
Failing students may be fewer, but we must identify them early.
```

---

## Slide 33: Final Summary

Remember:

```text
Class imbalance = one class has many records, another class has very few.
```

Danger:

```text
Accuracy may look high but model may ignore minority class.
```

Important tools:

```text
Check value_counts()
Use stratify=y
Look at precision, recall, F1-score
Try class_weight="balanced"
Consider oversampling or undersampling
Collect more minority data
```

---

## Slide 34: Memory Hook

```text
High accuracy is not always a good model.
Check minority class performance.
```

Simple warning:

```text
If minority class is important, accuracy alone can fool you.
```

Next topic:

# Classification Evaluation: Accuracy, Precision, Recall, and F1-score
