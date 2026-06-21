# Regression Models Overview

## From Linear Family to Tree-Based and Advanced Regression

---

## Slide 1: Title

# Regression Models Overview

### Remaining important regression models before moving to Classification

---

## Slide 2: Where We Are

Completed:

| Model                      | Status |
| -------------------------- | ------ |
| Simple Linear Regression   | Done   |
| Multiple Linear Regression | Done   |

Now we will overview the remaining regression models.

---

## Slide 3: Regression Model Roadmap

| Family             | Models                                         |
| ------------------ | ---------------------------------------------- |
| Linear Family      | Polynomial, Ridge, Lasso, Elastic Net          |
| Tree Family        | Decision Tree, Random Forest                   |
| Boosting Family    | Gradient Boosting, XGBoost, LightGBM, CatBoost |
| Distance / Margin  | KNN, SVR                                       |
| Special Regression | Robust, Quantile, Bayesian                     |

---

## Slide 4: Model 3 — Polynomial Regression

Purpose:

Handles curved relationships.

Example:

Study hours improve score quickly at first, but later improvement slows down.

Formula:

ŷ = b₀ + b₁x + b₂x²

Simple Linear Regression learns a line.

Polynomial Regression learns a curve.

---

## Slide 5: Polynomial Regression Example

| Study Hours | Score Pattern           |
| ----------: | ----------------------- |
|   1–3 hours | Score improves fast     |
|   4–6 hours | Score improves steadily |
|  7–10 hours | Score improvement slows |

Use when:

Relationship is not straight.

---

## Slide 6: Polynomial Regression Caution

Polynomial Regression can overfit.

Low degree:

May underfit.

High degree:

May overfit.

Rule:

Use the smallest degree that captures the pattern well.

---

## Slide 7: Model 4 — Ridge Regression

Purpose:

Controls overfitting.

Ridge adds penalty to large coefficients.

Main idea:

Keep all features, but reduce coefficient size.

Formula idea:

Loss = MSE + L2 penalty

Use when:

Many features are useful but coefficients are becoming too large.

---

## Slide 8: Ridge Regression Intuition

Without Ridge:

Model may depend too strongly on some features.

With Ridge:

Model becomes more balanced.

Good for:

* Multicollinearity
* Many features
* Reducing overfitting

---

## Slide 9: Model 5 — Lasso Regression

Purpose:

Feature selection.

Lasso can shrink some coefficients to exactly zero.

Formula idea:

Loss = MSE + L1 penalty

Use when:

You want the model to automatically remove weak or useless features.

---

## Slide 10: Lasso Regression Example

Before Lasso:

| Feature        | Coefficient |
| -------------- | ----------: |
| Study Hours    |         2.1 |
| Attendance     |         0.4 |
| Shoe Size      |        0.02 |
| Favorite Color |        0.01 |

After Lasso:

| Feature        | Coefficient |
| -------------- | ----------: |
| Study Hours    |         2.0 |
| Attendance     |         0.3 |
| Shoe Size      |           0 |
| Favorite Color |           0 |

---

## Slide 11: Ridge vs Lasso

| Model | Main Effect                       |
| ----- | --------------------------------- |
| Ridge | Shrinks coefficients              |
| Lasso | Shrinks some coefficients to zero |

Ridge keeps features.

Lasso can remove features.

---

## Slide 12: Model 6 — Elastic Net

Purpose:

Combines Ridge and Lasso.

Elastic Net uses:

L1 penalty + L2 penalty

Meaning:

It can reduce coefficient size and remove weak features.

Use when:

You want a balance between Ridge and Lasso.

---

## Slide 13: Elastic Net Use Case

Good when:

* Many features exist
* Some features are correlated
* Some features may be useless
* You want both stability and feature selection

Elastic Net is often safer than pure Lasso when features are highly correlated.

---

## Slide 14: Linear Family Summary

| Model       | Best For              |
| ----------- | --------------------- |
| Polynomial  | Curved patterns       |
| Ridge       | Overfitting control   |
| Lasso       | Feature selection     |
| Elastic Net | Ridge + Lasso balance |

---

## Slide 15: Section Divider

# Tree-Based Regression

Models that learn rules instead of equations.

---

## Slide 16: Model 7 — Decision Tree Regressor

Purpose:

Predict numbers using decision rules.

Example:

If study hours > 6 and attendance > 80, predict high score.

Tree models split data into smaller groups.

---

## Slide 17: Decision Tree Example

| Rule            | Prediction |
| --------------- | ---------: |
| Study Hours ≤ 3 |         50 |
| Study Hours 4–6 |         68 |
| Study Hours > 6 |         85 |

Decision Tree predicts using average target values inside each group.

---

## Slide 18: Decision Tree Strengths

Good for:

* Nonlinear patterns
* Feature interactions
* Easy explanation
* No scaling required
* Mixed feature types after encoding

Weakness:

Can overfit easily.

---

## Slide 19: Model 8 — Random Forest Regressor

Purpose:

Improve Decision Tree by using many trees.

Random Forest = collection of decision trees.

Final prediction:

Average of many tree predictions.

This usually improves stability and accuracy.

---

## Slide 20: Random Forest Intuition

One tree may overfit.

Many trees together reduce overfitting.

Example:

| Tree   | Prediction |
| ------ | ---------: |
| Tree 1 |         76 |
| Tree 2 |         78 |
| Tree 3 |         75 |
| Tree 4 |         79 |

Final prediction:

Average = 77

---

## Slide 21: Random Forest Strengths

Good for:

* Nonlinear data
* Many features
* Robust predictions
* Feature importance
* Less tuning than boosting

Weakness:

Less interpretable than a single tree.

---

## Slide 22: Tree Family Summary

| Model         | Main Idea           |
| ------------- | ------------------- |
| Decision Tree | One rule-based tree |
| Random Forest | Many trees averaged |

Decision Tree is simple.

Random Forest is stronger.

---

## Slide 23: Section Divider

# Boosting Regression

Models that learn from previous mistakes.

---

## Slide 24: Model 9 — Gradient Boosting Regressor

Purpose:

Build trees sequentially.

Each new tree tries to correct previous errors.

Main idea:

Tree 1 makes prediction.

Tree 2 learns from Tree 1’s mistakes.

Tree 3 learns from remaining mistakes.

---

## Slide 25: Boosting Intuition

Suppose model prediction error remains:

| Stage       | What Happens              |
| ----------- | ------------------------- |
| First tree  | Learns main pattern       |
| Second tree | Corrects remaining errors |
| Third tree  | Corrects smaller errors   |
| Final model | Combines all trees        |

Boosting is powerful but needs careful tuning.

---

## Slide 26: Model 10 — XGBoost Regressor

Purpose:

High-performance boosting model.

XGBoost is widely used in competitions and industry.

Good for:

* Tabular data
* Structured business data
* High accuracy
* Feature importance

---

## Slide 27: XGBoost Strengths

XGBoost handles:

* Nonlinear patterns
* Missing values
* Feature interactions
* Regularization
* Large datasets

It is often stronger than Random Forest on structured datasets.

---

## Slide 28: LightGBM Regressor

Purpose:

Fast gradient boosting.

LightGBM is designed for speed and large datasets.

Good for:

* Large tabular data
* Many rows
* Many features
* Faster training

---

## Slide 29: CatBoost Regressor

Purpose:

Boosting model strong with categorical features.

CatBoost is useful when dataset has many category columns.

Examples:

* City
* Product category
* Department
* Customer segment

It reduces preprocessing burden for categorical data.

---

## Slide 30: Boosting Models Summary

| Model             | Best For                       |
| ----------------- | ------------------------------ |
| Gradient Boosting | Conceptual boosting foundation |
| XGBoost           | High accuracy on tabular data  |
| LightGBM          | Large and fast datasets        |
| CatBoost          | Categorical-heavy datasets     |

---

## Slide 31: Section Divider

# Distance and Margin-Based Regression

Alternative ways to predict numbers.

---

## Slide 32: Model 11 — KNN Regressor

Purpose:

Predict based on nearby examples.

KNN means:

K-Nearest Neighbors.

Prediction is usually the average of nearby target values.

---

## Slide 33: KNN Example

New student:

Study Hours = 6

Nearest students:

| Neighbor | Study Hours | Score |
| -------- | ----------: | ----: |
| A        |         5.5 |    70 |
| B        |         6.0 |    72 |
| C        |         6.5 |    75 |

Prediction:

Average = 72.3

---

## Slide 34: KNN Strengths and Weaknesses

Strengths:

* Simple idea
* No training complexity
* Can capture nonlinear patterns

Weaknesses:

* Needs scaling
* Slow for large data
* Sensitive to irrelevant features
* Choosing K is important

---

## Slide 35: Model 12 — Support Vector Regression

Purpose:

Predict using margin-based thinking.

SVR tries to fit a function where errors inside a margin are tolerated.

Useful when:

* Dataset is smaller
* Relationship may be nonlinear
* Need robust boundary-like fitting

---

## Slide 36: SVR Intuition

SVR does not try to perfectly fit every point.

It creates a tube around the prediction line.

Errors inside the tube are acceptable.

Errors outside the tube are penalized.

---

## Slide 37: SVR Strengths and Weaknesses

Strengths:

* Works well on smaller datasets
* Can model nonlinear patterns with kernels
* Robust margin idea

Weaknesses:

* Needs scaling
* Harder to explain
* Can be slow on large data
* Parameter tuning matters

---

## Slide 38: Section Divider

# Special Regression Models

Used for specific needs.

---

## Slide 39: Model 13 — Robust Regression

Purpose:

Handle outliers better than ordinary Linear Regression.

Problem:

Linear Regression is sensitive to extreme values.

Robust Regression reduces the effect of outliers.

---

## Slide 40: Robust Regression Example

Dataset issue:

| Study Hours | Score |
| ----------: | ----: |
|           2 |    45 |
|           3 |    50 |
|           4 |    58 |
|           5 |    64 |
|          10 |    20 |

The last point is an outlier.

Robust Regression is less affected by it.

---

## Slide 41: Model 14 — Quantile Regression

Purpose:

Predict percentiles instead of only average.

Normal regression predicts expected average value.

Quantile Regression can predict:

* 25th percentile
* 50th percentile
* 75th percentile
* 90th percentile

Useful when risk or range matters.

---

## Slide 42: Quantile Regression Example

House price prediction:

| Prediction Type | Meaning                  |
| --------------- | ------------------------ |
| 50th percentile | Typical expected price   |
| 90th percentile | High-end possible price  |
| 10th percentile | Lower-end possible price |

Useful for uncertainty-aware business decisions.

---

## Slide 43: Model 15 — Bayesian Regression

Purpose:

Regression with uncertainty.

Instead of giving only one coefficient estimate, Bayesian Regression gives probability-based understanding.

Useful when:

* Data is limited
* Uncertainty matters
* You want confidence in predictions

---

## Slide 44: Bayesian Regression Output

Normal regression:

Prediction = 76

Bayesian regression:

Prediction likely around 76, with uncertainty range.

Example:

Expected score = 76
Possible range = 72 to 80

This is useful when confidence matters.

---

## Slide 45: Complete Regression Model Map

| Family            | Models                                         |
| ----------------- | ---------------------------------------------- |
| Linear Extensions | Polynomial, Ridge, Lasso, Elastic Net          |
| Tree-Based        | Decision Tree, Random Forest                   |
| Boosting          | Gradient Boosting, XGBoost, LightGBM, CatBoost |
| Distance / Margin | KNN, SVR                                       |
| Special           | Robust, Quantile, Bayesian                     |

---

## Slide 46: Which Model to Try First?

| Situation                  | Good Starting Model           |
| -------------------------- | ----------------------------- |
| Simple linear pattern      | Linear Regression             |
| Curved pattern             | Polynomial Regression         |
| Many features, overfitting | Ridge / Lasso                 |
| Nonlinear rules            | Decision Tree                 |
| Strong general model       | Random Forest                 |
| Best tabular accuracy      | XGBoost / LightGBM / CatBoost |

---

## Slide 47: Interpretability vs Accuracy

| Model             | Interpretability | Accuracy Potential |
| ----------------- | ---------------- | ------------------ |
| Linear Regression | High             | Medium             |
| Ridge / Lasso     | High             | Medium             |
| Decision Tree     | Medium-High      | Medium             |
| Random Forest     | Medium           | High               |
| Boosting Models   | Lower            | Very High          |
| SVR               | Lower            | Medium-High        |

---

## Slide 48: Scaling Requirement

| Model                  | Scaling Needed? |
| ---------------------- | --------------- |
| Linear / Ridge / Lasso | Recommended     |
| KNN                    | Required        |
| SVR                    | Required        |
| Decision Tree          | Usually no      |
| Random Forest          | Usually no      |
| Boosting Trees         | Usually no      |

---

## Slide 49: Handling Outliers

| Model                 | Outlier Sensitivity   |
| --------------------- | --------------------- |
| Linear Regression     | High                  |
| Polynomial Regression | High                  |
| Ridge / Lasso         | Medium                |
| Decision Tree         | Medium                |
| Random Forest         | Lower                 |
| Robust Regression     | Designed for outliers |

---

## Slide 50: Handling Nonlinearity

| Model                 | Handles Nonlinearity?        |
| --------------------- | ---------------------------- |
| Linear Regression     | No                           |
| Polynomial Regression | Yes, manually through powers |
| Decision Tree         | Yes                          |
| Random Forest         | Yes                          |
| Boosting Models       | Yes                          |
| KNN                   | Yes                          |
| SVR with kernel       | Yes                          |

---

## Slide 51: Common Regression Workflow

1. Understand problem
2. Identify target and features
3. Clean data
4. Split train/test
5. Start with baseline model
6. Evaluate MAE, RMSE, R²
7. Try stronger models
8. Compare results
9. Check overfitting
10. Explain final model

---

## Slide 52: Baseline First

Before advanced models, create a simple baseline.

Example baseline:

Predict average score for all students.

Then ask:

Does our ML model perform better than this baseline?

If not, model is not useful.

---

## Slide 53: Model Selection Mindset

Do not ask:

Which model is always best?

Ask:

Which model fits this dataset, business goal, and explanation need?

Best model depends on:

* Data size
* Feature quality
* Nonlinearity
* Outliers
* Need for explanation
* Accuracy requirement

---

## Slide 54: Regression Model Summary

| Model         | One-Line Meaning            |
| ------------- | --------------------------- |
| Polynomial    | Learns curve                |
| Ridge         | Controls large coefficients |
| Lasso         | Selects features            |
| Elastic Net   | Ridge + Lasso               |
| Decision Tree | Learns rules                |
| Random Forest | Averages many trees         |
| Boosting      | Learns from mistakes        |
| KNN           | Uses nearby examples        |
| SVR           | Uses margin tube            |
| Robust        | Handles outliers            |
| Quantile      | Predicts percentiles        |
| Bayesian      | Adds uncertainty            |

---

## Slide 55: Final Takeaway

Regression is not one model.

Regression is a family of models for numeric prediction.

The goal is always:

Learn from past data → Predict a numeric value → Minimize error

Next major ML family:

Classification Models
