# Day 3: Supervised Learning — Classification
## Section 1: Introduction to Classification Problems

## Slide 1: Section Opening

# Introduction to Classification Problems

### Predicting categories instead of numbers

Until now:

```text
Regression = Predict a number
Example: House price = ₹90 lakh
```

Now:

```text
Classification = Predict a category/class
Example: Email = Spam or Not Spam
```

---

## Slide 2: What Is Classification?

Classification is a type of **Supervised Machine Learning**.

Simple meaning:

> **Classification means predicting a category or class.**

The output is not a number like price or salary.

The output is a label/category.

Examples:

- Pass or Fail
- Spam or Not Spam
- Disease or No Disease
- Loan Approved or Rejected
- Customer Will Buy or Not Buy
- Fraud or Not Fraud

---

## Slide 3: Regression vs Classification

# Regression

Regression predicts a number.

Examples:

```text
Predict house price = ₹90 lakh
Predict salary = ₹8 LPA
Predict marks = 85
Predict temperature = 32.5°C
```

Question type:

```text
How much?
How many?
```

---

## Slide 4: Classification Thinking

# Classification

Classification predicts a category.

Examples:

```text
Predict email type = Spam
Predict student result = Pass
Predict disease status = Disease
Predict loan status = Approved
```

Question type:

```text
Which class?
Which category?
Yes or No?
```

---

## Slide 5: Easy Difference

| Problem | Output | Type |
|---|---|---|
| Predict house price | ₹90 lakh | Regression |
| Predict student marks | 85 | Regression |
| Predict pass/fail | Pass | Classification |
| Predict spam/not spam | Spam | Classification |
| Predict disease/no disease | Disease | Classification |
| Predict salary | ₹8 LPA | Regression |

Simple memory:

```text
Regression = Predict number
Classification = Predict category
```

---

## Slide 6: Running Example

For this module, we use a simple example:

> **Predict whether a student will Pass or Fail.**

Dataset:

| Study Hours | Attendance | Previous Marks | Result |
|---:|---:|---:|---|
| 2 | 60 | 40 | Fail |
| 5 | 85 | 70 | Pass |
| 6 | 90 | 80 | Pass |
| 1 | 45 | 25 | Fail |
| 4 | 75 | 60 | Pass |
| 3 | 55 | 45 | Fail |

---

## Slide 7: Features and Target

For student result prediction:

```text
Features:
Study Hours
Attendance
Previous Marks

Target:
Result
```

Target values:

```text
Pass
Fail
```

Because the target is a category, this is a **classification problem**.

---

## Slide 8: Classification Is Supervised Learning

Supervised learning means:

```text
Data has correct answers.
```

In our student example:

| Study Hours | Attendance | Previous Marks | Result |
|---:|---:|---:|---|
| 2 | 60 | 40 | Fail |
| 5 | 85 | 70 | Pass |

The correct answer is already available:

```text
Result = Pass or Fail
```

So this is supervised learning.

---

## Slide 9: What the Model Learns

The model learns from examples:

```text
Study Hours + Attendance + Previous Marks → Result
```

It may learn patterns like:

```text
Low study hours + low attendance + low previous marks → Fail
High study hours + high attendance + high previous marks → Pass
```

Then it predicts the result for a new student.

---

## Slide 10: New Student Prediction Example 1

New student:

```text
Study Hours = 4
Attendance = 80
Previous Marks = 65
```

The model may predict:

```text
Pass
```

Why?

Because the pattern looks closer to students who passed.

---

## Slide 11: New Student Prediction Example 2

Another student:

```text
Study Hours = 1
Attendance = 50
Previous Marks = 30
```

The model may predict:

```text
Fail
```

Why?

Because the pattern looks closer to students who failed.

---

## Slide 12: Real-Life Example 1 — Email Spam Detection

Features:

- Email words
- Sender
- Number of links
- Attachments
- Subject line

Target:

```text
Spam or Not Spam
```

This is classification because output is a category.

---

## Slide 13: Real-Life Example 2 — Loan Approval

Features:

- Income
- Credit score
- Loan amount
- Employment type
- Previous default history

Target:

```text
Approved or Rejected
```

This is classification.

The model predicts which class the customer belongs to.

---

## Slide 14: Real-Life Example 3 — Disease Prediction

Features:

- Age
- Blood pressure
- Sugar level
- Symptoms
- Medical history

Target:

```text
Disease or No Disease
```

This is classification.

The model predicts a health category.

---

## Slide 15: Real-Life Example 4 — Customer Churn

Features:

- Subscription months
- Usage frequency
- Complaint count
- Payment history
- Plan type

Target:

```text
Will Churn or Will Not Churn
```

This is classification.

The model predicts whether a customer may leave.

---

## Slide 16: Classification Output Can Be Text

Class labels may be text:

```text
Pass / Fail
Spam / Not Spam
Yes / No
Approved / Rejected
Disease / No Disease
```

These are categories.

The model does not predict a quantity.

It predicts a class label.

---

## Slide 17: Classification Output Can Be Number Codes

Sometimes class labels are written as numbers:

```text
0 = Fail
1 = Pass
```

Example:

| Study Hours | Attendance | Previous Marks | Result |
|---:|---:|---:|---:|
| 2 | 60 | 40 | 0 |
| 5 | 85 | 70 | 1 |

Even though target is written as 0 and 1, it is still classification.

Why?

Because 0 and 1 are class labels, not measurable quantities.

---

## Slide 18: Important Confusion

# If output is number, is it always regression?

No.

Example:

```text
0 = Not Spam
1 = Spam
```

This is classification.

Because 0 and 1 represent categories.

Simple rule:

```text
If number is measurable quantity → Regression
If number is category code → Classification
```

---

## Slide 19: Target Meaning Table

| Target | Meaning | Type |
|---|---|---|
| Price = 90 | Measurable amount | Regression |
| Marks = 85 | Measurable score | Regression |
| Spam = 1 | Category code | Classification |
| Disease = 0 | Category code | Classification |
| Risk Level = 3 | Category code | Classification |

---

## Slide 20: Classification Model Goal

A classification model tries to learn boundaries between classes.

For student result:

```text
Pass students are in one group.
Fail students are in another group.
```

The model tries to learn:

```text
What kind of students usually pass?
What kind of students usually fail?
```

---

## Slide 21: Pattern Thinking

Example pattern:

```text
If study hours are high and attendance is high → likely Pass
If study hours are low and attendance is low → likely Fail
```

Classification is about learning such class patterns.

Then the model assigns a new record to the most likely class.

---

## Slide 22: Classification Prediction Can Include Probability

Many classification models can give probability also.

Example:

```text
Pass probability = 0.85
Fail probability = 0.15
```

Final prediction:

```text
Pass
```

Probability gives confidence.

---

## Slide 23: Spam Probability Example

Example:

```text
Spam probability = 0.92
Not spam probability = 0.08
```

Final prediction:

```text
Spam
```

This is useful because the model can show how confident it is.

---

## Slide 24: Classification in Python Thinking

For our student example:

```python
X = df[["study_hours", "attendance", "previous_marks"]]
y = df["result"]
```

Here:

```text
X = input features
y = target class
```

Then we train a classifier:

```python
model.fit(X_train, y_train)
```

Then we predict:

```python
y_pred = model.predict(X_test)
```

---

## Slide 25: Regression Code vs Classification Code

The flow looks similar:

```text
Prepare X and y
Split train/test
Fit model
Predict
Evaluate
```

Difference:

```text
Regression model predicts a number.
Classification model predicts a class.
```

So the workflow is similar, but the output type is different.

---

## Slide 26: Common Classification Algorithms

In this module, we will learn:

- Naive Bayes
- Decision Tree Classifier
- Random Forest Classifier

Other common classification algorithms:

- Logistic Regression
- K-Nearest Neighbors
- Support Vector Machine
- Gradient Boosting
- XGBoost
- Neural Networks

---

## Slide 27: Business Use Cases

Classification is widely used in real projects.

Examples:

```text
Banking:
Loan approved or rejected
Fraud or not fraud

Healthcare:
Disease or no disease
High risk or low risk

Education:
Pass or fail
Dropout risk or no dropout risk

Retail:
Customer will buy or not buy
Customer will churn or stay

Cybersecurity:
Attack or normal activity

HR:
Candidate shortlisted or rejected
```

---

## Slide 28: Final Summary

Remember this clearly:

```text
Classification means predicting a category.
```

Examples:

```text
Pass/Fail
Spam/Not Spam
Approved/Rejected
Disease/No Disease
Fraud/Not Fraud
```

Classification belongs to:

```text
Supervised Learning
```

because training data has correct answers.

---

## Slide 29: Memory Hook

```text
Regression = How much?
Classification = Which class?
```

For our example:

```text
Study Hours + Attendance + Previous Marks → Pass or Fail
```

That is a classification problem.

---

## Slide 30: Small Quiz

Identify whether each is regression or classification:

```text
1. Predict house price
2. Predict whether customer will buy
3. Predict student final marks
4. Predict email spam or not spam
5. Predict delivery time
```

Answers:

```text
1. Regression
2. Classification
3. Regression
4. Classification
5. Regression
```

Next topic:

# Binary Classification vs Multi-class Classification
