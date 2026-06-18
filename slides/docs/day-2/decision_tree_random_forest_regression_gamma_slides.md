# Decision Tree Regression & Random Forest Regression Overview

## Slide 1: Section Opening

# Decision Tree Regression & Random Forest Regression

### Moving beyond straight-line thinking

So far, we learned:

- Simple Linear Regression
- Multiple Linear Regression

Both try to learn a formula-based relationship.

Now we learn models that think like:

> **Questions → Conditions → Decisions → Prediction**

---

## Slide 2: Why Do We Need Tree-Based Models?

Linear Regression tries to learn one formula:

```text
Price = b0 + b1×Area + b2×Bedrooms + b3×Age + b4×Distance
```

This is useful when the relationship is roughly straight-line.

But real life often works like rules:

- If location is prime and area is big → very high price
- If location is far and house is old → low price
- If area is medium but near metro → good price
- If house is new but far from city → medium price

For this kind of logic, tree-based models are useful.

---

## Slide 3: What Is Decision Tree Regression?

# Simple Meaning

> **Decision Tree Regression predicts a number by asking a series of questions.**

It works like a flowchart.

Example:

```text
Is area greater than 1800 sqft?
    Yes → Is distance less than 5 km?
        Yes → Predict high price
        No  → Predict medium-high price
    No → Is house age less than 5 years?
        Yes → Predict medium price
        No  → Predict lower price
```

---

## Slide 4: Why Is It Called a Tree?

A decision tree has a tree-like structure.

```text
Root Question
    ├── Branch 1
    │       ├── Sub-branch
    │       └── Sub-branch
    └── Branch 2
            ├── Sub-branch
            └── Sub-branch
```

Example:

```text
Area > 1800?
    ├── Yes
    │     └── Distance < 5?
    │            ├── Yes → ₹130 lakh
    │            └── No  → ₹105 lakh
    └── No
          └── Age < 5?
                 ├── Yes → ₹80 lakh
                 └── No  → ₹55 lakh
```

Final prediction points are called **leaf nodes**.

---

## Slide 5: House Price Example

Sample data:

| Area | Bedrooms | Age | Distance | Price |
|---:|---:|---:|---:|---:|
| 900 | 2 | 10 | 12 | 42 |
| 1000 | 2 | 5 | 8 | 55 |
| 1500 | 3 | 3 | 5 | 82 |
| 1800 | 3 | 4 | 6 | 95 |
| 2000 | 4 | 2 | 4 | 120 |
| 2200 | 4 | 2 | 3 | 130 |
| 2500 | 4 | 1 | 2 | 155 |

A decision tree may learn rules like:

- If area > 1900 and distance <= 4 → high price
- If area <= 1200 and age > 5 → low price
- If area is between 1400 and 1900 → medium price

---

## Slide 6: Linear Regression vs Decision Tree

# Linear Regression Thinking

```text
Let me fit one best mathematical formula.
```

Example:

```text
Price = 10 + 0.04×Area + 5×Bedrooms - 1×Age - 2×Distance
```

# Decision Tree Thinking

```text
Let me ask questions and split the data into groups.
```

Example:

- Is area greater than 1800?
- Is distance less than 5?
- Is age less than 5?

---

## Slide 7: Real Estate Agent Analogy

A Linear Regression-style agent says:

- Every extra sqft adds around ₹4,000.
- Every extra bedroom adds around ₹5 lakh.
- Every extra km from city reduces ₹2 lakh.

A Decision Tree-style agent says:

- First check location.
- Then check area.
- Then check age.
- Then check distance.
- Based on the condition, estimate price.

Both are useful, but they think differently.

---

## Slide 8: Decision Tree Prediction Example

Suppose the tree learned this:

```text
Area > 1800?
    Yes:
        Distance < 5?
            Yes → Predict ₹130 lakh
            No  → Predict ₹105 lakh
    No:
        Age < 5?
            Yes → Predict ₹85 lakh
            No  → Predict ₹55 lakh
```

New house:

```text
Area = 2000
Distance = 4
Age = 3
```

Path:

```text
Area > 1800? Yes
Distance < 5? Yes
Prediction = ₹130 lakh
```

---

## Slide 9: Another Prediction Example

New house:

```text
Area = 1500
Distance = 6
Age = 3
```

Tree path:

```text
Area > 1800? No
Age < 5? Yes
Prediction = ₹85 lakh
```

This is how Decision Tree Regression predicts:

> It follows question paths until it reaches a final prediction.

---

## Slide 10: Strengths of Decision Tree Regression

Decision Tree Regression is useful because:

- Easy to understand
- Works with non-linear patterns
- Captures rule-based behavior
- Does not usually require feature scaling
- Handles complex conditions

Example:

House price may suddenly increase when:

```text
Distance to metro < 1 km
```

A tree can capture this kind of condition well.

---

## Slide 11: Weakness of Decision Tree Regression

The major weakness:

# It can overfit.

Overfitting means:

> The model memorizes training data too much and performs poorly on new data.

Example:

```text
If area = 1500 and age = 3 and distance = 5 → ₹82 lakh
If area = 1510 and age = 3 and distance = 5.2 → ₹83 lakh
If area = 1520 and age = 4 and distance = 5.1 → ₹81 lakh
```

Too many tiny rules can make the tree weak on new data.

---

## Slide 12: Decision Tree Regression Code

```python
import pandas as pd
from sklearn.tree import DecisionTreeRegressor

data = {
    "area": [900, 1000, 1500, 1800, 2000, 2200, 2500],
    "bedrooms": [2, 2, 3, 3, 4, 4, 4],
    "age": [10, 5, 3, 4, 2, 2, 1],
    "distance": [12, 8, 5, 6, 4, 3, 2],
    "price": [42, 55, 82, 95, 120, 130, 155]
}

df = pd.DataFrame(data)

X = df[["area", "bedrooms", "age", "distance"]]
y = df["price"]

model = DecisionTreeRegressor(random_state=42)
model.fit(X, y)
```

---

## Slide 13: Decision Tree Prediction Code

```python
new_house = pd.DataFrame({
    "area": [1700],
    "bedrooms": [3],
    "age": [4],
    "distance": [6]
})

prediction = model.predict(new_house)

print("Predicted price:", prediction[0], "lakhs")
```

Important idea:

```text
DecisionTreeRegressor = Decision Tree model for predicting numbers
```

---

## Slide 14: What Is Random Forest Regression?

# Simple Meaning

> **Random Forest Regression combines many Decision Trees and averages their predictions.**

One decision tree can overfit.

So Random Forest says:

```text
Instead of trusting one tree, let many trees work together.
```

For regression:

- Each tree predicts a number.
- Final prediction is the average.

---

## Slide 15: Why Is It Called Random Forest?

```text
Forest = many trees
Random = each tree is trained slightly differently
```

So:

```text
Decision Tree = one tree
Random Forest = many decision trees
```

Example:

```text
Tree 1 predicts ₹85 lakh
Tree 2 predicts ₹88 lakh
Tree 3 predicts ₹82 lakh
Tree 4 predicts ₹90 lakh
Tree 5 predicts ₹86 lakh
```

Final prediction:

```text
Average = ₹86.2 lakh
```

---

## Slide 16: Random Forest Analogy

Imagine estimating a house price.

You ask one real estate agent:

```text
₹90 lakh
```

But one agent may be biased.

Now you ask 10 agents:

```text
Agent 1: ₹85 lakh
Agent 2: ₹88 lakh
Agent 3: ₹92 lakh
Agent 4: ₹86 lakh
Agent 5: ₹89 lakh
```

You take the average.

That is Random Forest thinking.

```text
Decision Tree = one expert
Random Forest = group of experts
```

---

## Slide 17: Random Forest Prediction Example

Suppose 5 trees predict:

| Tree | Prediction |
|---|---:|
| Tree 1 | ₹80 lakh |
| Tree 2 | ₹85 lakh |
| Tree 3 | ₹82 lakh |
| Tree 4 | ₹86 lakh |
| Tree 5 | ₹87 lakh |

Average:

```text
(80 + 85 + 82 + 86 + 87) / 5 = 84
```

Final prediction:

```text
₹84 lakh
```

---

## Slide 18: Why Random Forest Is Powerful

Random Forest is popular because:

- Usually performs better than a single decision tree
- Reduces overfitting
- Handles non-linear relationships
- Works well with many features
- Gives feature importance
- Useful for regression and classification

It can capture complex relationships like:

- Area matters more in some locations
- Distance matters more for premium properties
- Age matters differently based on construction quality

---

## Slide 19: Random Forest Regression Code

```python
import pandas as pd
from sklearn.ensemble import RandomForestRegressor

data = {
    "area": [900, 1000, 1500, 1800, 2000, 2200, 2500],
    "bedrooms": [2, 2, 3, 3, 4, 4, 4],
    "age": [10, 5, 3, 4, 2, 2, 1],
    "distance": [12, 8, 5, 6, 4, 3, 2],
    "price": [42, 55, 82, 95, 120, 130, 155]
}

df = pd.DataFrame(data)

X = df[["area", "bedrooms", "age", "distance"]]
y = df["price"]

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)
```

---

## Slide 20: Random Forest Prediction Code

```python
new_house = pd.DataFrame({
    "area": [1700],
    "bedrooms": [3],
    "age": [4],
    "distance": [6]
})

prediction = model.predict(new_house)

print("Predicted price:", prediction[0], "lakhs")
```

Important parameter:

```text
n_estimators=100
```

Meaning:

```text
Build 100 decision trees.
```

---

## Slide 21: Decision Tree vs Random Forest

| Point | Decision Tree Regression | Random Forest Regression |
|---|---|---|
| Model type | One tree | Many trees |
| Prediction | One tree output | Average of many tree outputs |
| Interpretability | Easy | Medium |
| Overfitting risk | Higher | Lower |
| Accuracy | Good | Often better |
| Speed | Faster | Slower than one tree |
| Stability | Less stable | More stable |

---

## Slide 22: Linear Regression vs Tree Models

| Point | Linear Regression | Decision Tree / Random Forest |
|---|---|---|
| Relationship | Straight-line assumption | Rule-based splits |
| Explainability | Formula-based | Tree/rule-based |
| Handles non-linear patterns | Limited | Better |
| Good for beginners | Yes | Yes |
| Overfitting risk | Usually lower | Tree can overfit |
| Real-world performance | Good baseline | Often stronger |

---

## Slide 23: When to Use Linear Regression

Use Linear Regression when:

- You want a simple explainable formula
- Relationship looks roughly linear
- You want to understand feature direction
- Data is not too complex

Examples:

- Experience → Salary
- Area → Price
- Ad spend → Sales

---

## Slide 24: When to Use Decision Tree

Use Decision Tree when:

- You want rule-based explanation
- Data has non-linear conditions
- You want simple visual decision logic

Example:

```text
If income > X and credit score > Y → loan amount estimate
```

Decision Tree is useful when business logic feels like conditions and branches.

---

## Slide 25: When to Use Random Forest

Use Random Forest when:

- You want stronger performance
- You have many features
- Relationships are complex
- You want to reduce overfitting compared to one tree

Examples:

- House price prediction with many property features
- Sales prediction with seasonality, discount, region, product category
- Delivery time prediction with traffic, weather, and distance

---

## Slide 26: Common Confusion 1

# Is Decision Tree only for classification?

No.

Decision Trees can be used for both:

```text
Classification → predicts category
Regression → predicts number
```

For regression:

```python
DecisionTreeRegressor
```

For classification:

```python
DecisionTreeClassifier
```

---

## Slide 27: Common Confusion 2

# Does Random Forest always give perfect results?

No.

Random Forest is powerful, but not magic.

It still needs:

- Good data
- Relevant features
- Enough examples
- Proper evaluation
- Correct train-test split

Bad data can still produce a bad model.

---

## Slide 28: Common Confusion 3

# Is Random Forest always better than Linear Regression?

Not always.

If the relationship is simple and linear, Linear Regression may work very well.

Random Forest is often better when patterns are complex.

Simple idea:

```text
Simple pattern → Linear Regression may be enough
Complex pattern → Random Forest may help
```

---

## Slide 29: Final Summary

Remember this:

```text
Decision Tree Regression = predicts a number using decision rules.
Random Forest Regression = many decision trees together, final prediction is average.
```

For house price:

```text
Decision Tree:
Ask questions like area > 1800, distance < 5, age < 5.

Random Forest:
Ask many trees and average their answers.
```

---

## Slide 30: Memory Hook

```text
Linear Regression = formula thinking
Decision Tree = flowchart thinking
Random Forest = group of flowcharts
```

Next topic:

# Regression Evaluation Metrics

We will learn:

- MAE
- MSE
- RMSE
- R² Score
