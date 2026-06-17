# Regression Evaluation Metrics

## Slide 1: Section Opening

# Regression Evaluation Metrics

### How do we know if a regression model is good?

So far, we learned models that predict numbers:

- Linear Regression
- Decision Tree Regression
- Random Forest Regression

Now the big question is:

> **How do we know whether the prediction is good or bad?**

That is where evaluation metrics help.

---

## Slide 2: Why Do We Need Evaluation Metrics?

Suppose a model predicts house price.

| Actual Price | Predicted Price |
|---:|---:|
| 80 lakh | 78 lakh |
| 100 lakh | 90 lakh |
| 60 lakh | 70 lakh |

Some predictions are close.

Some predictions are far.

But we need one proper number to measure model performance.

That number is called an **evaluation metric**.

---

## Slide 3: Simple Meaning

# Evaluation Metric

> **An evaluation metric tells how good or bad the model is.**

For regression, we compare:

```text
Actual value vs Predicted value
```

Example:

```text
Actual price = ₹100 lakh
Predicted price = ₹90 lakh
```

Difference:

```text
100 - 90 = 10 lakh
```

The model made an error of ₹10 lakh.

---

## Slide 4: What Is Error?

# Error

> **Error means difference between actual value and predicted value.**

Formula:

```text
Error = Actual - Predicted
```

Example:

```text
Actual = 80
Predicted = 75

Error = 80 - 75 = 5
```

Another example:

```text
Actual = 80
Predicted = 85

Error = 80 - 85 = -5
```

---

## Slide 5: Error Can Be Positive or Negative

The negative sign only shows direction.

Example:

```text
Actual = 80
Predicted = 85
Error = -5
```

This means the model predicted 5 more than actual.

But during evaluation, we usually care about:

```text
How big is the mistake?
```

So we often use:

- Absolute error
- Squared error

---

## Slide 6: Sample Data for Metrics

Let us use this example.

| House | Actual Price | Predicted Price |
|---|---:|---:|
| House 1 | 80 | 75 |
| House 2 | 100 | 110 |
| House 3 | 60 | 65 |
| House 4 | 120 | 100 |

Prices are in lakhs.

Now we calculate the errors.

---

## Slide 7: Error Calculation

| House | Actual | Predicted | Error |
|---|---:|---:|---:|
| House 1 | 80 | 75 | 5 |
| House 2 | 100 | 110 | -10 |
| House 3 | 60 | 65 | -5 |
| House 4 | 120 | 100 | 20 |

Errors:

```text
5, -10, -5, 20
```

Error can be positive or negative.

---

## Slide 8: Problem with Normal Average Error

If we directly average errors:

```text
Errors = 5, -10, -5, 20
```

Average error:

```text
(5 + -10 + -5 + 20) / 4 = 10 / 4 = 2.5
```

This says average error is only:

```text
2.5 lakh
```

But that is misleading.

Positive and negative errors cancelled each other.

---

## Slide 9: Why We Need Better Metrics

Actual mistakes were:

```text
5 lakh
10 lakh
5 lakh
20 lakh
```

But normal average error gave only:

```text
2.5 lakh
```

That hides the real mistake.

So regression uses better metrics:

- MAE
- MSE
- RMSE
- R² Score

---

## Slide 10: Metric 1 — MAE

# MAE

```text
MAE = Mean Absolute Error
```

Simple meaning:

> **Average absolute mistake made by the model.**

Absolute means:

```text
Ignore the negative sign.
```

Example:

```text
Error = -10
Absolute Error = 10
```

---

## Slide 11: MAE Calculation

| House | Actual | Predicted | Error | Absolute Error |
|---|---:|---:|---:|---:|
| House 1 | 80 | 75 | 5 | 5 |
| House 2 | 100 | 110 | -10 | 10 |
| House 3 | 60 | 65 | -5 | 5 |
| House 4 | 120 | 100 | 20 | 20 |

MAE:

```text
MAE = (5 + 10 + 5 + 20) / 4
MAE = 40 / 4
MAE = 10
```

---

## Slide 12: How to Interpret MAE

If:

```text
MAE = 10
```

For house price in lakhs, it means:

```text
Average error = ₹10 lakh
```

If:

```text
MAE = 3
```

It means:

```text
Average error = ₹3 lakh
```

Lower MAE is better.

```text
MAE 3 is better than MAE 10
```

---

## Slide 13: Metric 2 — MSE

# MSE

```text
MSE = Mean Squared Error
```

Simple meaning:

> **Average of squared errors.**

Instead of taking absolute value, we square the error.

Why square?

- It makes negative errors positive
- It punishes large errors more strongly

---

## Slide 14: MSE Calculation

Errors:

```text
5, -10, -5, 20
```

Squared errors:

```text
5² = 25
-10² = 100
-5² = 25
20² = 400
```

MSE:

```text
MSE = (25 + 100 + 25 + 400) / 4
MSE = 550 / 4
MSE = 137.5
```

---

## Slide 15: How to Interpret MSE

MSE is useful mathematically.

But for beginners and business users, it is harder to explain.

Why?

Because the unit is squared.

If price is in lakhs, MSE is in:

```text
lakh²
```

That is not easy to explain.

So we often use RMSE.

---

## Slide 16: Metric 3 — RMSE

# RMSE

```text
RMSE = Root Mean Squared Error
```

Simple meaning:

> **Square root of MSE.**

Formula idea:

```text
RMSE = √MSE
```

From our example:

```text
MSE = 137.5
```

So:

```text
RMSE = √137.5
RMSE ≈ 11.73
```

---

## Slide 17: How to Interpret RMSE

If:

```text
RMSE = 11.73
```

For house price in lakhs, it means:

```text
Model error is around ₹11.73 lakh.
```

RMSE is easier than MSE because it comes back to the original unit.

```text
Target unit = lakhs
RMSE unit = lakhs
```

---

## Slide 18: MAE vs RMSE

Both measure error.

But they behave differently.

# MAE

- Average normal error
- Less affected by very large errors
- Easy to explain

# RMSE

- Punishes large errors more
- Useful when large mistakes are serious
- Still in original unit

---

## Slide 19: MAE vs RMSE Example

Model A errors:

```text
5, 5, 5, 5
```

Model B errors:

```text
1, 1, 1, 17
```

Model B has one big mistake.

RMSE will punish Model B more.

Use RMSE when large errors are dangerous.

Examples:

- Medical dosage prediction
- High-value property pricing
- Financial risk prediction

---

## Slide 20: Metric 4 — R² Score

# R² Score

R² is different from MAE, MSE, and RMSE.

MAE, MSE, and RMSE measure error.

R² measures:

> **How well the model explains the variation in the target.**

Simple interpretation:

```text
R² = 1.0 → perfect model
R² = 0.0 → model is like predicting average
R² < 0   → model is worse than predicting average
```

---

## Slide 21: Simple R² Explanation

Suppose house prices are:

```text
60, 80, 100, 120
```

A very basic model could always predict average price.

Average:

```text
90
```

Baseline prediction:

```text
Every house = ₹90 lakh
```

R² checks:

> Is our model better than simply predicting average?

---

## Slide 22: R² Interpretation Table

| R² Score | Meaning |
|---:|---|
| 1.00 | Perfect prediction |
| 0.90 | Very good |
| 0.70 | Good in many cases |
| 0.50 | Moderate |
| 0.00 | No better than average prediction |
| Negative | Worse than average prediction |

Important:

```text
Higher R² is better.
```

But do not use R² alone.

Always check error metrics also.

---

## Slide 23: Metrics Direction

| Metric | Full Form | Better Direction |
|---|---|---|
| MAE | Mean Absolute Error | Lower is better |
| MSE | Mean Squared Error | Lower is better |
| RMSE | Root Mean Squared Error | Lower is better |
| R² | R-squared Score | Higher is better |

Simple memory:

```text
Error metrics → lower is better
R² score → higher is better
```

---

## Slide 24: Python Code for Metrics

```python
import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

actual = [80, 100, 60, 120]
predicted = [75, 110, 65, 100]

mae = mean_absolute_error(actual, predicted)
mse = mean_squared_error(actual, predicted)
rmse = np.sqrt(mse)
r2 = r2_score(actual, predicted)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R2 Score:", r2)
```

---

## Slide 25: Expected Output Idea

```text
MAE: 10.0
MSE: 137.5
RMSE: 11.73
R2 Score: some value
```

Meaning:

```text
MAE = average mistake
MSE = squared mistake average
RMSE = bigger mistakes punished
R² = model quality compared to average prediction
```

---

## Slide 26: Metrics with Model Prediction

Typical workflow:

```python
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
```

Meaning:

```text
Train model
Predict test data
Compare actual y_test with predicted y_pred
Calculate metrics
```

---

## Slide 27: Best Order to Teach Beginners

For beginners, explain metrics in this order:

```text
1. MAE
2. RMSE
3. R²
4. MSE
```

Why?

MAE is easiest:

```text
Average mistake
```

RMSE is useful:

```text
Punishes big mistakes
```

R² is useful:

```text
How well model explains target
```

MSE is more mathematical:

```text
Used internally and for optimization
```

---

## Slide 28: Business Explanation Example

Suppose your model gives:

```text
MAE = 5 lakh
RMSE = 8 lakh
R² = 0.87
```

You can explain to client:

```text
On average, our model is wrong by around ₹5 lakh.
Because RMSE is ₹8 lakh, some larger mistakes exist.
R² of 0.87 means the model explains around 87% of price variation.
```

This is a strong trainer explanation.

---

## Slide 29: Final Summary

Remember:

```text
MAE = average absolute mistake
MSE = average squared mistake
RMSE = square root of MSE
R² = how well model explains target variation
```

Direction:

```text
MAE, MSE, RMSE → lower is better
R² → higher is better
```

---

## Slide 30: House Price Memory Hook

For house price:

```text
MAE = 10 means average error is ₹10 lakh.
RMSE = 11.73 means bigger mistakes are being punished.
R² = 0.85 means model explains 85% of variation.
```

Simple memory:

```text
MAE = average mistake
RMSE = serious mistake checker
R² = model explanation score
```

Next topic:

# Hands-on Regression Model Building Using Scikit-learn
