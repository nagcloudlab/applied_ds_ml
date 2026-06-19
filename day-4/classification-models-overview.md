# Classification Models Overview

## From Basic Classifiers to Industry-Level Models

---

## Slide 1: Title

# Classification Models Overview

### Predicting categories instead of numbers

---

## Slide 2: Where We Are

Completed:

| ML Family             | Status       |
| --------------------- | ------------ |
| Regression Models     | Done         |
| Classification Models | Starting now |

Regression predicts numbers.

Classification predicts categories.

---

## Slide 3: What is Classification?

Classification means:

Predicting a class, label, or category.

Examples:

| Input               | Prediction           |
| ------------------- | -------------------- |
| Email text          | Spam / Not Spam      |
| Student performance | Pass / Fail          |
| Medical data        | Disease / No Disease |
| Customer data       | Churn / Not Churn    |
| Image               | Cat / Dog / Car      |

---

## Slide 4: Regression vs Classification

| Problem                        | Output   | ML Type        |
| ------------------------------ | -------- | -------------- |
| Predict marks                  | Number   | Regression     |
| Predict pass/fail              | Category | Classification |
| Predict salary                 | Number   | Regression     |
| Predict disease yes/no         | Category | Classification |
| Predict house price            | Number   | Regression     |
| Predict loan approved/rejected | Category | Classification |

---

## Slide 5: Classification Output

Classification output is usually:

| Type        | Example                              |
| ----------- | ------------------------------------ |
| Class label | Spam                                 |
| Probability | 0.87 probability of spam             |
| Decision    | Spam because probability > threshold |

Many classifiers first estimate probability, then convert it into a class.

---

## Slide 6: Classification Types

| Type                      | Meaning                  | Example             |
| ------------------------- | ------------------------ | ------------------- |
| Binary Classification     | Two classes              | Pass / Fail         |
| Multiclass Classification | More than two classes    | Low / Medium / High |
| Multilabel Classification | Multiple labels possible | Movie genres        |
| Imbalanced Classification | One class is rare        | Fraud detection     |

---

## Slide 7: Binary Classification

Binary classification has two classes.

Examples:

| Problem           | Classes             |
| ----------------- | ------------------- |
| Email filtering   | Spam / Not Spam     |
| Student result    | Pass / Fail         |
| Loan approval     | Approved / Rejected |
| Disease detection | Positive / Negative |
| Customer churn    | Churn / Not Churn   |

---

## Slide 8: Multiclass Classification

Multiclass classification has more than two classes.

Examples:

| Problem              | Classes                 |
| -------------------- | ----------------------- |
| Grade prediction     | A / B / C / D           |
| Image classification | Cat / Dog / Horse       |
| Customer segment     | Low / Medium / High     |
| Ticket priority      | Low / Medium / Critical |

One input belongs to one class.

---

## Slide 9: Multilabel Classification

Multilabel classification allows multiple labels for one record.

Example:

Movie classification:

| Movie   | Labels                |
| ------- | --------------------- |
| Movie A | Action, Thriller      |
| Movie B | Comedy, Family        |
| Movie C | Drama, Romance, Music |

One input can have many labels.

---

## Slide 10: Example Dataset

Student pass/fail prediction:

| Study Hours | Attendance | Previous Score | Result |
| ----------: | ---------: | -------------: | ------ |
|           2 |         55 |             40 | Fail   |
|           4 |         70 |             55 | Pass   |
|           3 |         65 |             45 | Fail   |
|           6 |         85 |             70 | Pass   |
|           7 |         90 |             80 | Pass   |

Target is categorical.

---

## Slide 11: Feature and Target

| Column         | Role    |
| -------------- | ------- |
| Study Hours    | Feature |
| Attendance     | Feature |
| Previous Score | Feature |
| Result         | Target  |

In classification:

Target is a class label.

Example:

Result = Pass or Fail

---

## Slide 12: Classification Workflow

1. Collect labeled data
2. Identify features and target
3. Encode categorical features
4. Split train/test
5. Train classifier
6. Predict class labels
7. Evaluate using classification metrics
8. Improve model

---

## Slide 13: Section Divider

# Part 1

## Core Classification Concepts

Before models, understand decisions and metrics.

---

## Slide 14: Probability to Class

Many classifiers output probability.

Example:

Probability of Pass = 0.82

Decision rule:

If probability ≥ 0.50 → Pass
If probability < 0.50 → Fail

0.50 is called the threshold.

---

## Slide 15: Threshold

Threshold decides class from probability.

Example:

| Probability of Pass | Threshold | Prediction |
| ------------------: | --------: | ---------- |
|                0.82 |      0.50 | Pass       |
|                0.63 |      0.50 | Pass       |
|                0.41 |      0.50 | Fail       |
|                0.20 |      0.50 | Fail       |

Changing threshold changes predictions.

---

## Slide 16: Why Threshold Matters

In medical diagnosis:

Missing a disease case is dangerous.

So we may use a lower threshold.

Example:

If disease probability ≥ 0.30 → Positive

This catches more true disease cases.

But it may also increase false alarms.

---

## Slide 17: Confusion Matrix

For binary classification:

|                 | Predicted Positive | Predicted Negative |
| --------------- | -----------------: | -----------------: |
| Actual Positive |      True Positive |     False Negative |
| Actual Negative |     False Positive |      True Negative |

This table is the foundation of classification evaluation.

---

## Slide 18: Confusion Matrix Example

Disease prediction:

|                   | Predicted Disease | Predicted No Disease |
| ----------------- | ----------------: | -------------------: |
| Actual Disease    |                80 |                   20 |
| Actual No Disease |                10 |                   90 |

| Term           | Value |
| -------------- | ----: |
| True Positive  |    80 |
| False Negative |    20 |
| False Positive |    10 |
| True Negative  |    90 |

---

## Slide 19: Accuracy

Accuracy means:

How many predictions were correct overall?

Formula:

Accuracy = Correct Predictions / Total Predictions

Using confusion matrix:

Accuracy = (TP + TN) / (TP + TN + FP + FN)

Good when classes are balanced.

---

## Slide 20: Accuracy Problem

Suppose fraud cases are only 1%.

A model predicts:

Everyone is Not Fraud.

Accuracy = 99%

But model catches no fraud.

So accuracy can be misleading for imbalanced datasets.

---

## Slide 21: Precision

Precision answers:

Out of predicted positives, how many were actually positive?

Formula:

Precision = TP / (TP + FP)

Use when false positives are costly.

Example:

Spam detection should avoid marking important emails as spam.

---

## Slide 22: Recall

Recall answers:

Out of actual positives, how many did we catch?

Formula:

Recall = TP / (TP + FN)

Use when false negatives are costly.

Example:

Disease detection should not miss sick patients.

---

## Slide 23: Precision vs Recall

| Metric    | Focus                               | Important When             |
| --------- | ----------------------------------- | -------------------------- |
| Precision | Correctness of positive predictions | False positives are costly |
| Recall    | Catching actual positives           | False negatives are costly |

Example:

Fraud detection often needs high recall.

Spam filtering often needs good precision.

---

## Slide 24: F1 Score

F1 Score balances precision and recall.

Formula:

F1 = 2 × (Precision × Recall) / (Precision + Recall)

Use when:

* Dataset is imbalanced
* Both precision and recall matter
* You need one combined score

---

## Slide 25: ROC-AUC

ROC-AUC measures how well the model separates classes across thresholds.

Simple meaning:

Higher AUC means better separation.

|  AUC | Meaning         |
| ---: | --------------- |
|  0.5 | Random guessing |
|  0.7 | Fair            |
|  0.8 | Good            |
| 0.9+ | Strong          |

---

## Slide 26: Classification Metrics Summary

| Metric    | Best Used When                             |
| --------- | ------------------------------------------ |
| Accuracy  | Classes are balanced                       |
| Precision | False positives are costly                 |
| Recall    | False negatives are costly                 |
| F1 Score  | Need balance between precision and recall  |
| ROC-AUC   | Need threshold-independent ranking quality |

---

## Slide 27: Section Divider

# Part 2

## Linear and Probability-Based Classifiers

Simple and interpretable classification models.

---

## Slide 28: Model 1 — Logistic Regression

Despite the name, Logistic Regression is a classification model.

Used for:

| Problem            | Classes             |
| ------------------ | ------------------- |
| Pass prediction    | Pass / Fail         |
| Churn prediction   | Churn / Not Churn   |
| Disease prediction | Positive / Negative |
| Loan prediction    | Approved / Rejected |

---

## Slide 29: Logistic Regression Idea

Linear Regression predicts any number.

Logistic Regression predicts probability between 0 and 1.

Formula idea:

Probability = sigmoid(linear score)

Linear score:

z = b₀ + b₁x₁ + b₂x₂ + ...

Sigmoid:

p = 1 / (1 + e⁻ᶻ)

---

## Slide 30: Logistic Regression Decision

Example:

Probability of Pass = 0.78

Threshold = 0.50

Since:

0.78 ≥ 0.50

Prediction:

Pass

---

## Slide 31: Logistic Regression Strengths

Good for:

* Binary classification
* Interpretable models
* Probability output
* Baseline classification model
* Linear decision boundaries

Limitations:

* Struggles with complex nonlinear patterns
* Needs feature engineering for curves/interactions
* Sensitive to outliers and scaling

---

## Slide 32: Logistic Regression Use Case

Student pass/fail:

| Feature        | Effect                                              |
| -------------- | --------------------------------------------------- |
| Study Hours    | More hours may increase pass probability            |
| Attendance     | Higher attendance may increase pass probability     |
| Previous Score | Strong previous score may increase pass probability |

Output:

Probability of Pass

---

## Slide 33: Model 2 — Naive Bayes

Naive Bayes is a probability-based classifier.

Commonly used for:

| Problem                 | Example             |
| ----------------------- | ------------------- |
| Text classification     | Spam detection      |
| Sentiment analysis      | Positive / Negative |
| Document classification | Topic prediction    |

It is fast and works well with text data.

---

## Slide 34: Naive Bayes Idea

Naive Bayes uses probability.

It asks:

Given these features, which class is most likely?

Example:

Email contains:

“free”, “winner”, “offer”

Model may predict:

Spam

---

## Slide 35: Why “Naive”?

It assumes features are independent.

Example:

Word 1 and Word 2 are treated as if they independently contribute to the class.

This assumption is often not fully true.

But the model can still work surprisingly well.

---

## Slide 36: Naive Bayes Strengths

Good for:

* Text classification
* High-dimensional data
* Fast training
* Small datasets
* Baseline NLP tasks

Limitations:

* Independence assumption is unrealistic
* Probability estimates may be rough
* Not ideal for complex feature interactions

---

## Slide 37: Section Divider

# Part 3

## Distance-Based Classifier

Prediction using nearby examples.

---

## Slide 38: Model 3 — KNN Classifier

KNN means:

K-Nearest Neighbors.

Main idea:

A new record is classified based on nearby records.

Example:

If nearest students mostly passed, predict Pass.

---

## Slide 39: KNN Example

New student:

Study Hours = 5
Attendance = 75

Nearest students:

| Neighbor  | Result |
| --------- | ------ |
| Student A | Pass   |
| Student B | Pass   |
| Student C | Fail   |

Majority class:

Pass

Prediction:

Pass

---

## Slide 40: Choosing K

K means number of neighbors.

| K Value | Behavior                             |
| ------: | ------------------------------------ |
| Small K | Sensitive to noise                   |
| Large K | Smoother but may miss local patterns |

Common values:

K = 3, 5, 7

Choose using validation.

---

## Slide 41: KNN Strengths and Weaknesses

Strengths:

* Simple idea
* Can capture nonlinear boundaries
* No training complexity

Weaknesses:

* Needs scaling
* Slow for large datasets
* Sensitive to irrelevant features
* Choosing K matters

---

## Slide 42: Section Divider

# Part 4

## Tree-Based Classifiers

Models that learn decision rules.

---

## Slide 43: Model 4 — Decision Tree Classifier

Decision Tree predicts class using if-else rules.

Example:

If Previous Score ≥ 50
and Attendance ≥ 70
then Predict Pass

Else Predict Fail

---

## Slide 44: Decision Tree Example

| Rule                                    | Prediction |
| --------------------------------------- | ---------- |
| Previous Score < 45                     | Fail       |
| Previous Score ≥ 45 and Attendance < 65 | Fail       |
| Previous Score ≥ 45 and Attendance ≥ 65 | Pass       |

Decision Trees are easy to explain.

---

## Slide 45: Gini and Entropy

Decision Trees choose splits that make groups purer.

Common split criteria:

| Criterion        | Meaning                           |
| ---------------- | --------------------------------- |
| Gini Impurity    | Measures class mixing             |
| Entropy          | Measures disorder                 |
| Information Gain | Reduction in disorder after split |

Goal:

Create groups with mostly one class.

---

## Slide 46: Decision Tree Strengths

Good for:

* Rule-based explanation
* Nonlinear patterns
* Feature interactions
* No scaling required
* Numeric and encoded categorical features

Weakness:

Can overfit easily.

---

## Slide 47: Model 5 — Random Forest Classifier

Random Forest uses many decision trees.

Each tree gives a vote.

Final prediction:

Majority vote.

Example:

| Tree   | Prediction |
| ------ | ---------- |
| Tree 1 | Pass       |
| Tree 2 | Pass       |
| Tree 3 | Fail       |
| Tree 4 | Pass       |

Final prediction:

Pass

---

## Slide 48: Why Random Forest Works Better

One tree may overfit.

Many trees together are more stable.

Random Forest reduces overfitting by:

* Using many trees
* Training on different data samples
* Using random feature subsets

---

## Slide 49: Random Forest Strengths

Good for:

* Strong baseline model
* Nonlinear patterns
* Feature importance
* Mixed feature types
* Less tuning than boosting

Weaknesses:

* Less interpretable than one tree
* Larger model size
* Can be slower than simple models

---

## Slide 50: Section Divider

# Part 5

## Margin-Based Classifier

Separating classes with boundaries.

---

## Slide 51: Model 6 — Support Vector Machine

SVM tries to find the best boundary between classes.

For binary classification:

It separates class A and class B with maximum margin.

Margin means distance between boundary and nearest points.

---

## Slide 52: SVM Intuition

Imagine two groups of points.

SVM asks:

Which line separates them with the widest safety gap?

The closest points are called support vectors.

They decide the boundary.

---

## Slide 53: Linear vs Kernel SVM

| Type       | Use Case                              |
| ---------- | ------------------------------------- |
| Linear SVM | Classes are mostly linearly separable |
| Kernel SVM | Classes have nonlinear boundaries     |

Kernel trick helps SVM create curved boundaries.

---

## Slide 54: SVM Strengths and Weaknesses

Strengths:

* Works well on small/medium datasets
* Good with high-dimensional data
* Kernel option handles nonlinear patterns

Weaknesses:

* Needs scaling
* Harder to explain
* Can be slow on large datasets
* Parameter tuning matters

---

## Slide 55: Section Divider

# Part 6

## Boosting Classifiers

Models that learn from previous mistakes.

---

## Slide 56: Model 7 — Gradient Boosting Classifier

Gradient Boosting builds models sequentially.

Each new tree tries to correct mistakes made by earlier trees.

Main idea:

Weak models combine into a strong model.

---

## Slide 57: Boosting Intuition

| Stage       | What Happens              |
| ----------- | ------------------------- |
| First tree  | Learns broad pattern      |
| Second tree | Focuses on mistakes       |
| Third tree  | Corrects remaining errors |
| Final model | Combines all trees        |

Boosting is powerful but needs careful tuning.

---

## Slide 58: Model 8 — XGBoost Classifier

XGBoost is a high-performance boosting model.

Good for:

* Tabular datasets
* Competitions
* Industry ML
* Nonlinear patterns
* Feature interactions

Often gives strong accuracy.

---

## Slide 59: Model 9 — LightGBM Classifier

LightGBM is a fast boosting model.

Good for:

* Large datasets
* Many rows
* Many features
* Faster training

Commonly used in production ML for structured data.

---

## Slide 60: Model 10 — CatBoost Classifier

CatBoost is a boosting model that handles categorical features well.

Good for datasets with:

* City
* Product category
* Department
* Customer segment
* User type

It reduces manual preprocessing for categorical-heavy data.

---

## Slide 61: Boosting Summary

| Model             | Best For                   |
| ----------------- | -------------------------- |
| Gradient Boosting | Learning boosting concept  |
| XGBoost           | High accuracy tabular data |
| LightGBM          | Large and fast datasets    |
| CatBoost          | Categorical-heavy datasets |

Boosting models are often very strong for real-world classification.

---

## Slide 62: Section Divider

# Part 7

## Neural Network Classifier

Flexible model for complex patterns.

---

## Slide 63: Model 11 — Neural Network Classifier

Neural networks learn layered representations.

Useful for:

| Data Type    | Example               |
| ------------ | --------------------- |
| Images       | Cat / Dog             |
| Text         | Sentiment             |
| Audio        | Speech classification |
| Tabular data | Customer churn        |

For tabular data, tree boosting often performs very well, but neural networks are important for deep learning.

---

## Slide 64: Neural Network Idea

Input features pass through layers.

Each layer transforms information.

Final layer outputs class probabilities.

Example:

Features → Hidden Layer → Hidden Layer → Class Probability

---

## Slide 65: Neural Network Strengths and Weaknesses

Strengths:

* Handles complex patterns
* Powerful for images, text, audio
* Can learn representations automatically

Weaknesses:

* Needs more data
* Harder to explain
* Needs scaling
* More tuning and compute

---

## Slide 66: Section Divider

# Part 8

## Special Classification Topics

Important practical concerns.

---

## Slide 67: Imbalanced Classification

Imbalanced data means one class is much smaller.

Example:

| Class     |  Count |
| --------- | -----: |
| Not Fraud | 99,000 |
| Fraud     |  1,000 |

Accuracy can be misleading.

Better metrics:

Precision, Recall, F1, ROC-AUC, PR-AUC

---

## Slide 68: Handling Imbalanced Data

Common techniques:

| Technique        | Meaning                               |
| ---------------- | ------------------------------------- |
| Class weights    | Penalize minority-class mistakes more |
| Oversampling     | Add more minority samples             |
| Undersampling    | Reduce majority samples               |
| SMOTE            | Create synthetic minority samples     |
| Threshold tuning | Adjust decision threshold             |

---

## Slide 69: Multiclass Strategies

Some models handle multiclass directly.

Others convert multiclass into multiple binary problems.

Common strategies:

| Strategy    | Meaning                            |
| ----------- | ---------------------------------- |
| One-vs-Rest | One classifier per class           |
| One-vs-One  | One classifier per pair of classes |

Example:

Classes = A, B, C

One-vs-Rest:

A vs others
B vs others
C vs others

---

## Slide 70: Probability Calibration

Some models give probabilities.

But probability may not always be well-calibrated.

Example:

If model says 80% probability, ideally 8 out of 10 such cases should be correct.

Calibration helps make probabilities more trustworthy.

Important in:

* Medical decisions
* Risk scoring
* Credit approval
* Fraud detection

---

## Slide 71: Feature Scaling Need

| Model               | Scaling Needed? |
| ------------------- | --------------- |
| Logistic Regression | Recommended     |
| KNN                 | Required        |
| SVM                 | Required        |
| Neural Network      | Required        |
| Decision Tree       | Usually no      |
| Random Forest       | Usually no      |
| Boosting Trees      | Usually no      |

Scaling matters strongly for distance and gradient-based models.

---

## Slide 72: Categorical Feature Handling

| Model               | Handling Categories        |
| ------------------- | -------------------------- |
| Logistic Regression | One-hot encoding           |
| KNN                 | One-hot encoding           |
| SVM                 | One-hot encoding           |
| Decision Tree       | Encoding needed in sklearn |
| Random Forest       | Encoding needed in sklearn |
| CatBoost            | Handles categories well    |

Do not assign random numbers to nominal categories.

---

## Slide 73: Data Leakage in Classification

Target leakage means a feature secretly contains the answer.

Examples:

| Feature                    | Problem                          |
| -------------------------- | -------------------------------- |
| Result status              | Already contains pass/fail       |
| Approval timestamp         | Created after approval           |
| Diagnosis code after test  | Future information               |
| Fraud investigation result | Known only after fraud detection |

Leakage gives fake performance.

---

## Slide 74: Model Interpretability

| Model               | Interpretability |
| ------------------- | ---------------- |
| Logistic Regression | High             |
| Naive Bayes         | Medium           |
| Decision Tree       | High             |
| Random Forest       | Medium           |
| Boosting Models     | Medium-Low       |
| SVM                 | Low              |
| Neural Network      | Low              |

Choose model based on both accuracy and explanation needs.

---

## Slide 75: Which Classifier to Try First?

| Situation                       | Good Starting Model           |
| ------------------------------- | ----------------------------- |
| Need simple baseline            | Logistic Regression           |
| Text classification             | Naive Bayes                   |
| Nonlinear tabular data          | Random Forest                 |
| High accuracy tabular data      | XGBoost / LightGBM / CatBoost |
| Small dataset with clear margin | SVM                           |
| Image/text/audio deep learning  | Neural Network                |

---

## Slide 76: Classification Model Map

| Family               | Models                                         |
| -------------------- | ---------------------------------------------- |
| Linear / Probability | Logistic Regression, Naive Bayes               |
| Distance-Based       | KNN                                            |
| Tree-Based           | Decision Tree, Random Forest                   |
| Margin-Based         | SVM                                            |
| Boosting             | Gradient Boosting, XGBoost, LightGBM, CatBoost |
| Deep Learning        | Neural Network                                 |

---

## Slide 77: Common Classification Workflow

1. Understand the class labels
2. Check class balance
3. Prepare features
4. Split train/test
5. Train baseline classifier
6. Evaluate confusion matrix
7. Check precision, recall, F1
8. Tune threshold if needed
9. Compare stronger models
10. Explain final model

---

## Slide 78: Common Mistakes

| Mistake                           | Why It Is a Problem                      |
| --------------------------------- | ---------------------------------------- |
| Using accuracy on imbalanced data | Can hide poor minority-class performance |
| Ignoring threshold                | Default 0.5 may not be best              |
| Not checking confusion matrix     | Misses error type                        |
| Random number encoding categories | Creates fake order                       |
| Scaling before split              | Causes leakage                           |
| Trusting training accuracy        | May hide overfitting                     |

---

## Slide 79: Classification Model Summary

| Model                         | One-Line Meaning               |
| ----------------------------- | ------------------------------ |
| Logistic Regression           | Predicts class probability     |
| Naive Bayes                   | Uses probability rules         |
| KNN                           | Uses nearby examples           |
| Decision Tree                 | Uses if-else rules             |
| Random Forest                 | Many trees vote                |
| SVM                           | Finds best separating boundary |
| Gradient Boosting             | Learns from mistakes           |
| XGBoost / LightGBM / CatBoost | Industry-level boosting        |
| Neural Network                | Learns layered patterns        |

---

## Slide 80: Final Takeaway

Classification predicts categories.

Core question:

Which class does this record belong to?

Important evaluation tools:

* Confusion Matrix
* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC

Next learning path:

Start deep with Logistic Regression.
