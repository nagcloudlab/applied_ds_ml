# Logistic Regression — Slide Deck

## Slide 1: Title

# Logistic Regression

### First classification model for predicting probabilities and classes

---

## Slide 2: Learning Path

# What Students Will Learn

* Why Logistic Regression is used for classification
* Probability, sigmoid, threshold
* Logistic Regression formula
* Coefficient interpretation
* Log loss
* Confusion matrix and metrics
* Threshold tuning
* Practical mistakes and limitations

---

## Slide 3: Classification Recap

# Classification Predicts Categories

| Problem        | Output               |
| -------------- | -------------------- |
| Student result | Pass / Fail          |
| Email          | Spam / Not Spam      |
| Loan           | Approved / Rejected  |
| Patient        | Disease / No Disease |

---

## Slide 4: Logistic Regression Use Case

# Example: Student Pass Prediction

Question:

Can we predict whether a student will pass?

| Feature        | Example |
| -------------- | ------- |
| Study Hours    | 6       |
| Attendance     | 80      |
| Previous Score | 60      |

Target:

Pass / Fail

---

## Slide 5: Example Dataset

| Study Hours | Attendance | Previous Score | Result |
| ----------: | ---------: | -------------: | ------ |
|           2 |         55 |             40 | Fail   |
|           4 |         70 |             55 | Pass   |
|           3 |         65 |             45 | Fail   |
|           6 |         85 |             70 | Pass   |
|           7 |         90 |             80 | Pass   |

---

## Slide 6: Feature and Target

| Column         | Role    |
| -------------- | ------- |
| Study Hours    | Feature |
| Attendance     | Feature |
| Previous Score | Feature |
| Result         | Target  |

Target is categorical.

---

## Slide 7: Why Not Linear Regression?

Linear Regression predicts continuous numbers.

But classification needs probability between 0 and 1.

Problem:

Linear Regression can predict values like:

* -0.3
* 1.4
* 2.1

These are invalid probabilities.

---

## Slide 8: Logistic Regression Output

Logistic Regression predicts probability.

Example:

Probability of Pass = 0.82

Then decision:

If probability ≥ threshold → Pass
If probability < threshold → Fail

---

## Slide 9: Threshold

Default threshold is usually:

0.50

| Probability of Pass | Prediction |
| ------------------: | ---------- |
|                0.82 | Pass       |
|                0.65 | Pass       |
|                0.40 | Fail       |
|                0.20 | Fail       |

---

## Slide 10: Core Formula Step 1

# Linear Score

First, Logistic Regression calculates a linear score.

z = b₀ + b₁x₁ + b₂x₂ + b₃x₃

For students:

z = b₀ + b₁(Study Hours) + b₂(Attendance) + b₃(Previous Score)

---

## Slide 11: Core Formula Step 2

# Sigmoid Function

Then it converts z into probability.

p = 1 / (1 + e⁻ᶻ)

This function is called sigmoid.

Output is always between 0 and 1.

---

## Slide 12: Sigmoid Intuition

| z value | Probability |
| ------: | ----------: |
|      -3 |        0.05 |
|      -1 |        0.27 |
|       0 |        0.50 |
|       1 |        0.73 |
|       3 |        0.95 |

Higher z → higher probability.

---

## Slide 13: Complete Formula

Linear score:

z = b₀ + b₁x₁ + b₂x₂ + b₃x₃

Probability:

p = 1 / (1 + e⁻ᶻ)

Prediction:

If p ≥ 0.50 → Class 1
If p < 0.50 → Class 0

---

## Slide 14: Class Encoding

For binary classification, classes are often encoded as:

| Class | Encoded Value |
| ----- | ------------: |
| Fail  |             0 |
| Pass  |             1 |

So:

p means probability of class 1.

Example:

p = Probability of Pass

---

## Slide 15: Prediction Example

Suppose model learned:

z = -8 + 0.7(Study Hours) + 0.05(Attendance) + 0.08(Previous Score)

New student:

| Feature        | Value |
| -------------- | ----: |
| Study Hours    |     6 |
| Attendance     |    80 |
| Previous Score |    60 |

---

## Slide 16: Calculate z

z = -8 + 0.7(6) + 0.05(80) + 0.08(60)

z = -8 + 4.2 + 4 + 4.8

z = 5.0

Now convert z into probability.

---

## Slide 17: Convert z to Probability

p = 1 / (1 + e⁻ᶻ)

For:

z = 5

p ≈ 0.99

So:

Probability of Pass ≈ 99%

Prediction:

Pass

---

## Slide 18: Contribution View

| Part           | Calculation | Contribution |
| -------------- | ----------- | -----------: |
| Intercept      | -8          |           -8 |
| Study Hours    | 0.7 × 6     |          4.2 |
| Attendance     | 0.05 × 80   |          4.0 |
| Previous Score | 0.08 × 60   |          4.8 |
| Linear Score z | Total       |          5.0 |

---

## Slide 19: Coefficient Meaning

| Coefficient Sign | Meaning                                  |
| ---------------- | ---------------------------------------- |
| Positive         | Feature increases probability of class 1 |
| Negative         | Feature decreases probability of class 1 |
| Near zero        | Weak effect                              |

Example:

Positive study coefficient means more study hours increase probability of passing.

---

## Slide 20: Important Phrase

Coefficient interpretation means:

Effect of one feature while other features stay fixed.

Example:

If Study Hours coefficient is positive:

More study hours increase pass probability, keeping attendance and previous score fixed.

---

## Slide 21: Odds

Odds are another way to express probability.

Odds = p / (1 - p)

Example:

If p = 0.80

Odds = 0.80 / 0.20

Odds = 4

Meaning:

Pass is 4 times as likely as Fail.

---

## Slide 22: Log-Odds

Logistic Regression is linear in log-odds.

log-odds = b₀ + b₁x₁ + b₂x₂ + ...

So:

Logistic Regression does not directly model probability linearly.

It models log-odds linearly.

---

## Slide 23: Odds Ratio

Odds Ratio = eᵇ

If coefficient b = 0.7:

Odds Ratio = e⁰·⁷ ≈ 2.01

Meaning:

For 1 unit increase in that feature, odds become about 2 times, keeping other features fixed.

---

## Slide 24: Decision Boundary

Logistic Regression separates classes using a boundary.

For two features:

z = b₀ + b₁x₁ + b₂x₂

At threshold 0.50:

p = 0.50

This happens when:

z = 0

So the decision boundary is:

b₀ + b₁x₁ + b₂x₂ = 0

---

## Slide 25: Linear Decision Boundary

Logistic Regression creates a linear decision boundary.

In 2D:

Boundary is a line.

In 3D:

Boundary is a plane.

With many features:

Boundary is a hyperplane.

---

## Slide 26: When Logistic Regression Works Well

Good when:

* Classes are mostly linearly separable
* Interpretability is important
* Probability output is needed
* Dataset is tabular
* You need a strong baseline classifier

---

## Slide 27: Training Goal

The model learns:

b₀, b₁, b₂, b₃, ...

Goal:

Predicted probabilities should match actual class labels.

For actual Pass, probability should be high.

For actual Fail, probability should be low.

---

## Slide 28: Why Not MSE?

For Linear Regression, we used MSE.

For Logistic Regression, we usually use:

Log Loss

Why?

Because classification is probability-based.

Log Loss strongly penalizes confident wrong predictions.

---

## Slide 29: Log Loss

For one record:

If actual y = 1:

Loss = -log(p)

If actual y = 0:

Loss = -log(1 - p)

Where:

p = predicted probability of class 1

---

## Slide 30: Log Loss Intuition

| Actual Class | Predicted Probability | Result          |
| -----------: | --------------------: | --------------- |
|            1 |                  0.99 | Very small loss |
|            1 |                  0.60 | Medium loss     |
|            1 |                  0.10 | Very high loss  |
|            0 |                  0.05 | Very small loss |
|            0 |                  0.90 | Very high loss  |

Confident wrong predictions are punished heavily.

---

## Slide 31: Training Objective

Logistic Regression tries to minimize:

Log Loss

Simple meaning:

Find coefficients that produce good probabilities.

Good model:

* High probability for correct class
* Low probability for wrong class

---

## Slide 32: Regularization

Logistic Regression can overfit when features are many.

Regularization controls coefficient size.

| Type | Meaning                         |
| ---- | ------------------------------- |
| L2   | Shrinks coefficients            |
| L1   | Can make weak coefficients zero |

This helps generalization.

---

## Slide 33: Feature Scaling

Scaling is recommended for Logistic Regression.

Why?

* Helps optimization
* Makes regularization fair
* Makes coefficients easier to compare

Common method:

z = (x - mean) / standard deviation

---

## Slide 34: Evaluation Starts Here

After training, we evaluate predictions.

Classification evaluation is different from regression.

Important tools:

* Confusion Matrix
* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

---

## Slide 35: Confusion Matrix

|             | Predicted Pass | Predicted Fail |
| ----------- | -------------: | -------------: |
| Actual Pass |  True Positive | False Negative |
| Actual Fail | False Positive |  True Negative |

This table shows what type of mistakes the model makes.

---

## Slide 36: Confusion Matrix Example

|             | Predicted Pass | Predicted Fail |
| ----------- | -------------: | -------------: |
| Actual Pass |             80 |             20 |
| Actual Fail |             10 |             90 |

| Term | Value |
| ---- | ----: |
| TP   |    80 |
| FN   |    20 |
| FP   |    10 |
| TN   |    90 |

---

## Slide 37: Accuracy

Accuracy = Correct Predictions / Total Predictions

Formula:

Accuracy = (TP + TN) / (TP + TN + FP + FN)

Good when classes are balanced.

---

## Slide 38: Accuracy Problem

Suppose 99% students pass.

A model predicts:

Everyone passes.

Accuracy = 99%

But it cannot identify failing students.

So accuracy can be misleading when classes are imbalanced.

---

## Slide 39: Precision

Precision answers:

Out of predicted positives, how many were truly positive?

Formula:

Precision = TP / (TP + FP)

Use when false positives are costly.

Example:

Do not wrongly mark a good email as spam.

---

## Slide 40: Recall

Recall answers:

Out of actual positives, how many did we catch?

Formula:

Recall = TP / (TP + FN)

Use when false negatives are costly.

Example:

Do not miss disease cases.

---

## Slide 41: Precision vs Recall

| Metric    | Focus                                  | Costly Mistake |
| --------- | -------------------------------------- | -------------- |
| Precision | Positive predictions should be correct | False Positive |
| Recall    | Actual positives should be caught      | False Negative |

Choose based on business problem.

---

## Slide 42: F1 Score

F1 Score balances precision and recall.

Formula:

F1 = 2 × Precision × Recall / (Precision + Recall)

Use when:

* Dataset is imbalanced
* Both precision and recall matter
* You need one combined score

---

## Slide 43: ROC-AUC

ROC-AUC measures class separation across thresholds.

|  AUC | Meaning         |
| ---: | --------------- |
|  0.5 | Random guessing |
|  0.7 | Fair            |
|  0.8 | Good            |
| 0.9+ | Strong          |

Useful for comparing classifiers.

---

## Slide 44: Precision-Recall AUC

PR-AUC is useful when positive class is rare.

Example:

* Fraud detection
* Disease detection
* Defect detection

When data is highly imbalanced, PR-AUC may be more informative than ROC-AUC.

---

## Slide 45: Threshold Tuning

Default threshold:

0.50

But it is not always best.

Example:

Disease detection may use:

Threshold = 0.30

This catches more disease cases but increases false positives.

---

## Slide 46: Threshold Trade-Off

| Lower Threshold          | Higher Threshold          |
| ------------------------ | ------------------------- |
| More positives predicted | Fewer positives predicted |
| Higher recall            | Higher precision          |
| More false positives     | More false negatives      |

Threshold should match business cost.

---

## Slide 47: Business Threshold Examples

| Problem           | Priority              | Threshold Strategy           |
| ----------------- | --------------------- | ---------------------------- |
| Disease detection | Catch positives       | Lower threshold              |
| Spam detection    | Avoid false spam      | Higher precision             |
| Fraud detection   | Catch fraud           | High recall                  |
| Loan approval     | Avoid risky approvals | Balance precision and recall |

---

## Slide 48: Train-Test Split

Correct workflow:

1. Split data into training and testing
2. Train on training data
3. Predict on test data
4. Evaluate test performance

Test data must remain unseen during training.

---

## Slide 49: Imbalanced Classes

Example:

| Class | Count |
| ----- | ----: |
| Pass  |   950 |
| Fail  |    50 |

Problem:

Model may ignore minority class.

Accuracy may look high but recall for minority class may be poor.

---

## Slide 50: Handling Imbalance

Common methods:

| Method           | Meaning                           |
| ---------------- | --------------------------------- |
| Class weights    | Penalize minority mistakes more   |
| Oversampling     | Add more minority samples         |
| Undersampling    | Reduce majority samples           |
| SMOTE            | Create synthetic minority samples |
| Threshold tuning | Adjust decision threshold         |

---

## Slide 51: Categorical Features

Logistic Regression needs numeric input.

Text categories must be encoded.

Example:

| Feature     | Encoding                    |
| ----------- | --------------------------- |
| Gender      | One-hot encoding            |
| City        | One-hot encoding            |
| Department  | One-hot encoding            |
| Skill Level | Ordinal encoding if ordered |

---

## Slide 52: One-Hot Encoding Example

Original:

| School Type |
| ----------- |
| Government  |
| Private     |

Encoded:

| School Type_Private |
| ------------------: |
|                   0 |
|                   1 |

Here:

0 = Government
1 = Private

Government is reference category.

---

## Slide 53: Data Leakage

Target leakage means a feature secretly contains the answer.

Examples:

| Feature                | Problem                 |
| ---------------------- | ----------------------- |
| Final result status    | Already contains target |
| Certificate issued     | Decided after result    |
| Rank after exam        | Future information      |
| Pass notification sent | Depends on target       |

Leakage creates fake high performance.

---

## Slide 54: Multicollinearity

Logistic Regression can also be affected by multicollinearity.

Example:

| Feature 1   | Feature 2           |
| ----------- | ------------------- |
| Study Hours | Practice Tests      |
| Attendance  | Class Participation |

Highly related features can make coefficients unstable.

---

## Slide 55: Probability Calibration

A model may output probability.

But is it trustworthy?

If model says 80% probability, ideally 8 out of 10 similar cases should be positive.

Calibration checks whether predicted probabilities are reliable.

---

## Slide 56: Multiclass Logistic Regression

Logistic Regression can be extended to multiple classes.

Example:

Grade prediction:

A / B / C / D

Approaches:

* One-vs-Rest
* Multinomial Logistic Regression

---

## Slide 57: One-vs-Rest

For classes A, B, C:

Train separate classifiers:

A vs Others
B vs Others
C vs Others

Final class:

Class with highest probability

---

## Slide 58: Softmax Idea

For multiclass classification, softmax converts scores into probabilities.

Example:

| Class   | Probability |
| ------- | ----------: |
| Grade A |        0.20 |
| Grade B |        0.55 |
| Grade C |        0.25 |

Prediction:

Grade B

---

## Slide 59: Strengths of Logistic Regression

Good for:

* Binary classification
* Probability output
* Interpretable coefficients
* Fast training
* Strong baseline
* Works well with clean linear patterns

---

## Slide 60: Limitations

Limitations:

* Linear decision boundary
* Needs feature engineering for nonlinear patterns
* Sensitive to outliers
* Needs scaling for best optimization
* Can struggle with complex interactions
* Accuracy can mislead on imbalanced data

---

## Slide 61: Common Mistakes

| Mistake                                          | Problem                           |
| ------------------------------------------------ | --------------------------------- |
| Thinking it is regression                        | It is classification              |
| Using accuracy only                              | Bad for imbalance                 |
| Ignoring threshold                               | Default may not fit business goal |
| Not scaling features                             | Can affect optimization           |
| Random category numbers                          | Creates fake order                |
| Interpreting coefficients without “fixed others” | Misleading                        |

---

## Slide 62: When to Use Logistic Regression

Use it when:

* Target is categorical
* You need probability
* You need interpretation
* You want a baseline classifier
* Relationship is mostly linear
* Dataset is tabular

---

## Slide 63: Logistic Regression Summary

Core idea:

Linear score → Sigmoid → Probability → Class

Formula:

z = b₀ + b₁x₁ + b₂x₂ + ...

p = 1 / (1 + e⁻ᶻ)

Decision:

If p ≥ threshold → Class 1
Else → Class 0

---

## Slide 64: Final Takeaway

Logistic Regression is the first major classification model.

It predicts:

Probability of belonging to a class.

It is powerful because it is:

* Simple
* Fast
* Interpretable
* Probability-based

Next model:

Naive Bayes
