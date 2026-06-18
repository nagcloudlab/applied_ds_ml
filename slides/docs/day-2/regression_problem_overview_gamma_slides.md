# Regression Problem Overview

## Slide 1: Section Title
# Regression Problem Overview

**Theme:** Regression means predicting a number.

Example:

> Predicting house price based on area, bedrooms, age, and distance.

---

## Slide 2: What Is Regression?

Regression is a type of **Supervised Machine Learning**.

Simple meaning:

> Regression means predicting a numerical value.

Examples:

- House price
- Salary
- Student marks
- Monthly sales
- Temperature
- Delivery time
- Electricity consumption

---

## Slide 3: Our Running Example

### House Price Prediction

We have old house data:

| Area | Bedrooms | House Age | Distance | Price |
|---:|---:|---:|---:|---:|
| 1000 sqft | 2 | 5 years | 8 km | ₹55 lakh |
| 1500 sqft | 3 | 3 years | 5 km | ₹82 lakh |
| 2000 sqft | 4 | 2 years | 4 km | ₹120 lakh |
| 900 sqft | 2 | 10 years | 12 km | ₹42 lakh |

Goal:

> Predict the price of a new house.

---

## Slide 4: Input and Output

For house price prediction:

**Input features:**

- Area
- Bedrooms
- House age
- Distance from city

**Target variable:**

- Price

So the model learns:

```text
Area + Bedrooms + Age + Distance → Price
```

---

## Slide 5: Why Is This Regression?

The output is:

```text
Price = ₹90 lakh
```

Price is a **number**.

So this is a regression problem.

Simple rule:

> If the output is a measurable number, it is usually regression.

---

## Slide 6: Regression Belongs to Supervised Learning

Supervised learning means:

> Data has inputs and correct answers.

In our example:

```text
Input  = Area, Bedrooms, Age, Distance
Answer = Price
```

Since the answer is available and it is numerical:

```text
Supervised Learning → Regression
```

---

## Slide 7: Easy Memory Line

Regression answers the question:

# How much?

Examples:

- How much is the house price?
- How much salary should be offered?
- How many marks will the student score?
- How much sales will happen next month?
- How much time will delivery take?

---

## Slide 8: Regression vs Classification

| Question | Output | Type |
|---|---|---|
| What is the house price? | ₹90 lakh | Regression |
| Will the loan be approved? | Yes / No | Classification |
| What are the final marks? | 82 | Regression |
| Will the student pass? | Pass / Fail | Classification |
| What is tomorrow’s temperature? | 32°C | Regression |
| Is this email spam? | Spam / Not Spam | Classification |

Remember:

```text
Regression = Number
Classification = Category
```

---

## Slide 9: Student Example — Regression

### Goal: Predict final marks

| Study Hours | Attendance | Previous Marks | Final Marks |
|---:|---:|---:|---:|
| 2 | 60% | 40 | 45 |
| 5 | 85% | 70 | 78 |
| 6 | 90% | 80 | 88 |

Target:

```text
Final Marks
```

Output is a number.

So this is **Regression**.

---

## Slide 10: Student Example — Classification

### Goal: Predict pass or fail

| Study Hours | Attendance | Previous Marks | Result |
|---:|---:|---:|---|
| 2 | 60% | 40 | Fail |
| 5 | 85% | 70 | Pass |
| 6 | 90% | 80 | Pass |

Target:

```text
Result
```

Output is a category.

So this is **Classification**.

---

## Slide 11: Regression Is an Estimate

Regression predictions are usually not exact.

Example:

```text
Actual house price    = ₹92 lakh
Predicted house price = ₹90 lakh
```

The prediction is close.

So the model is useful.

But if prediction is:

```text
Predicted house price = ₹60 lakh
```

Then the error is large.

---

## Slide 12: What Is Error?

Error means:

> Difference between actual value and predicted value.

Example:

```text
Actual price    = ₹100 lakh
Predicted price = ₹92 lakh
Error           = ₹8 lakh
```

Regression models are evaluated by checking:

> How far are predictions from actual values?

---

## Slide 13: Small Error vs Large Error

Small error means better model.

Large error means poor model.

Example:

| Actual Price | Predicted Price | Error |
|---:|---:|---:|
| ₹100 lakh | ₹98 lakh | ₹2 lakh |
| ₹100 lakh | ₹92 lakh | ₹8 lakh |
| ₹100 lakh | ₹60 lakh | ₹40 lakh |

Later, we measure this using:

- MAE
- MSE
- RMSE
- R² Score

---

## Slide 14: Real-Life Regression Example 1

# Salary Prediction

**Features:**

- Experience
- Education
- Skills score
- Interview score
- Location

**Target:**

- Salary

Since salary is a number, this is regression.

---

## Slide 15: Real-Life Regression Example 2

# Sales Prediction

**Features:**

- Month
- Product category
- Festival season
- Discount
- Advertisement spend
- Previous sales

**Target:**

- Sales amount

Since sales amount is numerical, this is regression.

---

## Slide 16: Real-Life Regression Example 3

# Delivery Time Prediction

**Features:**

- Distance
- Traffic level
- Weather
- Order size
- Delivery partner availability

**Target:**

- Delivery time in minutes

Since delivery time is a number, this is regression.

---

## Slide 17: Real-Life Regression Example 4

# Electricity Consumption Prediction

**Features:**

- Temperature
- Day of week
- Number of people
- Appliance usage
- Previous consumption

**Target:**

- Electricity units consumed

Since units consumed is numerical, this is regression.

---

## Slide 18: Regression Mental Model

Think of a real estate agent.

They look at:

- Area
- Location
- Age
- Facilities
- Market trend

Then they estimate:

```text
This house may sell for around ₹90 lakh.
```

That is regression thinking.

---

## Slide 19: Regression Output Can Be Decimal

Regression output can be an integer or decimal.

Examples:

- Temperature = 32.7°C
- Delivery time = 42.5 minutes
- House price = ₹87.6 lakh
- Sales forecast = ₹12.35 lakh

Main rule:

> The output should be a measurable numerical value.

---

## Slide 20: Beginner Confusion

### If output is number, is it always regression?

Mostly yes, but be careful.

Some numbers are actually labels.

Examples:

```text
Class 1, Class 2, Class 3
Pincode
Product ID
Customer ID
```

These are numbers, but they represent categories or identifiers.

---

## Slide 21: Better Rule

Use this rule:

```text
If the number is a measurable quantity → Regression
If the number is only a label/category → Classification or not useful as target
```

Examples:

| Value | Meaning | ML Type |
|---|---|---|
| Price | Measurable quantity | Regression |
| Temperature | Measurable quantity | Regression |
| Class 1/2/3 | Category | Classification |
| Product ID | Identifier | Not a useful target |

---

## Slide 22: One Feature or Many Features?

Regression can use one feature or many features.

### One feature

```text
Area → Price
```

This can become **Simple Linear Regression**.

### Many features

```text
Area + Bedrooms + Age + Distance → Price
```

This can become **Multiple Linear Regression**.

---

## Slide 23: Regression Project Flow

A regression project usually follows this flow:

```text
Collect past data
        ↓
Identify features and target
        ↓
Split data into train and test
        ↓
Train regression model
        ↓
Predict numerical value
        ↓
Measure error
        ↓
Improve model
```

---

## Slide 24: House Price Regression Flow

For our house price example:

```text
Collect old house price data
        ↓
Features = Area, Bedrooms, Age, Distance
Target   = Price
        ↓
Train-test split
        ↓
Train model
        ↓
Predict new house price
        ↓
Check prediction error
```

---

## Slide 25: Python Preview

```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

X = df[["area", "bedrooms", "age", "distance"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

prediction = model.predict(X_test)
```

Meaning:

> We trained a regression model to predict price.

---

## Slide 26: Final Summary

Remember:

```text
Regression means predicting a number.
```

Regression examples:

- House price
- Salary
- Marks
- Sales
- Temperature
- Delivery time
- Electricity usage

Simple memory:

```text
Regression = How much?
Classification = Which category?
```

---

## Slide 27: Quick Quiz

Identify whether each problem is regression or classification.

1. Predict house price
2. Predict pass or fail
3. Predict monthly sales
4. Predict spam or not spam
5. Predict delivery time

Answers:

```text
1. Regression
2. Classification
3. Regression
4. Classification
5. Regression
```

---

## Slide 28: Transition

Now that we understand regression, the next topic is:

# Simple Linear Regression

We will learn how a model predicts a number using one input feature.

Example:

```text
Area → House Price
```
