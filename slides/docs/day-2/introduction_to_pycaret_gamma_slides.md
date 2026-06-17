# Introduction to PyCaret

## Slide 1: Section Opening

# Introduction to PyCaret

### Low-code machine learning for faster experiments

Until now, we built regression models manually using **Scikit-learn**.

We manually handled:

- Importing libraries
- Creating the dataset
- Separating X and y
- Train-test split
- Creating models
- Training models
- Predicting
- Evaluating metrics
- Comparing models manually

Now we learn **PyCaret**.

---

## Slide 2: What Is PyCaret?

PyCaret is a low-code Machine Learning library in Python.

Simple meaning:

> **PyCaret helps us build, compare, tune, evaluate, and save ML models quickly with less code.**

It helps automate repeated ML workflow steps.

Instead of writing many lines for many models, PyCaret can do model comparison quickly.

---

## Slide 3: Why Do We Need PyCaret?

In Scikit-learn, if we want to compare multiple models, we write separate code for each model.

Examples:

- Linear Regression
- Decision Tree Regression
- Random Forest Regression
- KNN Regression
- Ridge Regression
- Lasso Regression
- Gradient Boosting Regression

For each model, we manually do:

```text
Create model
Train model
Predict
Evaluate MAE
Evaluate RMSE
Evaluate R²
Store results
Compare results
```

This takes time.

PyCaret makes this faster.

---

## Slide 4: Scikit-learn Style

In Scikit-learn, we manually create and train a model.

```python
model = LinearRegression()
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
```

Then we manually calculate metrics.

```python
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
```

This gives full control and strong learning.

---

## Slide 5: PyCaret Style

In PyCaret, we can compare many models automatically.

```python
best_model = compare_models()
```

This single function can try many regression models and show a comparison table.

That is why PyCaret is useful for quick experimentation.

---

## Slide 6: Simple Analogy

# Scikit-learn = Manual Car

You control:

- Clutch
- Gear
- Brake
- Accelerator
- Steering

You understand every action clearly.

# PyCaret = Automatic Car

It handles many repeated steps for you.

But you should first understand manual driving.

Similarly:

> **Learn Scikit-learn basics first. Then PyCaret becomes meaningful.**

---

## Slide 7: Where PyCaret Fits in ML Learning

Best learning path:

```text
ML concepts
        ↓
Scikit-learn implementation
        ↓
Model evaluation
        ↓
PyCaret automation
```

Why?

PyCaret automates tasks that you should first understand manually.

If you know these basics, PyCaret becomes easy:

- Features and target
- Train-test split
- Regression
- Metrics
- Model comparison

---

## Slide 8: What Can PyCaret Do?

PyCaret can help with:

- Experiment setup
- Data preprocessing
- Model comparison
- Model creation
- Model tuning
- Model evaluation
- Prediction
- Model saving and loading

Simple memory:

```text
PyCaret reduces boilerplate ML code.
```

---

## Slide 9: Our Running Example

We continue with the same house price problem.

Dataset columns:

- Area
- Bedrooms
- Age
- Distance
- Price

Goal:

```text
Predict price
```

Because price is a number:

```text
This is a regression problem.
```

---

## Slide 10: House Price Dataset

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

## Slide 11: PyCaret Basic Workflow

PyCaret regression workflow usually follows this pattern:

```text
Step 1: Import PyCaret regression module
Step 2: Setup experiment
Step 3: Compare models
Step 4: Create selected model
Step 5: Tune model
Step 6: Evaluate model
Step 7: Predict on new data
Step 8: Save model
```

Short memory:

```text
setup → compare → create/tune → evaluate → predict → save
```

---

## Slide 12: Step 1 — Import PyCaret

For regression:

```python
from pycaret.regression import *
```

This imports regression-related PyCaret functions.

Examples:

- `setup`
- `compare_models`
- `create_model`
- `tune_model`
- `evaluate_model`
- `predict_model`
- `save_model`
- `load_model`

---

## Slide 13: Step 2 — Setup Experiment

```python
s = setup(
    data=df,
    target="price",
    session_id=42
)
```

Meaning:

```text
data = full dataframe
target = column we want to predict
session_id = fixed randomness for reproducibility
```

In PyCaret, `setup()` prepares the ML experiment.

---

## Slide 14: Why setup() Is Important

In Scikit-learn, we manually did:

- Separate X and y
- Train-test split
- Some preprocessing
- Model preparation

In PyCaret, `setup()` starts the experiment.

It tells PyCaret:

```text
This is my dataset.
This is the target column.
Prepare the experiment for regression.
```

So `setup()` is the starting point.

---

## Slide 15: Step 3 — Compare Models

```python
best_model = compare_models()
```

This is one of PyCaret’s most useful functions.

It compares many regression models and returns the best one based on a selected metric.

The output usually includes metrics like:

- MAE
- MSE
- RMSE
- R²
- RMSLE
- MAPE

---

## Slide 16: What compare_models() Does

When you run:

```python
best_model = compare_models()
```

PyCaret may try models like:

- Linear Regression
- Ridge Regression
- Lasso Regression
- Decision Tree
- Random Forest
- Extra Trees
- Gradient Boosting
- KNN
- AdaBoost

Then it shows which model performed better.

---

## Slide 17: Why compare_models() Is Powerful

Without PyCaret, you manually write code for each model.

With PyCaret:

```python
best_model = compare_models()
```

This can create a model leaderboard automatically.

Trainer explanation:

> **compare_models() is useful for quickly finding a strong baseline model.**

---

## Slide 18: Step 4 — Create a Specific Model

Sometimes you may not want automatic best model.

You may want a specific model.

Example: Linear Regression

```python
lr_model = create_model("lr")
```

Example: Random Forest

```python
rf_model = create_model("rf")
```

Here:

```text
"lr" = Linear Regression
"rf" = Random Forest
```

---

## Slide 19: What create_model() Does

When you run:

```python
rf_model = create_model("rf")
```

PyCaret:

- Creates the selected model
- Trains it
- Evaluates it
- Shows performance metrics

It reduces repeated model-building code.

---

## Slide 20: Step 5 — Tune Model

```python
tuned_model = tune_model(rf_model)
```

Tuning means:

> **Trying better internal settings to improve model performance.**

Example Random Forest settings:

- Number of trees
- Maximum tree depth
- Minimum samples per split
- Minimum samples per leaf

---

## Slide 21: Why Tuning Matters

Default model settings are not always best.

Example:

Random Forest can change:

```text
Number of trees
Tree depth
Samples per split
Samples per leaf
```

In Scikit-learn, we may tune manually or use tools like GridSearchCV.

PyCaret simplifies this.

---

## Slide 22: Step 6 — Evaluate Model

```python
evaluate_model(tuned_model)
```

This helps inspect the model visually.

For regression, evaluation may include:

- Residual plots
- Prediction error plots
- Feature importance
- Learning curves

This is useful for understanding model behavior.

---

## Slide 23: Step 7 — Predict Using Model

To predict on test/holdout data:

```python
predictions = predict_model(tuned_model)
```

To predict on new data:

```python
new_house = pd.DataFrame({
    "area": [1700],
    "bedrooms": [3],
    "age": [4],
    "distance": [6]
})

new_prediction = predict_model(tuned_model, data=new_house)
```

This gives predicted price for the new house.

---

## Slide 24: Step 8 — Save Model

After training a good model, save it:

```python
save_model(tuned_model, "house_price_model")
```

Later, load it:

```python
loaded_model = load_model("house_price_model")
```

Why save?

```text
So we do not need to train the model again every time.
```

---

## Slide 25: Full PyCaret Example — Part 1

```python
import pandas as pd
from pycaret.regression import *

data = {
    "area": [900, 1000, 1200, 1500, 1600, 1800, 2000, 2200, 2500, 2800],
    "bedrooms": [2, 2, 2, 3, 3, 3, 4, 4, 4, 5],
    "age": [10, 8, 6, 5, 4, 7, 3, 2, 5, 1],
    "distance": [12, 10, 9, 7, 6, 8, 5, 4, 6, 3],
    "price": [45, 52, 58, 72, 78, 85, 105, 120, 135, 160]
}

df = pd.DataFrame(data)
```

---

## Slide 26: Full PyCaret Example — Part 2

```python
s = setup(
    data=df,
    target="price",
    session_id=42
)

best_model = compare_models()
```

Meaning:

```text
setup() prepares the experiment.
compare_models() compares many regression models.
```

---

## Slide 27: Full PyCaret Example — Part 3

```python
predictions = predict_model(best_model)

new_house = pd.DataFrame({
    "area": [1700],
    "bedrooms": [3],
    "age": [4],
    "distance": [6]
})

new_prediction = predict_model(best_model, data=new_house)

print(new_prediction)
```

This predicts price for a new house.

---

## Slide 28: Full PyCaret Example — Part 4

```python
save_model(best_model, "house_price_model")
```

This saves the trained model.

Later:

```python
loaded_model = load_model("house_price_model")
```

This loads the model again for future use.

---

## Slide 29: Important Warning About Small Datasets

Our example has only 10 rows.

That is fine for learning.

But in real ML projects, 10 rows is not enough.

For serious model building, we need much more data.

Examples:

- Hundreds of rows
- Thousands of rows
- Lakhs of records

With very small data, model comparison results may not be reliable.

---

## Slide 30: PyCaret Version Note

PyCaret has evolved across versions.

For corporate training, decide the environment version before the lab.

Keep all participants on the same setup:

```text
Same Python version
Same PyCaret version
Same notebook/lab environment
```

This avoids installation and compatibility issues.

---

## Slide 31: PyCaret vs Scikit-learn

| Point | Scikit-learn | PyCaret |
|---|---|---|
| Coding style | Manual | Low-code |
| Best for | Learning fundamentals | Fast experiments |
| Model comparison | Manual | Automatic |
| Control | More control | Less manual control |
| Beginner learning | Very important | After basics |
| Production understanding | Strong foundation | Useful acceleration |

---

## Slide 32: When Should We Use PyCaret?

Use PyCaret when:

- You want to quickly test many models
- You want a fast baseline
- You want quick model comparison
- You are doing early experimentation
- You want less boilerplate code

PyCaret is very useful during the experimentation phase.

---

## Slide 33: When Not to Depend Only on PyCaret

Avoid depending only on PyCaret when:

- You do not understand ML basics
- You need full custom control
- You need deeply customized production pipelines
- You need to explain every preprocessing step manually

Trainer message:

> **PyCaret is a helper, not a replacement for ML understanding.**

---

## Slide 34: Final Summary

Remember:

```text
PyCaret = low-code ML experimentation tool
```

Scikit-learn:

```text
Manual ML coding
```

PyCaret:

```text
Automated ML workflow
```

Core PyCaret flow:

```text
setup → compare_models → create_model → tune_model → evaluate_model → predict_model → save_model
```

---

## Slide 35: Memory Hook

```text
Scikit-learn teaches you how ML works.
PyCaret helps you move faster after you understand ML basics.
```

Simple comparison:

```text
Scikit-learn = manual learning
PyCaret = fast experimentation
```

Next topic:

# PyCaret Installation and Environment Setup
