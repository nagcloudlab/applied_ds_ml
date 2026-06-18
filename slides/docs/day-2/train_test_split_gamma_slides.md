# Train-Test Split Concept

## Why This Topic Matters

Before building any machine learning model, we must answer one important question:

**Has the model really learned, or has it only memorized?**

Train-test split helps us check that.

---

# Simple Meaning

Train-test split means we divide our data into two parts:

- **Training data** — used to teach the model
- **Testing data** — used to check the model

Common split:

- **80%** training data
- **20%** testing data

Main idea:

**Do not test the model on the same data it learned from.**

---

# Student Analogy

Imagine a student preparing for an exam.

The teacher gives 100 questions.

If the student studies all 100 questions and the exam also has the same 100 questions, the student may score well by memory.

That does not prove real understanding.

Better approach:

- **80 questions** for practice
- **20 new questions** for exam

Machine Learning works the same way.

---

# ML Analogy

In machine learning:

- **Training data** = practice questions
- **Testing data** = exam questions

The model learns from training data.

Then we check it using testing data.

If it performs well on testing data, we gain confidence that it can handle new data.

---

# House Price Example

Suppose we have house data:

| Area | Bedrooms | Age | Distance | Price |
|---:|---:|---:|---:|---:|
| 1000 | 2 | 5 | 8 | 55 |
| 1500 | 3 | 3 | 5 | 82 |
| 2000 | 4 | 2 | 4 | 120 |
| 900 | 2 | 10 | 12 | 42 |
| 1800 | 3 | 4 | 6 | 95 |
| 2200 | 4 | 2 | 3 | 130 |
| 1300 | 2 | 6 | 9 | 65 |
| 2500 | 4 | 1 | 2 | 155 |
| 1600 | 3 | 5 | 7 | 78 |
| 2800 | 5 | 1 | 2 | 175 |

Goal:

**Predict house price.**

---

# How We Split the Data

From 10 rows:

- **8 rows** for training
- **2 rows** for testing

The model learns from the 8 training rows.

Then we hide the prices of the 2 testing rows and ask:

**Can you predict the price?**

After prediction, we compare:

**Actual price vs Predicted price**

---

# Main Goal

The goal of train-test split is to check:

**Can the model perform well on new, unseen data?**

In real life, we do not build ML models only for old data.

We build models for new situations:

- New house price
- New student result
- New customer churn
- New sales forecast
- New loan approval

---

# What Happens Without Train-Test Split?

If we train on all data and test on the same data, the result may look very good.

But it may be misleading.

Why?

Because the model already saw the answers.

This is like a student getting the same question paper before the exam.

The score may be high, but understanding may be low.

---

# Overfitting

Overfitting means:

**The model memorizes training data too much and performs poorly on new data.**

Example:

A student memorizes:

- 2 + 2 = 4
- 3 + 3 = 6
- 4 + 4 = 8

But when asked:

**5 + 5 = ?**

The student gets confused.

The student memorized examples but did not understand the concept.

---

# Underfitting

Underfitting means:

**The model has not learned enough even from the training data.**

Student analogy:

The student did not study properly.

So:

- Practice test score is poor
- Final exam score is also poor

In ML:

- Training performance is poor
- Testing performance is poor

---

# Good Model Behavior

A good model should perform reasonably well on both:

- Training data
- Testing data

Good behavior:

**Training performance is good**

**Testing performance is also good**

That means the model learned the pattern instead of only memorizing examples.

---

# Train-Test Split in Python

We use `train_test_split` from scikit-learn.

```python
from sklearn.model_selection import train_test_split
```

First, separate features and target:

```python
X = df[["area", "bedrooms", "age", "distance"]]
y = df["price"]
```

Then split:

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

---

# What These Variables Mean

After splitting, we get four parts:

| Variable | Meaning |
|---|---|
| `X_train` | Input features for training |
| `X_test` | Input features for testing |
| `y_train` | Correct answers for training |
| `y_test` | Correct answers for testing |

Simple view:

```text
Training: X_train + y_train
Testing: X_test + y_test
```

---

# Model Flow

Training step:

```python
model.fit(X_train, y_train)
```

Prediction step:

```python
y_pred = model.predict(X_test)
```

Evaluation step:

```text
Compare y_test with y_pred
```

Meaning:

- `y_test` = actual answers
- `y_pred` = model predictions

---

# Meaning of test_size

```python
test_size=0.2
```

means:

- **20%** data is used for testing
- **80%** data is used for training

Example:

If total rows = 1000:

- Training rows = 800
- Testing rows = 200

---

# Meaning of random_state

```python
random_state=42
```

means:

**Fix the randomness so we get the same split every time.**

Without `random_state`, every run may create a different split.

For teaching and learning, we use `random_state` so results are repeatable.

---

# Full Python Example

```python
import pandas as pd
from sklearn.model_selection import train_test_split

data = {
    "area": [1000, 1500, 2000, 900, 1800, 2200, 1300, 2500, 1600, 2800],
    "bedrooms": [2, 3, 4, 2, 3, 4, 2, 4, 3, 5],
    "age": [5, 3, 2, 10, 4, 2, 6, 1, 5, 1],
    "distance": [8, 5, 4, 12, 6, 3, 9, 2, 7, 2],
    "price": [55, 82, 120, 42, 95, 130, 65, 155, 78, 175]
}

df = pd.DataFrame(data)

X = df[["area", "bedrooms", "age", "distance"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Total rows:", len(df))
print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))
```

---

# Expected Output Idea

```text
Total rows: 10
Training rows: 8
Testing rows: 2
```

Meaning:

The full dataset has 10 records.

The model learns from 8 records.

The model is tested on 2 unseen records.

---

# Visual Understanding

Before split:

```text
Full Data
━━━━━━━━━━━━━━━━━━━━
100%
```

After split:

```text
Training Data                    Testing Data
━━━━━━━━━━━━━━━━        ━━━━
80%                     20%
```

The model sees only the training data while learning.

Testing data is kept aside.

---

# Important Mistake to Avoid

Wrong approach:

```python
model.fit(X, y)
y_pred = model.predict(X)
```

Why wrong?

The model is tested on the same data it already saw.

Correct approach:

```python
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

Golden rule:

**Train on training data. Test on testing data.**

---

# Real-Life Banking Example

A bank wants to build a loan approval model.

Past data includes:

- Customer income
- Credit score
- Loan amount
- Employment status
- Previous default history
- Loan approved or rejected

We split the data:

- Training data: old records used for learning
- Testing data: hidden old records used for checking

If testing performance is good, the bank can use the model for new customers.

---

# Train-Test Split and Future Prediction

The complete flow:

```text
Past data
    ↓
Split into train and test
    ↓
Train model using training data
    ↓
Evaluate model using testing data
    ↓
Use model on new real data
```

Example:

A new customer applies for a loan.

The trained model predicts:

**Approved or Rejected**

---

# Final Summary

Train-test split checks whether the model can work on unseen data.

Core idea:

```text
Full data
    ↓
Split into train and test
    ↓
Train model using training data
    ↓
Predict using testing data
    ↓
Compare prediction with actual answer
```

---

# Golden Rule

**Training data is for learning.**

**Testing data is for checking.**

Never test the model only on the same data it learned from.

That can create fake confidence.

---

# Quick Quiz

A company has 10,000 old customer records.

They use 8,000 records to train the model and 2,000 records to check the model.

What is this called?

**Answer:** Train-test split

Why?

Because the data is divided into training data and testing data.
