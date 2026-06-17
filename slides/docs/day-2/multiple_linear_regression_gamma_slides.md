# Multiple Linear Regression
## Predicting a Number Using Many Input Features

Audience: Beginner ML learners  
Running example: House price prediction  
Goal: Understand how multiple input features can predict one numerical target.

---

# Slide 1: Connect with Previous Topic

In Simple Linear Regression, we used only one input feature.

Example:

```text
Area → Price
```

But in real life, house price does not depend only on area.

It may also depend on:

- Bedrooms
- House age
- Distance from city
- Parking
- Location
- Floor
- Nearby metro
- Construction quality

So now we need a model that can use many input features.

That model is called **Multiple Linear Regression**.

---

# Slide 2: What is Multiple Linear Regression?

Multiple Linear Regression means:

> Predicting one numerical output using more than one input feature.

For house price prediction:

```text
Area + Bedrooms + House Age + Distance → Price
```

Here:

- Inputs = multiple features
- Output = one numerical target

So this is a regression problem with many input columns.

---

# Slide 3: Why the Word “Multiple”?

It is called **Multiple** because we use multiple input features.

Example:

| Feature | Meaning |
|---|---|
| Area | Size of the house |
| Bedrooms | Number of bedrooms |
| House Age | How old the house is |
| Distance | Distance from city center |

Target variable:

```text
Price
```

Simple idea:

```text
Multiple inputs → One output
```

---

# Slide 4: Why the Word “Linear”?

It is called **Linear** because the model assumes a straight-line type relationship between each feature and the target.

Simple examples:

- If area increases, price may increase.
- If bedrooms increase, price may increase.
- If house age increases, price may decrease.
- If distance from city increases, price may decrease.

The model represents these relationships using a formula.

---

# Slide 5: Simple vs Multiple Linear Regression

Simple Linear Regression formula:

```text
Price = slope × Area + intercept
```

Multiple Linear Regression formula:

```text
Price = b0 + b1×Area + b2×Bedrooms + b3×Age + b4×Distance
```

Where:

- b0 = intercept
- b1 = coefficient for Area
- b2 = coefficient for Bedrooms
- b3 = coefficient for Age
- b4 = coefficient for Distance

Each feature gets its own coefficient.

---

# Slide 6: What is a Coefficient?

A coefficient tells how a feature affects the target.

Simple meaning:

> A coefficient is the importance or effect value learned for a feature.

Example:

```text
Price = 10 + 0.04×Area + 5×Bedrooms - 1×Age - 2×Distance
```

Here:

- Area coefficient = 0.04
- Bedrooms coefficient = 5
- Age coefficient = -1
- Distance coefficient = -2

---

# Slide 7: Positive and Negative Coefficients

Positive coefficient means:

```text
Feature increases → Target increases
```

Negative coefficient means:

```text
Feature increases → Target decreases
```

In house price:

- Area may have a positive coefficient.
- Bedrooms may have a positive coefficient.
- Age may have a negative coefficient.
- Distance may have a negative coefficient.

This matches real-life thinking.

---

# Slide 8: Example Formula

Suppose the model learns this formula:

```text
Price = 10 + 0.04×Area + 5×Bedrooms - 1×Age - 2×Distance
```

Meaning:

- Base value = 10
- Area effect = 0.04 × Area
- Bedroom effect = 5 × Bedrooms
- Age effect = -1 × Age
- Distance effect = -2 × Distance

Price is measured in lakhs.

---

# Slide 9: Understand Area Coefficient

Formula:

```text
Price = 10 + 0.04×Area + 5×Bedrooms - 1×Age - 2×Distance
```

Area coefficient = 0.04

Meaning:

```text
For every 1 sqft increase, price increases by 0.04 lakh.
```

0.04 lakh = ₹4,000

So if area increases by 100 sqft:

```text
Price increases by around ₹4 lakh.
```

---

# Slide 10: Understand Bedroom Coefficient

Bedroom coefficient = 5

Meaning:

```text
For every extra bedroom, price increases by around ₹5 lakh.
```

Example:

- 2-bedroom house → lower price
- 3-bedroom house → higher price
- 4-bedroom house → even higher price

But this is after considering other features also.

---

# Slide 11: Understand Age Coefficient

Age coefficient = -1

Meaning:

```text
For every 1 year older, price decreases by around ₹1 lakh.
```

Example:

- 2-year-old house → better price
- 10-year-old house → lower price

The negative sign shows that age may reduce price.

---

# Slide 12: Understand Distance Coefficient

Distance coefficient = -2

Meaning:

```text
For every 1 km farther from city, price decreases by around ₹2 lakh.
```

Example:

- 4 km from city → higher price
- 12 km from city → lower price

The negative sign shows that distance may reduce price.

---

# Slide 13: Manual Calculation Example

Formula:

```text
Price = 10 + 0.04×Area + 5×Bedrooms - 1×Age - 2×Distance
```

New house:

```text
Area = 1500 sqft
Bedrooms = 3
Age = 4 years
Distance = 6 km
```

Calculation:

```text
Price = 10 + 0.04×1500 + 5×3 - 1×4 - 2×6
Price = 10 + 60 + 15 - 4 - 12
Price = 69
```

Predicted price:

```text
₹69 lakh
```

---

# Slide 14: Why Multiple Linear Regression is Better

Simple Linear Regression:

```text
Area → Price
```

Problem:

Two houses may have the same area but different prices.

| Area | Bedrooms | Age | Distance | Price |
|---:|---:|---:|---:|---:|
| 1500 | 3 | 3 | 5 km | ₹82 lakh |
| 1500 | 2 | 12 | 15 km | ₹55 lakh |

Both houses have 1500 sqft.

But price is different because other features are different.

---

# Slide 15: Dataset Example

Let us use this dataset:

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

Features:

```text
Area, Bedrooms, Age, Distance
```

Target:

```text
Price
```

---

# Slide 16: Python Step 1 — Import Libraries

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
```

We use:

- `pandas` to create and handle tabular data
- `LinearRegression` to train the regression model

---

# Slide 17: Python Step 2 — Create Data

```python
data = {
    "area": [1000, 1500, 2000, 900, 1800, 2200, 1300, 2500],
    "bedrooms": [2, 3, 4, 2, 3, 4, 2, 4],
    "age": [5, 3, 2, 10, 4, 2, 6, 1],
    "distance": [8, 5, 4, 12, 6, 3, 9, 2],
    "price": [55, 82, 120, 42, 95, 130, 65, 155]
}

df = pd.DataFrame(data)

print(df)
```

This creates our sample house price dataset.

---

# Slide 18: Python Step 3 — Separate Features and Target

```python
X = df[["area", "bedrooms", "age", "distance"]]
y = df["price"]
```

Meaning:

```text
X = multiple input columns
y = one output column
```

Features:

```text
area, bedrooms, age, distance
```

Target:

```text
price
```

---

# Slide 19: Python Step 4 — Train the Model

```python
model = LinearRegression()

model.fit(X, y)
```

Meaning:

```text
Learn how area, bedrooms, age, and distance affect price.
```

The model learns coefficients for each feature.

---

# Slide 20: Python Step 5 — Predict New House Price

```python
new_house = pd.DataFrame({
    "area": [1700],
    "bedrooms": [3],
    "age": [4],
    "distance": [6]
})

predicted_price = model.predict(new_house)

print("Predicted price:", predicted_price[0], "lakhs")
```

The model predicts one numerical value:

```text
Predicted house price
```

---

# Slide 21: Full Code Together

```python
import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "area": [1000, 1500, 2000, 900, 1800, 2200, 1300, 2500],
    "bedrooms": [2, 3, 4, 2, 3, 4, 2, 4],
    "age": [5, 3, 2, 10, 4, 2, 6, 1],
    "distance": [8, 5, 4, 12, 6, 3, 9, 2],
    "price": [55, 82, 120, 42, 95, 130, 65, 155]
}

df = pd.DataFrame(data)

X = df[["area", "bedrooms", "age", "distance"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)

new_house = pd.DataFrame({
    "area": [1700],
    "bedrooms": [3],
    "age": [4],
    "distance": [6]
})

predicted_price = model.predict(new_house)

print("Predicted price:", predicted_price[0], "lakhs")
```

---

# Slide 22: Checking Coefficients

After training, we can check what the model learned.

```python
print("Intercept:", model.intercept_)
print("Coefficients:", model.coef_)
```

Better view with feature names:

```python
coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})

print(coefficients)
```

---

# Slide 23: Reading Coefficients

Example output idea:

| Feature | Coefficient |
|---|---:|
| area | positive value |
| bedrooms | positive value |
| age | negative value |
| distance | negative value |

Meaning:

```text
Positive coefficient → increases price
Negative coefficient → decreases price
```

For beginner level, focus more on direction than exact value.

---

# Slide 24: Important Warning About Coefficients

Do not blindly compare coefficient size.

Why?

Because features may be on different scales.

Example:

```text
Area may be 1000 to 3000
Bedrooms may be 1 to 5
Age may be 1 to 30
Distance may be 1 to 50
```

Beginner-safe understanding:

```text
Coefficient sign tells direction.
Positive = increases target.
Negative = decreases target.
```

---

# Slide 25: With Train-Test Split

In real projects, we should not train and test on the same data.

We split data first:

```python
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
```

Meaning:

```text
Train on training data.
Predict on testing data.
Compare actual vs predicted prices.
```

---

# Slide 26: Common Beginner Mistake

Wrong:

```python
X = df[["area", "bedrooms", "age", "distance", "price"]]
y = df["price"]
```

Why wrong?

Because price is included inside the input features.

That means the model already sees the answer.

Correct:

```python
X = df[["area", "bedrooms", "age", "distance"]]
y = df["price"]
```

Golden rule:

```text
Target column should not be inside features.
```

---

# Slide 27: Another Real-Life Example — Salary Prediction

Features:

- Experience
- Skill score
- Interview score
- Education level

Target:

```text
Salary
```

Formula idea:

```text
Salary = b0 + b1×Experience + b2×SkillScore + b3×InterviewScore + b4×EducationLevel
```

This is also Multiple Linear Regression.

---

# Slide 28: Simple vs Multiple Linear Regression

| Point | Simple Linear Regression | Multiple Linear Regression |
|---|---|---|
| Input features | One | More than one |
| Example | Area → Price | Area + Bedrooms + Age → Price |
| Formula | y = mx + c | y = b0 + b1x1 + b2x2 + ... |
| Real-world usefulness | Basic | More practical |
| Visualization | Easy | Harder |

---

# Slide 29: When to Use Multiple Linear Regression

Use it when:

- Target is numerical
- Multiple input features affect the target
- Relationship is roughly linear
- You want an explainable model

Examples:

- House price prediction
- Salary prediction
- Sales forecasting
- Rent prediction
- Marks prediction
- Electricity consumption prediction

---

# Slide 30: Limitations

Multiple Linear Regression may not work well when:

- Relationship is highly non-linear
- Features interact in complex ways
- Data has many outliers
- Important features are missing
- Data quality is poor

Example:

House price may depend heavily on location quality.

If location is missing, model prediction may be weak.

---

# Slide 31: Final Summary

Remember:

```text
Multiple Linear Regression = many input features + one numerical target
```

For house price:

```text
Area + Bedrooms + Age + Distance → Price
```

Formula:

```text
Price = b0 + b1×Area + b2×Bedrooms + b3×Age + b4×Distance
```

Simple memory:

```text
Simple Linear Regression = one input
Multiple Linear Regression = many inputs
Both predict a number
```

---

# Slide 32: Check Your Understanding

Question:

A company wants to predict salary using:

```text
Experience
Skill score
Interview score
Education level
```

Target:

```text
Salary
```

What type of problem is this?

Answer:

```text
Supervised Learning → Regression → Multiple Linear Regression
```

Why?

```text
Salary is a number, and there are multiple input features.
```
