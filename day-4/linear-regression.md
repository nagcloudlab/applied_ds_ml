# Linear Regression — First ML Model

## Slide 1: Title

# Linear Regression

### The first prediction model in Machine Learning

---

## Slide 2: Big Picture

# What do ML models do?

Machine Learning models learn patterns from past data.

Then they use those patterns to predict new cases.

Simple flow:

Past Data → Learn Pattern → Predict Future Value

---

## Slide 3: What Are We Predicting?

# Regression Predicts Numbers

| Input           | Prediction  |
| --------------- | ----------- |
| Study hours     | Exam score  |
| House size      | House price |
| Work experience | Salary      |
| Ad spend        | Sales       |

---

## Slide 4: Regression Problem

# Numeric Output

Regression is used when the output is a number.

| Problem             | Output  |
| ------------------- | ------- |
| Predict exam score  | Marks   |
| Predict house price | Price   |
| Predict salary      | Amount  |
| Predict temperature | Degrees |

---

## Slide 5: Regression vs Classification

# Number or Category?

| Problem               | Output Type | ML Type        |
| --------------------- | ----------- | -------------- |
| Predict exam score    | Number      | Regression     |
| Predict pass/fail     | Category    | Classification |
| Predict house price   | Number      | Regression     |
| Predict spam/not spam | Category    | Classification |

Linear Regression is for numeric prediction.

---

## Slide 6: Example Problem

# Predict Student Score

Question:

If a student studies for a certain number of hours, what score can we expect?

| Role   | Column      |
| ------ | ----------- |
| Input  | Study Hours |
| Output | Exam Score  |

---

## Slide 7: Example Dataset

# Past Student Data

| Student | Study Hours | Exam Score |
| ------- | ----------: | ---------: |
| A       |           1 |         36 |
| B       |           2 |         39 |
| C       |           3 |         47 |
| D       |           4 |         51 |
| E       |           5 |         58 |

The model learns from these examples.

---

## Slide 8: Feature and Target

# Two Important ML Terms

| Term    | Meaning                   | Example     |
| ------- | ------------------------- | ----------- |
| Feature | Input used for prediction | Study Hours |
| Target  | Output we want to predict | Exam Score  |

Simple view:

Feature → Model → Target

---

## Slide 9: Same Idea in Other Problems

# Input and Output Examples

| Feature/Input   | Target/Output    |
| --------------- | ---------------- |
| Study hours     | Score            |
| House size      | Price            |
| Work experience | Salary           |
| Ad budget       | Sales            |
| Engine size     | Fuel consumption |

---

## Slide 10: Human Intuition

# What Pattern Do We See?

| Study Hours | Score |
| ----------: | ----: |
|           1 |    36 |
|           2 |    39 |
|           3 |    47 |
|           4 |    51 |
|           5 |    58 |

General pattern:

As study hours increase, score also increases.

---

## Slide 11: What Linear Regression Does

# It Learns a Straight-Line Relationship

Linear Regression tries to find a straight line that best represents the relationship between input and output.

Example:

Study Hours → Exam Score

The line becomes the prediction rule.

---

## Slide 12: Why a Line?

# Line as a Prediction Rule

A line gives a simple rule:

If input changes, prediction changes in a consistent way.

Example:

More study hours → Higher predicted score

Linear Regression is popular because it is simple and interpretable.

---

## Slide 13: Core Formula

# Linear Regression Formula

Formula:

ŷ = mx + c

Meaning:

Predicted value = slope × input + intercept

For student score:

Predicted Score = m × Study Hours + c

---

## Slide 14: Formula Symbols

# What Each Symbol Means

| Symbol | Meaning         |
| ------ | --------------- |
| x      | Input feature   |
| y      | Actual value    |
| ŷ      | Predicted value |
| m      | Slope           |
| c      | Intercept       |

Important:

y = actual answer
ŷ = model’s predicted answer

---

## Slide 15: Same Formula, Different Terms

# Different Names Used in ML

| Concept | Common Names                         |
| ------- | ------------------------------------ |
| m       | Slope, coefficient, weight           |
| c       | Intercept, bias, constant            |
| x       | Feature, input, independent variable |
| y       | Target, output, dependent variable   |
| ŷ       | Prediction, estimated value          |

---

## Slide 16: Another Formula Style

# ML Notation

Linear Regression may also be written as:

ŷ = wx + b

| Symbol | Meaning                      |
| ------ | ---------------------------- |
| w      | Weight / coefficient / slope |
| b      | Bias / intercept             |
| x      | Input                        |
| ŷ      | Prediction                   |

So:

mx + c and wx + b mean the same idea.

---

## Slide 17: Understanding Slope

# Slope Shows Rate of Change

Slope tells:

How much output changes when input increases by 1 unit.

Formula:

m = Change in y / Change in x

For student score:

m = Change in Score / Change in Study Hours

---

## Slide 18: Slope Example

# Score Increases by 5 Marks

| Study Hours | Score |
| ----------: | ----: |
|           1 |    35 |
|           2 |    40 |
|           3 |    45 |
|           4 |    50 |
|           5 |    55 |

For every extra 1 hour, score increases by 5.

So:

m = 5

---

## Slide 19: Slope Using Two Points

# Formula for Slope

Take two points:

| Point   |  x |  y |
| ------- | -: | -: |
| Point 1 |  1 | 35 |
| Point 2 |  5 | 55 |

Formula:

m = (y₂ - y₁) / (x₂ - x₁)

m = (55 - 35) / (5 - 1)

m = 20 / 4

m = 5

---

## Slide 20: Meaning of m = 5

# Interpreting Slope

If:

m = 5

Then:

Every extra 1 unit of x increases predicted y by 5 units.

For students:

Every extra 1 study hour increases predicted score by around 5 marks.

---

## Slide 21: Positive Slope

# When x Increases, y Increases

Example:

Study Hours → Exam Score

| Study Hours | Score |
| ----------: | ----: |
|           1 |    35 |
|           2 |    40 |
|           3 |    45 |

Slope is positive.

Meaning:

More study hours → Higher score

---

## Slide 22: Negative Slope

# When x Increases, y Decreases

Example:

Screen Time → Sleep Hours

| Screen Time | Sleep Hours |
| ----------: | ----------: |
|           1 |           8 |
|           2 |           7 |
|           3 |           6 |

Slope is negative.

Meaning:

More screen time → Lower sleep hours

---

## Slide 23: Zero Slope

# When x Has Almost No Effect

Example:

Roll Number → Exam Score

| Roll Number | Score |
| ----------: | ----: |
|           1 |    70 |
|           2 |    71 |
|           3 |    69 |
|           4 |    70 |

Slope is close to zero.

Meaning:

Input does not meaningfully change output.

---

## Slide 24: Slope Strength

# Strong vs Weak Effect

| Formula       | Meaning            |
| ------------- | ------------------ |
| ŷ = 10x + 20  | Strong increase    |
| ŷ = 2x + 20   | Mild increase      |
| ŷ = 0.1x + 20 | Very weak increase |
| ŷ = -5x + 80  | Decrease           |

Slope shows both direction and strength.

---

## Slide 25: Slope Unit Caution

# Slope Depends on Units

Slope value depends on the unit of measurement.

Example:

| Measurement           | Meaning                  |
| --------------------- | ------------------------ |
| Study time in hours   | Slope = marks per hour   |
| Study time in minutes | Slope = marks per minute |

So always interpret slope with its unit.

---

## Slide 26: Understanding Intercept

# Intercept is the Starting Point

Formula:

ŷ = mx + c

When:

x = 0

Then:

ŷ = c

So intercept means:

Predicted value when input is 0.

---

## Slide 27: Intercept Example

# Starting Score

Suppose:

Predicted Score = 5 × Study Hours + 30

Here:

| Term | Value | Meaning                       |
| ---- | ----: | ----------------------------- |
| m    |     5 | Score increases by 5 per hour |
| c    |    30 | Starting predicted score      |

When study hours = 0:

Predicted Score = 30

---

## Slide 28: How to Calculate Intercept

# Simple Intercept Formula

Formula:

c = y - mx

Example point:

x = 1
y = 35
m = 5

So:

c = 35 - 5 × 1
c = 35 - 5
c = 30

Final model:

Predicted Score = 5 × Study Hours + 30

---

## Slide 29: Intercept Using Averages

# Best-Fit Intercept

For many data points, we use averages.

Formula:

c = ȳ - m x̄

Where:

| Symbol | Meaning      |
| ------ | ------------ |
| x̄     | Average of x |
| ȳ      | Average of y |
| m      | Slope        |
| c      | Intercept    |

Intercept is calculated after slope is found.

---

## Slide 30: Prediction Rule

# Slope + Intercept Together

Formula:

Predicted Score = 5 × Study Hours + 30

Meaning:

Start from 30.

Then add 5 marks for every extra study hour.

---

## Slide 31: Prediction Table

# Applying the Formula

Using:

Predicted Score = 5 × Study Hours + 30

| Study Hours | Calculation | Predicted Score |
| ----------: | ----------- | --------------: |
|           0 | 5 × 0 + 30  |              30 |
|           1 | 5 × 1 + 30  |              35 |
|           2 | 5 × 2 + 30  |              40 |
|           3 | 5 × 3 + 30  |              45 |
|           4 | 5 × 4 + 30  |              50 |

---

## Slide 32: New Prediction

# Predict for 6 Study Hours

Formula:

Predicted Score = 5 × Study Hours + 30

For 6 hours:

Predicted Score = 5 × 6 + 30

Predicted Score = 30 + 30

Predicted Score = 60

So:

6 hours → 60 marks

---

## Slide 33: Model as a Rule

# What Does the Model Learn?

The model learns the best values of:

m and c

Once learned, the model becomes:

ŷ = mx + c

So prediction becomes simple substitution.

---

## Slide 34: How Does the Model Learn?

# It Tries to Reduce Mistakes

The model checks different possible lines.

Examples:

ŷ = 4x + 30
ŷ = 5x + 30
ŷ = 6x + 30

The best line is the one with the smallest error.

---

## Slide 35: Candidate Lines

# Comparing Possible Models

Dataset:

|  x | Actual y |
| -: | -------: |
|  1 |       35 |
|  2 |       40 |
|  3 |       45 |

Candidate lines:

| Line | Formula     |
| ---- | ----------- |
| A    | ŷ = 4x + 30 |
| B    | ŷ = 5x + 30 |
| C    | ŷ = 6x + 30 |

---

## Slide 36: Candidate Line A

# Formula: ŷ = 4x + 30

|  x | Actual y | Predicted ŷ | Error |
| -: | -------: | ----------: | ----: |
|  1 |       35 |          34 |     1 |
|  2 |       40 |          38 |     2 |
|  3 |       45 |          42 |     3 |

Line A predicts too low.

---

## Slide 37: Candidate Line B

# Formula: ŷ = 5x + 30

|  x | Actual y | Predicted ŷ | Error |
| -: | -------: | ----------: | ----: |
|  1 |       35 |          35 |     0 |
|  2 |       40 |          40 |     0 |
|  3 |       45 |          45 |     0 |

Line B is perfect for this simple dataset.

---

## Slide 38: Candidate Line C

# Formula: ŷ = 6x + 30

|  x | Actual y | Predicted ŷ | Error |
| -: | -------: | ----------: | ----: |
|  1 |       35 |          36 |    -1 |
|  2 |       40 |          42 |    -2 |
|  3 |       45 |          48 |    -3 |

Line C predicts too high.

---

## Slide 39: Best Line Selection

# Which Line is Best?

| Line | Formula     | Error Pattern        |
| ---- | ----------- | -------------------- |
| A    | ŷ = 4x + 30 | Predictions too low  |
| B    | ŷ = 5x + 30 | Perfect fit          |
| C    | ŷ = 6x + 30 | Predictions too high |

Best line:

ŷ = 5x + 30

Because it has the smallest error.

---

## Slide 40: Error Formula

# Actual vs Predicted

Error = Actual - Predicted

or

Error = y - ŷ

Example:

| Actual y | Predicted ŷ | Error |
| -------: | ----------: | ----: |
|       45 |          42 |     3 |
|       50 |          55 |    -5 |

Error shows how far the prediction is from the actual value.

---

## Slide 41: Problem With Raw Error

# Positive and Negative Errors Cancel

Example:

| Actual | Predicted | Error |
| -----: | --------: | ----: |
|     50 |        45 |     5 |
|     50 |        55 |    -5 |

Raw total:

5 + (-5) = 0

But both predictions are wrong.

So raw error total is misleading.

---

## Slide 42: Absolute Error

# One Solution

Absolute Error = |Actual - Predicted|

or

Absolute Error = |y - ŷ|

| Error | Absolute Error |
| ----: | -------------: |
|     5 |              5 |
|    -5 |              5 |
|     2 |              2 |
|    -2 |              2 |

Absolute error removes negative signs.

---

## Slide 43: Squared Error

# Another Important Solution

Squared Error = (Actual - Predicted)²

or

Squared Error = (y - ŷ)²

| Error | Squared Error |
| ----: | ------------: |
|     5 |            25 |
|    -5 |            25 |
|     2 |             4 |
|    -2 |             4 |

Squaring makes all errors positive.

---

## Slide 44: Why Squared Error?

# Big Mistakes Are Punished More

| Error | Absolute Error | Squared Error |
| ----: | -------------: | ------------: |
|     1 |              1 |             1 |
|     2 |              2 |             4 |
|     5 |              5 |            25 |
|    10 |             10 |           100 |

Squared error strongly penalizes large mistakes.

---

## Slide 45: Mean Squared Error

# MSE

MSE = Average of squared errors

Formula:

MSE = Σ(y - ŷ)² / n

Where:

| Symbol | Meaning           |
| ------ | ----------------- |
| Σ      | Sum of all values |
| y      | Actual value      |
| ŷ      | Predicted value   |
| n      | Number of records |

Lower MSE means better model.

---

## Slide 46: MSE Example

# Calculate MSE

|  x | Actual y | Predicted ŷ | Error | Squared Error |
| -: | -------: | ----------: | ----: | ------------: |
|  1 |       35 |          34 |     1 |             1 |
|  2 |       40 |          38 |     2 |             4 |
|  3 |       45 |          42 |     3 |             9 |

MSE = (1 + 4 + 9) / 3

MSE = 14 / 3

MSE = 4.67

---

## Slide 47: Training Objective

# What Linear Regression Minimizes

Prediction formula:

ŷ = mx + c

Error:

y - ŷ

Since:

ŷ = mx + c

Error becomes:

y - (mx + c)

Training goal:

Find m and c that make MSE minimum.

Formula:

MSE = Σ[y - (mx + c)]² / n

---

## Slide 48: Perfect Data vs Real Data

# Real Data Has Noise

Perfect data:

|  x |  y |
| -: | -: |
|  1 | 35 |
|  2 | 40 |
|  3 | 45 |
|  4 | 50 |

Real data:

|  x |  y |
| -: | -: |
|  1 | 36 |
|  2 | 39 |
|  3 | 47 |
|  4 | 51 |

Real data rarely follows a perfect line.

---

## Slide 49: Realistic Dataset

# Student Score Data

| Study Hours | Score |
| ----------: | ----: |
|           1 |    36 |
|           2 |    39 |
|           3 |    47 |
|           4 |    51 |
|           5 |    58 |

The increase is not exactly the same every time.

But the overall pattern is increasing.

---

## Slide 50: Best-Fit Line

# Close to All Points

Linear Regression does not need to touch every point.

It tries to stay close to all points overall.

This line is called:

Best-fit line

The best-fit line has the lowest overall error.

---

## Slide 51: Best-Fit Slope

# Calculating Slope From Real Data

Formula:

m = Σ(x - x̄)(y - ȳ) / Σ(x - x̄)²

Meaning:

Slope compares how x and y move together.

For this dataset:

x̄ = 3
ȳ = 46.2

After calculation:

m = 56 / 10
m = 5.6

---

## Slide 52: Best-Fit Intercept

# Calculating c

Formula:

c = ȳ - m x̄

Values:

ȳ = 46.2
m = 5.6
x̄ = 3

Calculation:

c = 46.2 - 5.6 × 3
c = 46.2 - 16.8
c = 29.4

---

## Slide 53: Realistic Learned Model

# Final Best-Fit Formula

From the realistic dataset:

m = 5.6
c = 29.4

Final model:

Predicted Score = 5.6 × Study Hours + 29.4

Meaning:

Every extra study hour is associated with around 5.6 more marks.

---

## Slide 54: Actual vs Predicted

# Predictions Are Close, Not Perfect

Using:

Predicted Score = 5.6 × Study Hours + 29.4

| Study Hours | Actual Score | Predicted Score |
| ----------: | -----------: | --------------: |
|           1 |           36 |            35.0 |
|           2 |           39 |            40.6 |
|           3 |           47 |            46.2 |
|           4 |           51 |            51.8 |
|           5 |           58 |            57.4 |

---

## Slide 55: Residuals

# Prediction Error Row by Row

Residual = Actual - Predicted

or

Residual = y - ŷ

| Study Hours | Actual | Predicted | Residual |
| ----------: | -----: | --------: | -------: |
|           1 |     36 |      35.0 |      1.0 |
|           2 |     39 |      40.6 |     -1.6 |
|           3 |     47 |      46.2 |      0.8 |
|           4 |     51 |      51.8 |     -0.8 |
|           5 |     58 |      57.4 |      0.6 |

---

## Slide 56: Evaluation Metrics

# How Good Is the Model?

| Metric | Formula Idea        | Meaning                 |     |                          |
| ------ | ------------------- | ----------------------- | --- | ------------------------ |
| MAE    | Σ                   | y - ŷ                   | / n | Average absolute mistake |
| MSE    | Σ(y - ŷ)² / n       | Average squared mistake |     |                          |
| RMSE   | √MSE                | Error in original unit  |     |                          |
| R²     | Explained variation | Fit quality             |     |                          |

---

## Slide 57: Train-Test Split

# Why Testing Matters

A model should not be tested only on the same data it learned from.

| Data Type     | Purpose              |
| ------------- | -------------------- |
| Training data | Learn the pattern    |
| Testing data  | Check on unseen data |

Goal:

Check whether the model works for new cases.

---

## Slide 58: Underfitting and Overfitting

# Two Common Problems

| Situation    | Training Error | Testing Error | Meaning                      |
| ------------ | -------------: | ------------: | ---------------------------- |
| Underfitting |           High |          High | Model learned too little     |
| Good fit     |            Low |           Low | Model learned useful pattern |
| Overfitting  |       Very low |          High | Model memorized too much     |

Goal:

Good performance on unseen data.

---

## Slide 59: Assumptions and Limitations

# When Does It Work Well?

Linear Regression works best when:

| Assumption            | Meaning                           |
| --------------------- | --------------------------------- |
| Linear relationship   | Pattern is roughly straight       |
| Numeric target        | Output is a number                |
| Meaningful feature    | Input is related to output        |
| Few outliers          | Extreme values are controlled     |
| Safe prediction range | New inputs are within known range |

Limitations:

| Limitation                    | Example                                           |
| ----------------------------- | ------------------------------------------------- |
| One feature may not be enough | Score also depends on attendance, sleep, practice |
| Outliers can disturb the line | 10 hours study but 20 marks                       |
| Curved patterns are difficult | Improvement slows after some point                |
| Far extrapolation is risky    | Predicting score for 100 study hours              |

---

## Slide 60: Final Summary and Next Step

# Linear Regression in One View

Core formula:

ŷ = mx + c

Core goal:

Find m and c with minimum error.

Core idea:

Learn a straight-line pattern from past data.

Best use:

Predict continuous numeric values.

Next step:

Multiple Linear Regression

Formula:

ŷ = b₀ + b₁x₁ + b₂x₂ + b₃x₃

Example:

Score = b₀ + b₁(Study Hours) + b₂(Attendance) + b₃(Previous Score)
