# Model 2: Multiple Linear Regression — Gamma Slide Deck

## Slide 1: Title

# Multiple Linear Regression

### Predicting one numeric value using many input features

---

## Slide 2: Learning Path

# What Students Will Learn

* Why one feature is not enough
* Multiple Linear Regression formula
* Meaning of coefficients
* Prediction calculation
* Training objective
* Evaluation metrics
* Train-test split
* Scaling, multicollinearity, encoding, interactions

---

## Slide 3: Section Divider

# Part 1

## Foundation

From one input to many inputs.

---

## Slide 4: Quick Recap

# Simple Linear Regression

Simple Linear Regression uses one feature.

Formula:

ŷ = mx + c

Example:

Predicted Score = m × Study Hours + c

---

## Slide 5: Why Multiple Regression?

# Real Life Has Many Reasons

A student’s score may depend on:

| Factor         |
| -------------- |
| Study Hours    |
| Attendance     |
| Previous Score |
| Sleep Hours    |
| Practice Tests |

One feature is often not enough.

---

## Slide 6: Core Idea

# Many Inputs → One Prediction

Multiple Linear Regression predicts one numeric target using multiple features.

Example:

Study Hours + Attendance + Previous Score + Sleep Hours → Final Score

---

## Slide 7: Example Problem

# Predict Final Exam Score

Question:

Can we predict a student’s final exam score using academic and lifestyle factors?

| Role     | Column                                               |
| -------- | ---------------------------------------------------- |
| Target   | Final Score                                          |
| Features | Study Hours, Attendance, Previous Score, Sleep Hours |

---

## Slide 8: Example Dataset

| Student | Study Hours | Attendance | Previous Score | Sleep Hours | Final Score |
| ------- | ----------: | ---------: | -------------: | ----------: | ----------: |
| A       |           2 |         60 |             40 |           5 |          48 |
| B       |           3 |         70 |             45 |           6 |          55 |
| C       |           4 |         65 |             50 |           6 |          59 |
| D       |           5 |         80 |             55 |           7 |          68 |
| E       |           6 |         75 |             60 |           7 |          72 |

---

## Slide 9: Feature and Target

| Column         | Role    |
| -------------- | ------- |
| Study Hours    | Feature |
| Attendance     | Feature |
| Previous Score | Feature |
| Sleep Hours    | Feature |
| Final Score    | Target  |

Features are inputs.

Target is what we want to predict.

---

## Slide 10: Simple vs Multiple Regression

| Model                      |  Features | Formula                    |
| -------------------------- | --------: | -------------------------- |
| Simple Linear Regression   |         1 | ŷ = mx + c                 |
| Multiple Linear Regression | 2 or more | ŷ = b₀ + b₁x₁ + b₂x₂ + ... |

Same idea.

More features.

More coefficients.

---

## Slide 11: Section Divider

# Part 2

## Formula and Prediction

Understanding the equation clearly.

---

## Slide 12: Main Formula

Formula:

ŷ = b₀ + b₁x₁ + b₂x₂ + b₃x₃ + b₄x₄

For student score:

Predicted Score
= b₀

* b₁(Study Hours)
* b₂(Attendance)
* b₃(Previous Score)
* b₄(Sleep Hours)

---

## Slide 13: Formula Symbols

| Symbol | Meaning                   |
| ------ | ------------------------- |
| ŷ      | Predicted value           |
| b₀     | Intercept / bias          |
| b₁     | Coefficient for feature 1 |
| b₂     | Coefficient for feature 2 |
| x₁     | Feature 1                 |
| x₂     | Feature 2                 |

Each feature gets its own coefficient.

---

## Slide 14: Different Names

| Concept    | Other Names                             |
| ---------- | --------------------------------------- |
| b₀         | Intercept, bias, constant               |
| b₁, b₂, b₃ | Coefficients, weights, slopes           |
| x₁, x₂, x₃ | Features, inputs, independent variables |
| y          | Target, output, dependent variable      |
| ŷ          | Prediction, estimated value             |

---

## Slide 15: Example Learned Model

Suppose the model learns:

Predicted Score
= 5

* 2.5(Study Hours)
* 0.2(Attendance)
* 0.5(Previous Score)
* 1.5(Sleep Hours)

This formula combines many feature contributions.

---

## Slide 16: Coefficient Meaning

| Feature        | Coefficient | Meaning                                          |
| -------------- | ----------: | ------------------------------------------------ |
| Study Hours    |         2.5 | 1 extra hour adds about 2.5 marks                |
| Attendance     |         0.2 | 1 extra attendance point adds about 0.2 marks    |
| Previous Score |         0.5 | 1 extra previous-score mark adds about 0.5 marks |
| Sleep Hours    |         1.5 | 1 extra sleep hour adds about 1.5 marks          |

---

## Slide 17: Important Phrase

# Keeping Other Features Fixed

Coefficient interpretation means:

Effect of one feature while all other features stay the same.

Example:

If Study Hours coefficient = 2.5

Then:

1 extra study hour adds around 2.5 marks, keeping attendance, previous score, and sleep hours fixed.

---

## Slide 18: Coefficient Sign

| Coefficient Sign      | Meaning                                  |
| --------------------- | ---------------------------------------- |
| Positive coefficient  | Feature increases → prediction increases |
| Negative coefficient  | Feature increases → prediction decreases |
| Near zero coefficient | Feature has weak linear effect           |

Always interpret this while keeping other features fixed.

---

## Slide 19: Prediction Example

Model:

Predicted Score
= 5

* 2.5(Study Hours)
* 0.2(Attendance)
* 0.5(Previous Score)
* 1.5(Sleep Hours)

New student:

| Feature        | Value |
| -------------- | ----: |
| Study Hours    |     6 |
| Attendance     |    80 |
| Previous Score |    60 |
| Sleep Hours    |     7 |

---

## Slide 20: Prediction Calculation

Predicted Score
= 5

* 2.5 × 6
* 0.2 × 80
* 0.5 × 60
* 1.5 × 7

= 5 + 15 + 16 + 30 + 10.5

= 76.5

Prediction:

Final Score ≈ 76.5

---

## Slide 21: Contribution View

| Part             | Calculation | Contribution |
| ---------------- | ----------- | -----------: |
| Base value       | 5           |            5 |
| Study Hours      | 2.5 × 6     |           15 |
| Attendance       | 0.2 × 80    |           16 |
| Previous Score   | 0.5 × 60    |           30 |
| Sleep Hours      | 1.5 × 7     |         10.5 |
| Final Prediction | Total       |         76.5 |

---

## Slide 22: Why It Is More Realistic

Simple Linear Regression:

Only study hours explain score.

Multiple Linear Regression:

Several factors contribute together.

This better matches real-world problems.

---

## Slide 23: House Price Example

Price
= b₀

* b₁(House Size)
* b₂(Bedrooms)
* b₃(Location Score)
* b₄(House Age)

Many features explain one numeric target.

---

## Slide 24: Salary Example

Salary
= b₀

* b₁(Experience)
* b₂(Skill Score)
* b₃(Education Level)
* b₄(Interview Score)

Target is numeric.

Features are multiple.

---

## Slide 25: Section Divider

# Part 3

## Training and Evaluation

How the model learns and how we judge it.

---

## Slide 26: How the Model Learns

The model tries to find the best values of:

b₀, b₁, b₂, b₃, b₄

Goal:

Make predictions as close as possible to actual values.

---

## Slide 27: Error Formula

Error = Actual - Predicted

or

Error = y - ŷ

Example:

| Actual Score | Predicted Score | Error |
| -----------: | --------------: | ----: |
|           70 |              68 |     2 |
|           80 |              83 |    -3 |

---

## Slide 28: Squared Error

Squared Error = (y - ŷ)²

Why square?

* Removes negative signs
* Prevents errors from cancelling
* Punishes large mistakes more

---

## Slide 29: MSE Objective

MSE = Σ(y - ŷ)² / n

Since:

ŷ = b₀ + b₁x₁ + b₂x₂ + ...

Training goal:

Find b₀, b₁, b₂, ... that minimize MSE.

---

## Slide 30: Full Training Goal

Best model = coefficients with lowest MSE

Full idea:

Minimize Σ[y - (b₀ + b₁x₁ + b₂x₂ + b₃x₃ + ...)]² / n

This is the heart of Multiple Linear Regression.

---

## Slide 31: Coefficients Are Learned Together

The model does not learn each feature separately.

It learns all coefficients together.

Why?

Features may be related.

Example:

Students who study more may also attend more classes.

So the model must decide how much credit each feature receives.

---

## Slide 32: Feature Credit Problem

| Feature        | Possible Overlap               |
| -------------- | ------------------------------ |
| Study Hours    | Related to Practice Tests      |
| Attendance     | Related to Study Discipline    |
| Previous Score | Related to Current Preparation |
| Sleep Hours    | Related to Concentration       |

Multiple Regression separates these effects as much as possible.

---

## Slide 33: Matrix Intuition

For many features, we can think in table form.

| Bias | Study | Attendance | Previous | Sleep |
| ---: | ----: | ---------: | -------: | ----: |
|    1 |     2 |         60 |       40 |     5 |
|    1 |     3 |         70 |       45 |     6 |
|    1 |     4 |         65 |       50 |     6 |

Bias column is 1 because:

b₀ × 1 = b₀

---

## Slide 34: Coefficient Vector

| Coefficient | Meaning                    |
| ----------- | -------------------------- |
| b₀          | Intercept                  |
| b₁          | Study coefficient          |
| b₂          | Attendance coefficient     |
| b₃          | Previous score coefficient |
| b₄          | Sleep coefficient          |

Prediction = feature row × coefficient vector

---

## Slide 35: Row-Level Prediction

Feature row:

[1, 6, 80, 60, 7]

Coefficient vector:

[5, 2.5, 0.2, 0.5, 1.5]

Prediction:

1×5 + 6×2.5 + 80×0.2 + 60×0.5 + 7×1.5

= 76.5

---

## Slide 36: Actual vs Predicted

| Student | Actual Score | Predicted Score | Error |
| ------- | -----------: | --------------: | ----: |
| A       |           48 |            47.6 |   0.4 |
| B       |           55 |            55.2 |  -0.2 |
| C       |           59 |            59.6 |  -0.6 |
| D       |           68 |            67.9 |   0.1 |
| E       |           72 |            72.3 |  -0.3 |

Small errors indicate good fit.

---

## Slide 37: Evaluation Metrics

| Metric      | Meaning                            |
| ----------- | ---------------------------------- |
| MAE         | Average absolute mistake           |
| MSE         | Average squared mistake            |
| RMSE        | Error in original unit             |
| R²          | How much variation is explained    |
| Adjusted R² | R² adjusted for number of features |

---

## Slide 38: MAE

MAE = Σ|y - ŷ| / n

Meaning:

Average absolute prediction error.

Example:

If MAE = 2.5

Then:

The model is wrong by around 2.5 marks on average.

---

## Slide 39: MSE

MSE = Σ(y - ŷ)² / n

Meaning:

Average squared prediction error.

MSE punishes large errors more strongly.

Lower MSE is better.

---

## Slide 40: RMSE

RMSE = √MSE

Meaning:

Error returned to original unit.

If the target is marks:

RMSE is also in marks.

If the target is rupees:

RMSE is also in rupees.

---

## Slide 41: R² Score

R² tells how much variation in the target is explained by the model.

| R² Value | Meaning                           |
| -------: | --------------------------------- |
|      1.0 | Perfect fit                       |
|      0.9 | Strong fit                        |
|      0.7 | Good fit                          |
|      0.5 | Medium fit                        |
|      0.0 | No better than average prediction |

R² can be negative if the model is very poor.

---

## Slide 42: Adjusted R²

In Multiple Regression, R² can increase when we add more features.

Even useless features may increase R² slightly.

Adjusted R² handles this by penalizing unnecessary features.

Simple meaning:

Adjusted R² rewards useful features and penalizes useless extra features.

---

## Slide 43: R² vs Adjusted R²

| Metric      | Meaning                            | Risk                                            |
| ----------- | ---------------------------------- | ----------------------------------------------- |
| R²          | How much variation model explains  | May increase when more features are added       |
| Adjusted R² | R² adjusted for number of features | Better for comparing multiple regression models |

Use Adjusted R² when comparing models with different numbers of features.

---

## Slide 44: Train-Test Split

A model should be tested on unseen data.

| Data Type     | Purpose            |
| ------------- | ------------------ |
| Training data | Learn coefficients |
| Testing data  | Check performance  |

Correct idea:

Train on old examples.

Test on new examples.

---

## Slide 45: Why Testing Matters

If a student practices 10 questions and the exam has the same 10 questions, a high score may not prove understanding.

Similarly:

Training performance alone is not enough.

Testing performance shows whether the model generalizes.

---

## Slide 46: Correct ML Workflow

1. Collect data
2. Identify features and target
3. Split into training and testing data
4. Train on training data
5. Predict on testing data
6. Evaluate test error
7. Improve model if needed

---

## Slide 47: Training vs Testing Error

| Case     | Training Error | Testing Error | Meaning |
| -------- | -------------: | ------------: | ------- |
| High     |           High |  Underfitting |         |
| Low      |            Low |      Good fit |         |
| Very low |           High |   Overfitting |         |

Goal:

Low testing error.

---

## Slide 48: Underfitting

Underfitting means:

The model is too simple and fails to learn the real pattern.

Example:

Predicted Score = 60 for every student

Problem:

High training error and high testing error.

---

## Slide 49: Overfitting

Overfitting means:

The model memorizes training data too much.

Problem:

Training error is very low.

Testing error is high.

This means the model fails on new data.

---

## Slide 50: Section Divider

# Part 4

## Practical Issues

Real-world problems in Multiple Linear Regression.

---

## Slide 51: Feature Scaling

# Why Scaling Matters

Features may have different ranges.

| Feature        |     Range | Unit       |
| -------------- | --------: | ---------- |
| Study Hours    |   1 to 10 | hours      |
| Attendance     | 40 to 100 | percentage |
| Previous Score |  0 to 100 | marks      |
| Sleep Hours    |    4 to 9 | hours      |

Different scales can make coefficient comparison difficult.

---

## Slide 52: Scaling Meaning

Feature scaling means:

Convert features into a common scale.

Two common methods:

| Method          | Formula                         |
| --------------- | ------------------------------- |
| Min-Max Scaling | (x - min) / (max - min)         |
| Standardization | (x - mean) / standard deviation |

---

## Slide 53: Standardization

Formula:

z = (x - mean) / standard deviation

After standardization:

Mean becomes 0.

Standard deviation becomes 1.

Meaning:

z tells how far a value is from the average.

---

## Slide 54: Coefficients Before Scaling

| Feature        | Coefficient | Unit Meaning           |
| -------------- | ----------: | ---------------------- |
| Study Hours    |         2.5 | Per 1 hour             |
| Attendance     |         0.2 | Per 1 percentage point |
| Previous Score |         0.5 | Per 1 mark             |
| Sleep Hours    |         1.5 | Per 1 hour             |

These are not directly comparable because units differ.

---

## Slide 55: Coefficients After Scaling

| Feature        | Scaled Coefficient | Meaning                           |
| -------------- | -----------------: | --------------------------------- |
| Study Hours    |                4.8 | Per 1 standard deviation increase |
| Attendance     |                3.2 | Per 1 standard deviation increase |
| Previous Score |                6.5 | Per 1 standard deviation increase |
| Sleep Hours    |                1.4 | Per 1 standard deviation increase |

Now comparison is more meaningful.

---

## Slide 56: Data Leakage Warning

Wrong approach:

Scale full dataset first.

Then split into train and test.

Correct approach:

Split first.

Learn scaling values from training data only.

Apply same scaling to test data.

Reason:

Test data should remain unseen.

---

## Slide 57: Target Leakage

# A Dangerous Mistake

Target leakage means:

A feature secretly contains information about the answer.

Example:

Predicting final score using:

| Feature                 | Problem                        |
| ----------------------- | ------------------------------ |
| Final grade status      | Already depends on final score |
| Certificate eligibility | May be decided after score     |
| Result published flag   | Future information             |
| Rank after exam         | Contains target information    |

Target leakage makes model look excellent but fail in real life.

---

## Slide 58: Residual Analysis

# Check the Errors

Residual = Actual - Predicted

Good residual behavior:

* Errors look random
* No clear pattern
* No extreme outliers
* Error spread is roughly stable

If residuals show a pattern, the model may be missing something.

---

## Slide 59: Residual Pattern Warning

| Residual Pattern  | Possible Meaning                   |
| ----------------- | ---------------------------------- |
| Curved pattern    | Relationship may not be linear     |
| Increasing spread | Error variance is changing         |
| Many large errors | Outliers or missing features       |
| Group-wise errors | Category or segment effect missing |

Residuals help diagnose model weakness.

---

## Slide 60: Multicollinearity

# When Features Duplicate Information

Multicollinearity means:

Two or more input features are strongly related to each other.

Examples:

| Feature 1   | Feature 2       |
| ----------- | --------------- |
| Study Hours | Practice Tests  |
| House Size  | Number of Rooms |
| Experience  | Age             |
| Ad Spend    | Impressions     |

---

## Slide 61: Why Multicollinearity Is a Problem

The model asks:

How much credit should each feature get?

If two features say almost the same thing, the model gets confused.

Prediction may still be good.

But coefficient interpretation becomes unreliable.

---

## Slide 62: Correlation

Correlation shows how two features move together.

| Correlation | Meaning                           |
| ----------: | --------------------------------- |
|        +1.0 | Perfect positive relationship     |
|        +0.9 | Very strong positive relationship |
|         0.0 | No linear relationship            |
|        -0.9 | Very strong negative relationship |
|        -1.0 | Perfect negative relationship     |

---

## Slide 63: Multicollinearity Example

| Student | Study Hours | Practice Tests |
| ------- | ----------: | -------------: |
| A       |           2 |              1 |
| B       |           3 |              2 |
| C       |           4 |              3 |
| D       |           5 |              4 |
| E       |           6 |              5 |

Study Hours and Practice Tests move together.

They may duplicate information.

---

## Slide 64: Coefficient Confusion

Model may learn:

Study Hours coefficient = -1.5
Practice Tests coefficient = 6.0

This looks strange.

Does studying reduce score?

Probably not.

This may happen because the two features are strongly correlated.

---

## Slide 65: VIF

VIF means:

Variance Inflation Factor

Simple meaning:

How much one feature can be explained by other features.

Formula:

VIF = 1 / (1 - R²)

|      VIF | Meaning              |
| -------: | -------------------- |
|        1 | No multicollinearity |
|   1 to 5 | Usually acceptable   |
|  5 to 10 | Warning zone         |
| Above 10 | Serious issue        |

---

## Slide 66: Fixing Multicollinearity

| Solution                      | Explanation                         |
| ----------------------------- | ----------------------------------- |
| Remove one correlated feature | Keep the more useful one            |
| Combine features              | Create a new meaningful score       |
| Use domain knowledge          | Choose feature with clearer meaning |
| Collect more diverse data     | Reduce overlap                      |
| Use regularization            | Ridge can help                      |
| Use PCA                       | Advanced feature compression        |

---

## Slide 67: Section Divider

# Part 5

## Categorical Features and Interactions

Handling real-world data types.

---

## Slide 68: Categorical Features

Real datasets often have text columns.

Examples:

| Feature       | Categories                    |
| ------------- | ----------------------------- |
| School Type   | Government, Private           |
| Learning Mode | Online, Offline               |
| City          | Chennai, Hyderabad, Bengaluru |
| Department    | CSE, ECE, Mechanical          |

Linear Regression needs numbers.

So categories must be encoded.

---

## Slide 69: Nominal vs Ordinal

| Type    | Meaning          | Example           | Encoding         |
| ------- | ---------------- | ----------------- | ---------------- |
| Nominal | No natural order | City, School Type | One-Hot Encoding |
| Ordinal | Has order        | Low, Medium, High | Ordered encoding |

Do not assign random numbers to unordered categories.

---

## Slide 70: One-Hot Encoding

Original:

| Student | School Type |
| ------- | ----------- |
| A       | Government  |
| B       | Private     |
| C       | Private     |
| D       | Government  |

Encoded:

| Student | School Type_Private |
| ------- | ------------------: |
| A       |                   0 |
| B       |                   1 |
| C       |                   1 |
| D       |                   0 |

Here, Government is the reference category.

---

## Slide 71: Dummy Variable Trap

If a category has two values:

Government and Private

Creating both columns gives duplicate information.

| Government | Private |
| ---------: | ------: |
|          1 |       0 |
|          0 |       1 |

One column already tells the other.

Solution:

Use k - 1 dummy columns.

---

## Slide 72: Dummy Coefficient Interpretation

Model:

Score = b₀ + b₁(Study Hours) + b₂(School Type_Private)

If:

School Type_Private = 1 → Private
School Type_Private = 0 → Government

Then:

b₂ means effect of Private compared to Government, keeping other features fixed.

---

## Slide 73: Interaction Terms

Sometimes one feature’s effect depends on another feature.

Example:

Study hours may help more when previous score is already strong.

Interaction term:

Study Hours × Previous Score

Formula:

Score = b₀ + b₁(Study Hours) + b₂(Previous Score) + b₃(Study Hours × Previous Score)

---

## Slide 74: Interaction Example

| Student | Study Hours | Previous Score | Interaction |
| ------- | ----------: | -------------: | ----------: |
| A       |           2 |             40 |          80 |
| B       |           3 |             45 |         135 |
| C       |           4 |             50 |         200 |
| D       |           5 |             60 |         300 |

Interaction = Study Hours × Previous Score

---

## Slide 75: Meaning of Interaction Coefficient

If interaction coefficient is positive:

The two features strengthen each other.

Example:

Study hours become more useful when previous score is higher.

If interaction coefficient is negative:

One feature reduces the effect of another.

Example:

Study hours become less effective when stress is high.

---

## Slide 76: Interaction Prediction Example

Model:

Score = 10 + 2(Study Hours) + 0.5(Previous Score) + 0.02(Study × Previous)

Student:

Study Hours = 4
Previous Score = 70
Interaction = 4 × 70 = 280

Prediction:

Score = 10 + 8 + 35 + 5.6

Score = 58.6

---

## Slide 77: Interaction Interpretation Rule

For:

ŷ = b₀ + b₁x₁ + b₂x₂ + b₃(x₁x₂)

Effect of x₁ is:

b₁ + b₃x₂

Meaning:

The effect of x₁ changes depending on x₂.

That is the mathematical meaning of interaction.

---

## Slide 78: Assumptions of Multiple Linear Regression

| Assumption            | Meaning                                |
| --------------------- | -------------------------------------- |
| Linear relationship   | Features combine linearly              |
| Numeric target        | Output is a number                     |
| Independent errors    | Errors should not depend on each other |
| Low multicollinearity | Features should not duplicate too much |
| Controlled outliers   | Extreme points should be checked       |
| Constant error spread | Error variance should be stable        |

---

## Slide 79: Common Mistakes

| Mistake                                 | Why It Is a Problem          |
| --------------------------------------- | ---------------------------- |
| Adding too many features blindly        | Can cause overfitting        |
| Comparing raw coefficients directly     | Units may differ             |
| Ignoring multicollinearity              | Coefficients become unstable |
| Encoding categories with random numbers | Creates false order          |
| Scaling before train-test split         | Causes data leakage          |
| Trusting training score only            | May hide poor generalization |
| Using leaked target information         | Gives fake performance       |

---

## Slide 80: When to Use Multiple Linear Regression

Use it when:

* Target is numeric
* Multiple features influence the target
* Relationship is mostly linear
* Interpretability is important
* You want to understand feature effects

Examples:

| Domain      | Prediction  |
| ----------- | ----------- |
| Education   | Final score |
| Real estate | House price |
| HR          | Salary      |
| Marketing   | Sales       |
| Finance     | Loan amount |

---

## Slide 81: Final Summary

Multiple Linear Regression formula:

ŷ = b₀ + b₁x₁ + b₂x₂ + b₃x₃ + ...

Core idea:

Prediction = base value + contribution of each feature

Training goal:

Find coefficients that minimize error.

Important concepts:

* Coefficients
* Evaluation
* Train-test split
* Scaling
* Multicollinearity
* One-hot encoding
* Interaction terms

---

## Slide 82: Next Model

# Polynomial Regression

Why next?

Sometimes one feature has a curved relationship with the target.

Example:

Study hours improve score quickly at first, but after some point improvement slows down.

Next model:

Polynomial Regression
