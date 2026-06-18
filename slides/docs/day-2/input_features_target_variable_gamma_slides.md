# Input Features and Target Variable

## Beginner-Friendly Deep Dive

Learning the most important foundation before building any Machine Learning model.

---

# Big Idea

Before building a Machine Learning model, we must clearly understand:

```text
What is input?
What is output?
What should the machine learn?
```

In ML language:

```text
Input = Features
Output = Target Variable
```

---

# Simple Meaning

Suppose we ask:

**Based on study hours, attendance, and previous marks, can we predict final marks?**

Inputs:

- Study hours
- Attendance
- Previous marks

Output:

- Final marks

In ML:

```text
Inputs are called features.
Output is called target variable.
```

---

# House Price Example

| Area | Bedrooms | House Age | Distance from City | Price |
|---:|---:|---:|---:|---:|
| 1000 sqft | 2 | 5 years | 8 km | ₹55 lakh |
| 1500 sqft | 3 | 3 years | 5 km | ₹82 lakh |
| 2000 sqft | 4 | 2 years | 4 km | ₹120 lakh |
| 900 sqft | 2 | 10 years | 12 km | ₹42 lakh |

Goal:

**Predict house price.**

The model should learn:

```text
Area + Bedrooms + House Age + Distance → Price
```

---

# Column Roles

| Column | Role |
|---|---|
| Area | Feature |
| Bedrooms | Feature |
| House Age | Feature |
| Distance from City | Feature |
| Price | Target Variable |

The features are the inputs.

The target variable is the answer we want to predict.

---

# What Is a Feature?

A feature is an input column used to make prediction.

Simple definition:

**A feature is useful information given to the model.**

For house price prediction, useful features may be:

- Area
- Number of bedrooms
- Number of bathrooms
- House age
- Distance from city
- Parking availability
- Nearby metro

---

# Features Are Clues

Think like this:

```text
Features = Clues
Target = Answer
```

Example:

```text
Clues:
Area = 1500 sqft
Bedrooms = 3
Age = 3 years
Distance = 5 km

Answer:
Price = ₹82 lakh
```

The model learns how clues connect to the answer.

---

# What Is Target Variable?

The target variable is the column we want to predict.

In house price prediction:

```text
Target = Price
```

Because our question is:

**What is the price?**

Target variable is also called:

- Label
- Output
- Dependent variable
- y

---

# Target Examples

| Problem | Target Variable |
|---|---|
| Predict house price | Price |
| Predict student marks | Marks |
| Predict pass/fail | Result |
| Predict disease/no disease | Disease Status |
| Predict salary | Salary |
| Predict sales | Sales Amount |
| Predict spam/not spam | Spam Status |

---

# X and y Meaning

In Machine Learning code, we commonly use:

```python
X
y
```

Meaning:

```text
X = input features
y = target variable
```

For house price:

```text
X = Area, Bedrooms, House Age, Distance
y = Price
```

Read it as:

```text
Given X, predict y.
```

---

# Python Example

```python
X = df[["area", "bedrooms", "house_age", "distance"]]
y = df["price"]
```

Meaning:

```text
Use area, bedrooms, house age, and distance to predict price.
```

This is the first step before training a model.

---

# Why X Is Capital and y Is Small

Simple reason:

```text
X usually contains multiple columns.
y usually contains one column.
```

Example:

```text
X = area, bedrooms, age, distance
```

This is a table with many columns.

```text
y = price
```

This is usually one column.

---

# One Row Example

| Area | Bedrooms | House Age | Distance | Price |
|---:|---:|---:|---:|---:|
| 1500 | 3 | 3 | 5 | 82 |

For this row:

Features:

```text
Area = 1500
Bedrooms = 3
House Age = 3
Distance = 5
```

Target:

```text
Price = 82
```

---

# Many Rows Teach the Model

The model learns from many examples:

```text
Row 1: features → target
Row 2: features → target
Row 3: features → target
Row 4: features → target
```

After learning, it can predict target for a new row.

---

# New Prediction Example

New house:

| Area | Bedrooms | House Age | Distance |
|---:|---:|---:|---:|
| 1700 | 3 | 4 | 6 |

Here, price is unknown.

So:

```text
Features are available.
Target is unknown.
```

The trained model predicts:

```text
Price = maybe ₹90 lakh
```

---

# Important Rule

## Target should not be inside features

Wrong:

```python
X = df[["area", "bedrooms", "house_age", "distance", "price"]]
y = df["price"]
```

Why wrong?

The model is already seeing the answer.

It is like giving an exam question with the answer printed beside it.

---

# Correct Feature Selection

Correct:

```python
X = df[["area", "bedrooms", "house_age", "distance"]]
y = df["price"]
```

Golden rule:

```text
Features should not contain the target column.
```

---

# Doctor Analogy

A doctor predicts disease risk using:

- Age
- Weight
- Blood pressure
- Sugar level
- Cholesterol
- Symptoms

These are features.

Disease result:

```text
Disease / No Disease
```

This is the target.

The doctor uses symptoms and test values to decide disease.

Similarly, the ML model uses features to predict target.

---

# Student Marks Prediction

| Study Hours | Attendance | Previous Marks | Final Marks |
|---:|---:|---:|---:|
| 2 | 60 | 40 | 45 |
| 5 | 85 | 70 | 78 |
| 6 | 90 | 80 | 88 |
| 1 | 45 | 25 | 30 |

Goal:

**Predict final marks.**

Features:

- Study Hours
- Attendance
- Previous Marks

Target:

- Final Marks

This is Regression because final marks is a number.

---

# Student Result Classification

| Study Hours | Attendance | Previous Marks | Result |
|---:|---:|---:|---|
| 2 | 60 | 40 | Fail |
| 5 | 85 | 70 | Pass |
| 6 | 90 | 80 | Pass |
| 1 | 45 | 25 | Fail |

Goal:

**Predict pass or fail.**

Features:

- Study Hours
- Attendance
- Previous Marks

Target:

- Result

This is Classification because result is a category.

---

# How to Identify Features and Target

Ask two questions:

## Question 1

**What do I want to predict?**

That is the target variable.

Example:

```text
I want to predict house price.
Target = Price
```

## Question 2

**What information do I use to predict it?**

Those are the features.

Example:

```text
Features = Area, Bedrooms, Age, Distance
```

---

# Feature Selection Thinking

Not every column is useful.

Suppose house data has:

```text
House ID
Owner Name
Area
Bedrooms
Age
Distance
Price
```

Useful features:

```text
Area
Bedrooms
Age
Distance
```

Not useful or risky features:

```text
House ID
Owner Name
```

Good features should have some relationship with the target.

---

# Feature and Target Examples by Domain

| Domain | Features | Target |
|---|---|---|
| Real estate | Area, bedrooms, location, age | Price |
| Education | Study hours, attendance, previous marks | Final marks |
| Banking | Income, credit score, loan amount | Loan approved/rejected |
| Healthcare | Age, BP, sugar level, symptoms | Disease status |
| Retail | Month, product, discount, ad spend | Sales amount |
| HR | Experience, skills, interview score | Salary |

---

# Small Python Example

```python
import pandas as pd

data = {
    "area": [1000, 1500, 2000, 900],
    "bedrooms": [2, 3, 4, 2],
    "house_age": [5, 3, 2, 10],
    "distance": [8, 5, 4, 12],
    "price": [55, 82, 120, 42]
}

df = pd.DataFrame(data)

X = df[["area", "bedrooms", "house_age", "distance"]]
y = df["price"]

print(X)
print(y)
```

---

# Common Confusions

## Is target also a column?

Yes.

Target is a column in training data.

But when predicting new data, target will be unknown.

## Can we have multiple features?

Yes.

Most real ML problems have many features.

## Can target be text?

Yes.

If target is text/category, it is classification.

---

# Final Summary

Remember clearly:

```text
Features = Input columns
Target = Output column
```

In code:

```python
X = features
y = target
```

For house price:

```text
X = Area, Bedrooms, Age, Distance
y = Price
```

Golden rule:

```text
Do not include the target column inside features.
```

---

# Quick Quiz

Identify features and target:

| Experience | Skills Score | Interview Score | Salary |
|---:|---:|---:|---:|
| 1 | 60 | 55 | ₹4 LPA |
| 3 | 75 | 70 | ₹7 LPA |
| 5 | 85 | 80 | ₹12 LPA |

Goal:

**Predict salary.**

---

# Quick Quiz Answer

Features:

```text
Experience
Skills Score
Interview Score
```

Target:

```text
Salary
```
