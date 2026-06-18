# Hands-on Regression Model Building Using Scikit-learn

## Slide 1: Section Opening

# Hands-on Regression Model Building Using Scikit-learn

### Build a complete regression model step by step

In this section, we connect everything we learned:

- Features and target
- Train-test split
- Regression model
- Prediction
- Evaluation metrics

---

## Slide 2: What Is Scikit-learn?

Scikit-learn is a popular Python library for Machine Learning.

It provides ready-made tools for:

- Data splitting
- Regression models
- Classification models
- Clustering models
- Evaluation metrics
- Preprocessing
- Model selection

In this lesson, we use Scikit-learn to build a house price prediction model.

---

## Slide 3: Problem Statement

We have old house data.

Each house has:

- Area
- Bedrooms
- House age
- Distance from city
- Price

Our goal:

> **Predict the price of a new house.**

This is a regression problem because:

```text
Price is a number.
```

---

## Slide 4: Dataset

Sample house price data:

| Area | Bedrooms | Age | Distance | Price |
|---:|---:|---:|---:|---:|
| 900 | 2 | 10 | 12 | 45 |
| 1000 | 2 | 8 | 10 | 52 |
| 1200 | 2 | 6 | 9 | 58 |
| 1500 | 3 | 5 | 7 | 72 |
| 1600 | 3 | 4 | 6 | 78 |
| 1800 | 3 | 7 | 8 | 85 |
| 2000 | 4 | 3 | 5 | 105 |
| 2200 | 4 | 2 | 4 | 120 |
| 2500 | 4 | 5 | 6 | 135 |
| 2800 | 5 | 1 | 3 | 160 |

Price is in lakhs.

---

## Slide 5: ML Workflow

Every basic regression project follows this flow:

```text
Step 1: Import libraries
Step 2: Create/load dataset
Step 3: Separate features and target
Step 4: Split data into train and test
Step 5: Create model
Step 6: Train model
Step 7: Predict using test data
Step 8: Evaluate model
Step 9: Predict new data
```

---

## Slide 6: Step 1 — Import Libraries

```python
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
```

Meaning:

- `pandas` → create and manage data table
- `numpy` → numerical calculations
- `train_test_split` → split data
- `LinearRegression` → regression model
- `metrics` → evaluate model

---

## Slide 7: Step 2 — Create Dataset

```python
data = {
    "area": [900, 1000, 1200, 1500, 1600, 1800, 2000, 2200, 2500, 2800],
    "bedrooms": [2, 2, 2, 3, 3, 3, 4, 4, 4, 5],
    "age": [10, 8, 6, 5, 4, 7, 3, 2, 5, 1],
    "distance": [12, 10, 9, 7, 6, 8, 5, 4, 6, 3],
    "price": [45, 52, 58, 72, 78, 85, 105, 120, 135, 160]
}

df = pd.DataFrame(data)

print(df)
```

Each row is one house.

Each column gives information about that house.

---

## Slide 8: Step 3 — Separate Features and Target

Our goal is to predict:

```text
price
```

So:

```python
X = df[["area", "bedrooms", "age", "distance"]]
y = df["price"]
```

Here:

```text
X = input features
y = target variable
```

Features:

- area
- bedrooms
- age
- distance

Target:

- price

---

## Slide 9: Important Rule

Do not include price inside `X`.

Wrong:

```python
X = df[["area", "bedrooms", "age", "distance", "price"]]
```

Correct:

```python
X = df[["area", "bedrooms", "age", "distance"]]
```

Golden rule:

> **The target column should not be inside the input features.**

---

## Slide 10: Step 4 — Train-Test Split

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
```

Meaning:

```text
80% data → training
20% data → testing
```

Training data teaches the model.

Testing data checks the model.

---

## Slide 11: Train-Test Split Mental Model

```text
Full Data
    ↓
Training Data + Testing Data
    ↓
Train model on training data
    ↓
Check model on testing data
```

Simple analogy:

```text
Training data = practice questions
Testing data = exam questions
```

---

## Slide 12: Step 5 — Create the Model

```python
model = LinearRegression()
```

This creates an empty Linear Regression model.

At this point:

```text
The model has not learned anything yet.
```

It is like a new student before studying.

---

## Slide 13: Step 6 — Train the Model

```python
model.fit(X_train, y_train)
```

Meaning:

```text
Learn the relationship between house features and price.
```

The model learns patterns like:

- Bigger area usually increases price
- More bedrooms may increase price
- Older house may reduce price
- Farther distance may reduce price

---

## Slide 14: Important Word — fit()

In Scikit-learn:

```python
model.fit(X_train, y_train)
```

means:

```text
Train the model.
```

Simple memory:

```text
fit = learn
```

---

## Slide 15: Step 7 — Predict Test Data

```python
y_pred = model.predict(X_test)
```

Meaning:

```text
Use the trained model to predict prices for test houses.
```

Now we have:

```text
y_test = actual prices
y_pred = predicted prices
```

We compare both.

---

## Slide 16: Important Word — predict()

In Scikit-learn:

```python
model.predict(X_test)
```

means:

```text
Use the trained model to answer new inputs.
```

Simple memory:

```text
predict = answer
```

---

## Slide 17: Step 8 — Evaluate the Model

```python
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
```

Meaning:

- MAE → average mistake
- MSE → squared mistake average
- RMSE → bigger mistakes punished
- R² → model explanation score

---

## Slide 18: Metrics Direction

| Metric | Better Direction |
|---|---|
| MAE | Lower is better |
| MSE | Lower is better |
| RMSE | Lower is better |
| R² | Higher is better |

Simple memory:

```text
Error metrics → lower is better
R² score → higher is better
```

---

## Slide 19: Step 9 — Predict a New House

Suppose a new house has:

```text
Area = 1700 sqft
Bedrooms = 3
Age = 4 years
Distance = 6 km
```

Code:

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

---

## Slide 20: Complete Code — Part 1

```python
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


data = {
    "area": [900, 1000, 1200, 1500, 1600, 1800, 2000, 2200, 2500, 2800],
    "bedrooms": [2, 2, 2, 3, 3, 3, 4, 4, 4, 5],
    "age": [10, 8, 6, 5, 4, 7, 3, 2, 5, 1],
    "distance": [12, 10, 9, 7, 6, 8, 5, 4, 6, 3],
    "price": [45, 52, 58, 72, 78, 85, 105, 120, 135, 160]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)
```

---

## Slide 21: Complete Code — Part 2

```python
X = df[["area", "bedrooms", "age", "distance"]]
y = df["price"]

print("\\nFeatures:")
print(X)

print("\\nTarget:")
print(y)


X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\\nTraining rows:", len(X_train))
print("Testing rows:", len(X_test))
```

---

## Slide 22: Complete Code — Part 3

```python
model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("\\nActual prices:")
print(list(y_test))

print("\\nPredicted prices:")
print(list(np.round(y_pred, 2)))
```

---

## Slide 23: Complete Code — Part 4

```python
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\\nModel Evaluation:")
print("MAE :", round(mae, 2))
print("MSE :", round(mse, 2))
print("RMSE:", round(rmse, 2))
print("R2  :", round(r2, 2))
```

---

## Slide 24: Complete Code — Part 5

```python
coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})

print("\\nModel Coefficients:")
print(coefficients)

print("\\nIntercept:", round(model.intercept_, 2))
```

The coefficient table shows how each feature contributes to price direction.

---

## Slide 25: Complete Code — Part 6

```python
new_house = pd.DataFrame({
    "area": [1700],
    "bedrooms": [3],
    "age": [4],
    "distance": [6]
})

predicted_price = model.predict(new_house)

print("\\nNew House Details:")
print(new_house)

print("\\nPredicted price for new house:", round(predicted_price[0], 2), "lakhs")
```

This predicts price for a new unseen house.

---

## Slide 26: How to Read the Output

You may see actual and predicted prices like:

```text
Actual prices:
[135, 52]

Predicted prices:
[130.5, 50.8]
```

Meaning:

```text
For first test house:
Actual = 135 lakh
Predicted = 130.5 lakh

For second test house:
Actual = 52 lakh
Predicted = 50.8 lakh
```

---

## Slide 27: How to Read Metrics

Example:

```text
MAE  = 4.5
RMSE = 5.2
R²   = 0.93
```

Meaning:

```text
MAE  = average prediction mistake
RMSE = error with stronger penalty for large mistakes
R²   = how well model explains the target
```

For house price:

```text
MAE = 4.5 means average error is around ₹4.5 lakh.
```

---

## Slide 28: What Coefficients Mean

Example coefficient table:

| Feature | Coefficient |
|---|---:|
| area | positive |
| bedrooms | positive |
| age | negative |
| distance | negative |

Meaning:

```text
Positive coefficient → increases price
Negative coefficient → decreases price
```

Example:

```text
area positive → bigger house increases price
age negative → older house may reduce price
distance negative → farther from city may reduce price
```

---

## Slide 29: Complete ML Flow in One Line

```text
Data → X/y → train-test split → train model → predict → evaluate → use on new data
```

For house price:

```text
House data
    ↓
features/price
    ↓
split
    ↓
train Linear Regression
    ↓
predict prices
    ↓
check error
    ↓
predict new house price
```

---

## Slide 30: Common Mistake 1

# Including target inside features

Wrong:

```python
X = df[["area", "bedrooms", "age", "distance", "price"]]
```

Correct:

```python
X = df[["area", "bedrooms", "age", "distance"]]
```

Reason:

```text
The model should not see the answer column as input.
```

---

## Slide 31: Common Mistake 2

# Predicting before training

Wrong:

```python
model = LinearRegression()
model.predict(X_test)
```

Correct:

```python
model = LinearRegression()
model.fit(X_train, y_train)
model.predict(X_test)
```

Reason:

```text
The model must learn before predicting.
```

---

## Slide 32: Common Mistake 3

# Evaluating with X instead of y

Wrong thinking:

```text
Compare X_test with y_pred
```

Correct thinking:

```text
Compare y_test with y_pred
```

Because:

```text
y_test = actual answers
y_pred = model predictions
```

---

## Slide 33: Final Summary

Remember this workflow:

```python
X = df[["feature1", "feature2"]]
y = df["target"]

X_train, X_test, y_train, y_test = train_test_split(X, y)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
```

---

## Slide 34: Memory Hook

```text
fit = learn
predict = answer
metric = check
```

Full ML memory:

```text
Data → Split → Fit → Predict → Check → Use
```

Next topic:

# Introduction to PyCaret
