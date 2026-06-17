# Simple Linear Regression

## The Simplest Regression Algorithm

Simple Linear Regression is used when we want to predict **one numerical output** using **one input feature**.

**Simple meaning:**  
Simple Linear Regression predicts a number using a straight-line relationship.

---

# Why “Simple”?

It is called **Simple** because it uses only one input feature.

Example:

```text
Area → House Price
```

- Input feature: Area
- Target variable: Price

Only one feature is used, so it is called **Simple Linear Regression**.

---

# Why “Linear”?

It is called **Linear** because the model tries to draw a **straight line** through the data.

Example:

| Area | Price |
|---:|---:|
| 1000 sqft | ₹50 lakh |
| 1200 sqft | ₹60 lakh |
| 1500 sqft | ₹75 lakh |
| 1800 sqft | ₹90 lakh |
| 2000 sqft | ₹100 lakh |

As area increases, price also increases.

---

# Running Example

Earlier, house price could depend on many features:

- Area
- Bedrooms
- House age
- Distance from city

But for Simple Linear Regression, we use only one feature:

```text
Area → Price
```

Goal:

> Use area to predict house price.

---

# Example Data

| Area | Price |
|---:|---:|
| 1000 | 50 |
| 1200 | 60 |
| 1500 | 75 |
| 1800 | 90 |
| 2000 | 100 |

Price is in lakhs.

The model learns the relationship between **area** and **price**.

---

# Human Thinking

If I ask:

```text
Area = 1600 sqft
Price = ?
```

You may think:

```text
1500 sqft house price = ₹75 lakh
1800 sqft house price = ₹90 lakh
```

So 1600 sqft may be around:

```text
₹80 lakh
```

This is the same kind of pattern Simple Linear Regression learns.

---

# Formula of Simple Linear Regression

The formula is:

```text
y = mx + c
```

In Machine Learning terms:

```text
Predicted Price = slope × Area + intercept
```

Where:

- x = input feature
- y = predicted output
- m = slope
- c = intercept

---

# Formula for House Price

For house price prediction:

```text
Price = m × Area + c
```

Example:

```text
Price = 0.05 × Area + 5
```

This means the model has learned a straight-line relationship between area and price.

---

# What Is Slope?

Slope means:

> How much y changes when x increases by 1 unit.

In our example:

```text
How much does price change when area increases by 1 sqft?
```

If:

```text
Price = 0.05 × Area
```

Then every extra sqft adds around **0.05 lakh**, or **₹5,000**.

---

# What Is Intercept?

Intercept is the starting/base value of the line.

Formula:

```text
Price = m × Area + c
```

Here:

```text
c = intercept
```

Example:

```text
Price = 0.05 × Area + 5
```

Intercept = 5

For beginner understanding:

> Intercept helps place the line correctly.

---

# Example Calculation

Suppose the model learned this formula:

```text
Price = 0.05 × Area + 5
```

Now predict price for:

```text
Area = 1600 sqft
```

Calculation:

```text
Price = 0.05 × 1600 + 5
Price = 80 + 5
Price = ₹85 lakh
```

---

# How Does the Model Learn?

The model looks at all training data points and tries to draw the **best possible straight line**.

The line should pass close to most points.

It may not pass exactly through every point because real data has noise.

Examples of noise:

- Location difference
- Interior quality
- Road access
- Parking
- Builder reputation
- Market condition

---

# Prediction Error

Suppose:

```text
Actual price = ₹82 lakh
Predicted price = ₹85 lakh
```

Error:

```text
85 - 82 = 3 lakh
```

The model is wrong by ₹3 lakh.

Simple Linear Regression tries to find a line where the total error is as small as possible.

---

# Visual Understanding

Imagine dots on a graph.

```text
X-axis = Area
Y-axis = Price
```

Each house is one dot.

The model draws a straight line near these dots.

Then for a new area, it checks the line and predicts the price.

---

# Python Step 1: Import Libraries

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
```

- `pandas` is used for data tables.
- `LinearRegression` is the ML model.

---

# Python Step 2: Create Data

```python
data = {
    "area": [1000, 1200, 1500, 1800, 2000],
    "price": [50, 60, 75, 90, 100]
}


df = pd.DataFrame(data)
print(df)
```

This creates our small training dataset.

---

# Python Step 3: Separate X and y

```python
X = df[["area"]]
y = df["price"]
```

Meaning:

```text
X = input feature
y = target variable
```

Important:

```python
X = df[["area"]]
```

We use double brackets because scikit-learn expects X as a 2D table.

---

# Python Step 4: Create the Model

```python
model = LinearRegression()
```

This creates an empty Linear Regression model.

At this point, the model has not learned anything yet.

---

# Python Step 5: Train the Model

```python
model.fit(X, y)
```

Meaning:

```text
Learn the relationship between area and price.
```

The model now learns that price increases when area increases.

---

# Python Step 6: Predict New House Price

```python
new_house = pd.DataFrame({
    "area": [1600]
})

predicted_price = model.predict(new_house)

print("Predicted price:", predicted_price[0], "lakhs")
```

Output may be around:

```text
Predicted price: 80.0 lakhs
```

---

# Full Code Together

```python
import pandas as pd
from sklearn.linear_model import LinearRegression


data = {
    "area": [1000, 1200, 1500, 1800, 2000],
    "price": [50, 60, 75, 90, 100]
}


df = pd.DataFrame(data)

X = df[["area"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)

new_house = pd.DataFrame({
    "area": [1600]
})

predicted_price = model.predict(new_house)

print("Predicted price:", predicted_price[0], "lakhs")
```

---

# Checking Slope and Intercept

After training, we can see what the model learned.

```python
print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
```

Example output:

```text
Slope: 0.05
Intercept: 0.0
```

Meaning:

```text
Price = 0.05 × Area + 0
```

---

# Important Limitation

Simple Linear Regression uses only one feature.

But real house price depends on many things:

- Location
- Bedrooms
- House age
- Parking
- Nearby metro
- Road width
- Construction quality

So Simple Linear Regression is useful for learning, but real projects usually need more features.

---

# When to Use Simple Linear Regression

Use it when:

- There is one main input feature
- The output is numerical
- The relationship is roughly straight-line
- You want simple explanation

Examples:

- Study hours → Marks
- Experience → Salary
- Area → Price
- Ad spend → Sales
- Temperature → Ice cream sales

---

# Common Beginner Mistakes

## Mistake 1

Thinking prediction is always exact.

Regression gives an estimate.

```text
Predicted price = ₹80 lakh
Actual price = ₹83 lakh
```

Small difference is normal.

---

# Common Beginner Mistakes

## Mistake 2

Using Simple Linear Regression for every problem.

Simple Linear Regression uses only one input.

Real-world problems usually need multiple inputs.

---

# Common Beginner Mistakes

## Mistake 3

Confusing slope and intercept.

Remember:

```text
Slope = rate of change
Intercept = starting/base value
```

For house price:

```text
Slope = price increase per sqft
Intercept = line starting point
```

---

# Final Summary

Simple Linear Regression means:

```text
One input feature + one numerical target + straight-line relationship
```

For house price:

```text
Area → Price
```

Formula:

```text
Price = slope × Area + intercept
```

---

# Memory Line

```text
Simple = one input
Linear = straight line
Regression = predicts number
```

Next topic:

# Multiple Linear Regression
