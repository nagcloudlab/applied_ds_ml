# Day 4: Hyperparameter Tuning, Ensemble Methods & Clustering

## Slide 1: Title

# Day 4

## Hyperparameter Tuning, Ensemble Methods & Clustering

---

## Slide 2: Logical Split of Today’s Topics

| Part   | Topic Group           | Main Question                            |
| ------ | --------------------- | ---------------------------------------- |
| Part 1 | Model Generalization  | Is my model learning correctly?          |
| Part 2 | Cross-Validation      | Can I trust my model score?              |
| Part 3 | Hyperparameter Tuning | Can I improve the model systematically?  |
| Part 4 | Ensemble Methods      | Can many models perform better than one? |
| Part 5 | Clustering            | Can we discover groups without labels?   |
| Part 6 | K-Means Evaluation    | How do we choose good clusters?          |

---

## Slide 3: Day 4 Learning Goals

By the end of today, students should understand:

* Overfitting and underfitting
* Bias-variance trade-off
* Cross-validation
* Grid Search and Random Search
* Model tuning workflow
* Bagging and Boosting
* Clustering fundamentals
* K-Means clustering
* Elbow method
* Silhouette score

---

## Slide 4: Big Picture

Training a model is only the beginning.

A practical ML engineer must answer:

* Is the model too simple?
* Is the model memorizing?
* Can it work on unseen data?
* Can tuning improve it?
* Can multiple models help?
* Can we discover hidden groups?

---

## Slide 5: Running Example for Supervised ML

Student pass/fail prediction:

| Study Hours | Attendance | Previous Score | Practice Tests | Result |
| ----------: | ---------: | -------------: | -------------: | ------ |
|           2 |         55 |             40 |              1 | Fail   |
|           4 |         70 |             55 |              2 | Pass   |
|           3 |         65 |             45 |              1 | Fail   |
|           6 |         85 |             70 |              4 | Pass   |
|           7 |         90 |             80 |              5 | Pass   |

We will use this idea for model tuning.

---

## Slide 6: Running Example for Clustering

Student grouping without labels:

| Student | Study Hours | Attendance | Practice Tests | Assignment Score |
| ------- | ----------: | ---------: | -------------: | ---------------: |
| A       |           2 |         55 |              1 |               45 |
| B       |           3 |         60 |              1 |               50 |
| C       |           5 |         75 |              3 |               65 |
| D       |           7 |         85 |              5 |               78 |
| E       |           8 |         90 |              6 |               85 |

No target column.

The goal is to discover groups.

---

## Slide 7: Section Divider

# Part 1

## Model Generalization

Overfitting, underfitting, and bias-variance trade-off.

---

## Slide 8: What is Generalization?

Generalization means:

The model performs well on new unseen data.

Example:

| Data          | Model Performance |
| ------------- | ----------------- |
| Training data | Good              |
| New test data | Good              |

A model is useful only if it generalizes.

---

## Slide 9: What is Underfitting?

Underfitting means:

The model is too simple and fails to learn the real pattern.

Example:

A model predicts almost every student as Pass.

Problem:

* Training performance is poor
* Testing performance is poor

---

## Slide 10: Underfitting Example

| Student | Actual Result | Predicted Result |
| ------- | ------------- | ---------------- |
| A       | Pass          | Pass             |
| B       | Fail          | Pass             |
| C       | Fail          | Pass             |
| D       | Pass          | Pass             |
| E       | Fail          | Pass             |

The model is not learning enough.

It is too simple.

---

## Slide 11: Underfitting Score Example

| Metric            | Score |
| ----------------- | ----: |
| Training Accuracy |   60% |
| Testing Accuracy  |   58% |

Interpretation:

Both scores are low.

The model has high bias.

---

## Slide 12: What is Overfitting?

Overfitting means:

The model learns the training data too deeply, including noise.

It performs very well on training data.

But it performs poorly on new test data.

---

## Slide 13: Overfitting Score Example

| Metric            | Score |
| ----------------- | ----: |
| Training Accuracy |   99% |
| Testing Accuracy  |   65% |

Interpretation:

The model memorized training examples.

It failed to generalize.

---

## Slide 14: Overfitting Example

A deep decision tree may create rules like:

| Rule                                                           | Prediction |
| -------------------------------------------------------------- | ---------- |
| If study_hours = 6 and attendance = 83 and previous_score = 71 | Pass       |
| If study_hours = 6 and attendance = 82 and previous_score = 70 | Fail       |

The rules are too specific.

The model may be memorizing.

---

## Slide 15: Good Fit

A good model:

* Learns useful pattern
* Does not memorize noise
* Performs well on unseen data

| Metric            | Score |
| ----------------- | ----: |
| Training Accuracy |   86% |
| Testing Accuracy  |   84% |

Training and testing scores are close.

---

## Slide 16: Three Model Conditions

| Condition    | Training Error | Testing Error |
| ------------ | -------------: | ------------: |
| Underfitting |           High |          High |
| Good Fit     |            Low |           Low |
| Overfitting  |       Very Low |          High |

Goal:

Low testing error.

---

## Slide 17: Student Learning Analogy

| ML Problem   | Student Analogy                                      |
| ------------ | ---------------------------------------------------- |
| Underfitting | Student did not understand the subject               |
| Overfitting  | Student memorized only practice questions            |
| Good fit     | Student understood concepts and solves new questions |

---

## Slide 18: Underfitting Causes

| Cause                   | Example                           |
| ----------------------- | --------------------------------- |
| Model too simple        | Straight line for complex pattern |
| Too few features        | Only study hours used             |
| Poor data quality       | Missing or wrong values           |
| Too much regularization | Model restricted too much         |

---

## Slide 19: Overfitting Causes

| Cause             | Example                                  |
| ----------------- | ---------------------------------------- |
| Model too complex | Very deep decision tree                  |
| Too many features | Useless columns included                 |
| Too little data   | Model learns noise                       |
| Data leakage      | Future information included              |
| No regularization | Coefficients or rules become too extreme |

---

## Slide 20: Fixing Underfitting

| Fix                     | Example                       |
| ----------------------- | ----------------------------- |
| Add better features     | Attendance, previous score    |
| Use more flexible model | Tree-based model              |
| Reduce regularization   | Allow model to learn more     |
| Improve data quality    | Clean missing or wrong values |

---

## Slide 21: Fixing Overfitting

| Fix                     | Example                           |
| ----------------------- | --------------------------------- |
| Simplify model          | Reduce tree depth                 |
| Add regularization      | Penalize complex model            |
| Remove useless features | Drop ID-like columns              |
| Collect more data       | More examples reduce memorization |
| Use cross-validation    | More reliable model selection     |

---

## Slide 22: Practical Example

Decision Tree with different depths:

| max_depth | Training Accuracy | Testing Accuracy | Meaning      |
| --------: | ----------------: | ---------------: | ------------ |
|         1 |               65% |              63% | Underfitting |
|         4 |               87% |              84% | Good fit     |
|        15 |              100% |              70% | Overfitting  |

---

## Slide 23: Key Memory

Underfitting:

Model learns too little.

Overfitting:

Model memorizes too much.

Good fit:

Model learns useful pattern and generalizes.

---

## Slide 24: Section Divider

# Part 2

## Bias-Variance Trade-off

Why model complexity must be balanced.

---

## Slide 25: What is Bias?

Bias means:

Error caused by overly simple assumptions.

High-bias model:

* Too simple
* Misses real pattern
* Usually underfits

Example:

Using a straight line for a strongly curved pattern.

---

## Slide 26: High Bias Example

Actual pattern:

Study hours improve score fast at first, then slow down.

Model used:

Simple straight line.

Problem:

The model cannot capture the curve.

Result:

Underfitting.

---

## Slide 27: What is Variance?

Variance means:

Model changes too much when training data changes.

High-variance model:

* Too sensitive to training data
* Learns noise
* Usually overfits

Example:

Very deep decision tree.

---

## Slide 28: High Variance Example

Training Set 1 gives one tree.

Training Set 2 gives a very different tree.

Training Set 3 gives another different tree.

The model is unstable.

That is high variance.

---

## Slide 29: Bias and Variance Table

| Model Behavior |   Bias | Variance |
| -------------- | -----: | -------: |
| Too simple     |   High |      Low |
| Balanced       | Medium |   Medium |
| Too complex    |    Low |     High |

Goal:

Balance bias and variance.

---

## Slide 30: Bias-Variance Formula

Prediction error can be understood as:

Error = Bias² + Variance + Irreducible Error

| Term              | Meaning                             |
| ----------------- | ----------------------------------- |
| Bias²             | Error from wrong/simple assumptions |
| Variance          | Error from sensitivity to data      |
| Irreducible Error | Noise we cannot remove              |

---

## Slide 31: Irreducible Error

Some error cannot be removed.

Examples:

* Human behavior randomness
* Measurement noise
* Missing real-world factors
* Unexpected events
* Data entry mistakes

Even a strong model may not become perfect.

---

## Slide 32: Model Complexity Example

| Model                 |                         Bias |        Variance |
| --------------------- | ---------------------------: | --------------: |
| Logistic Regression   |                  Higher bias |  Lower variance |
| Shallow Decision Tree |                  Medium bias | Medium variance |
| Deep Decision Tree    |                   Lower bias | Higher variance |
| Random Forest         | Lower variance than one tree |     More stable |

---

## Slide 33: Bias-Variance and Tree Depth

| Tree Depth |   Bias | Variance | Behavior    |
| ---------: | -----: | -------: | ----------- |
|          1 |   High |      Low | Too simple  |
|          4 | Medium |   Medium | Balanced    |
|         20 |    Low |     High | Too complex |

---

## Slide 34: Practical Diagnosis

| Symptom               | Likely Problem | Fix                             |
| --------------------- | -------------- | ------------------------------- |
| Train low, test low   | High bias      | More features or flexible model |
| Train high, test low  | High variance  | Simplify model or regularize    |
| Train high, test high | Good fit       | Keep improving carefully        |

---

## Slide 35: Trainer Explanation

Bias means:

The model is not learning enough.

Variance means:

The model is learning too specifically.

Good ML means:

Learning the general rule, not every accident in the data.

---

## Slide 36: Section Divider

# Part 3

## Cross-Validation

Getting a more trustworthy model score.

---

## Slide 37: Why Cross-Validation?

Train-test split gives only one evaluation.

But one split may be lucky or unlucky.

Cross-validation gives a more reliable estimate by testing multiple splits.

---

## Slide 38: Problem with One Split

Suppose test set accidentally contains easy examples.

| Split       | Test Accuracy |
| ----------- | ------------: |
| Lucky split |           92% |
| Hard split  |           74% |

One split can mislead us.

---

## Slide 39: Cross-Validation Idea

Cross-validation means:

* Split data into multiple folds
* Train and test multiple times
* Average the results

Final score is more stable.

---

## Slide 40: 5-Fold Cross-Validation

Data is divided into 5 folds.

| Round | Training Data | Validation Data |
| ----- | ------------- | --------------- |
| 1     | Folds 2,3,4,5 | Fold 1          |
| 2     | Folds 1,3,4,5 | Fold 2          |
| 3     | Folds 1,2,4,5 | Fold 3          |
| 4     | Folds 1,2,3,5 | Fold 4          |
| 5     | Folds 1,2,3,4 | Fold 5          |

---

## Slide 41: Cross-Validation Score Example

| Fold   | Accuracy |
| ------ | -------: |
| Fold 1 |     0.82 |
| Fold 2 |     0.85 |
| Fold 3 |     0.80 |
| Fold 4 |     0.86 |
| Fold 5 |     0.84 |

Average CV Score:

0.834

---

## Slide 42: Why Average Matters

One fold may be high.

One fold may be low.

Average gives a better estimate.

Also check variation:

| Model   | Average Score | Score Variation |
| ------- | ------------: | --------------- |
| Model A |          0.84 | Low             |
| Model B |          0.85 | High            |

Model A may be more stable.

---

## Slide 43: Stratified K-Fold

For classification, use Stratified K-Fold.

It preserves class ratio in every fold.

Example original data:

| Class | Ratio |
| ----- | ----: |
| Pass  |   70% |
| Fail  |   30% |

Each fold keeps roughly 70/30 ratio.

---

## Slide 44: Why Stratification Matters

Without stratification:

| Fold   | Pass | Fail |
| ------ | ---: | ---: |
| Fold 1 |  95% |   5% |
| Fold 2 |  55% |  45% |

This creates unstable evaluation.

Stratification keeps folds balanced.

---

## Slide 45: Cross-Validation for Regression and Classification

| Problem Type   | CV Method         | Common Metrics                           |
| -------------- | ----------------- | ---------------------------------------- |
| Regression     | K-Fold            | MAE, RMSE, R²                            |
| Classification | Stratified K-Fold | Accuracy, Precision, Recall, F1, ROC-AUC |

---

## Slide 46: Cross-Validation Cost Example

If:

K = 5 folds

And:

20 model configurations are tested

Total trainings:

20 × 5 = 100

Cross-validation is reliable but computationally expensive.

---

## Slide 47: Validation vs Test Set

| Data            | Purpose                               |
| --------------- | ------------------------------------- |
| Training set    | Learn model                           |
| Validation / CV | Select model and tune hyperparameters |
| Test set        | Final unbiased evaluation             |

Do not tune using the test set.

---

## Slide 48: Key Memory

Train-test split gives one view.

Cross-validation gives multiple views.

Better estimate:

Average performance across folds.

---

## Slide 49: Section Divider

# Part 4

## Hyperparameter Tuning

Improving model behavior systematically.

---

## Slide 50: Parameters vs Hyperparameters

| Type           | Meaning                | Example                          |
| -------------- | ---------------------- | -------------------------------- |
| Parameter      | Learned from data      | Logistic Regression coefficients |
| Hyperparameter | Chosen before training | max_depth in Decision Tree       |

Parameters are learned.

Hyperparameters are configured.

---

## Slide 51: Hyperparameter Examples

| Model               | Hyperparameters              |
| ------------------- | ---------------------------- |
| Logistic Regression | C, penalty                   |
| Decision Tree       | max_depth, min_samples_split |
| Random Forest       | n_estimators, max_depth      |
| KNN                 | n_neighbors                  |
| SVM                 | C, kernel, gamma             |
| K-Means             | n_clusters                   |

---

## Slide 52: Why Tune Hyperparameters?

Default settings may not be best.

Tuning helps:

* Improve validation performance
* Reduce overfitting
* Reduce underfitting
* Control model complexity
* Improve generalization

---

## Slide 53: Decision Tree Tuning Example

| max_depth | Training Accuracy | CV Accuracy | Meaning      |
| --------: | ----------------: | ----------: | ------------ |
|         1 |               65% |         62% | Underfitting |
|         3 |               82% |         79% | Better       |
|         5 |               90% |         85% | Best         |
|        15 |              100% |         74% | Overfitting  |

Choose based on CV score, not training score.

---

## Slide 54: Tuning Workflow

1. Choose model
2. Choose metric
3. Define search space
4. Use cross-validation
5. Compare configurations
6. Select best hyperparameters
7. Evaluate final model on test set

---

## Slide 55: Grid Search

Grid Search tries every combination.

Example:

| Hyperparameter    | Values        |
| ----------------- | ------------- |
| max_depth         | 3, 5, 7       |
| min_samples_split | 2, 5          |
| criterion         | gini, entropy |

Total combinations:

3 × 2 × 2 = 12

---

## Slide 56: Grid Search Example Table

| max_depth | min_samples_split | criterion |
| --------: | ----------------: | --------- |
|         3 |                 2 | gini      |
|         3 |                 2 | entropy   |
|         3 |                 5 | gini      |
|         3 |                 5 | entropy   |
|         5 |                 2 | gini      |
|         5 |                 2 | entropy   |

Grid Search tries all combinations.

---

## Slide 57: Grid Search Strengths and Weaknesses

| Strength                 | Weakness                            |
| ------------------------ | ----------------------------------- |
| Systematic               | Can be slow                         |
| Easy to explain          | Expensive for large spaces          |
| Tries all listed options | May waste time on poor combinations |

Best for small search spaces.

---

## Slide 58: Random Search

Random Search tries random combinations.

Instead of testing everything, it samples a fixed number of configurations.

Example:

Try 30 random configurations from a large search space.

---

## Slide 59: Random Search Example

Search space:

| Hyperparameter    | Range            |
| ----------------- | ---------------- |
| n_estimators      | 50 to 500        |
| max_depth         | 2 to 20          |
| min_samples_split | 2 to 20          |
| max_features      | sqrt, log2, none |

Random Search samples combinations from this space.

---

## Slide 60: Grid Search vs Random Search

| Method        | Best For                               |
| ------------- | -------------------------------------- |
| Grid Search   | Small, carefully chosen search space   |
| Random Search | Large search space, faster exploration |

Practical approach:

Start with Random Search.

Refine with smaller Grid Search.

---

## Slide 61: Choosing the Right Metric

| Problem                   | Better Metric      |
| ------------------------- | ------------------ |
| Balanced classification   | Accuracy           |
| Imbalanced classification | F1, Recall, PR-AUC |
| Disease detection         | Recall             |
| Spam detection            | Precision          |
| Regression                | MAE, RMSE, R²      |

Tuning must optimize the right metric.

---

## Slide 62: Hyperparameter Tuning Result Example

| Configuration | CV Accuracy |
| ------------- | ----------: |
| max_depth=2   |        0.74 |
| max_depth=4   |        0.83 |
| max_depth=6   |        0.86 |
| max_depth=10  |        0.78 |

Best choice:

max_depth = 6

---

## Slide 63: Over-Tuning Warning

If we tune too much on the same validation data:

The model may become optimized for validation set only.

Best practice:

Keep final test set untouched.

Use it only once at the end.

---

## Slide 64: Key Memory

Hyperparameter tuning is not guessing.

It is a systematic process:

Choose values → Train → Validate → Compare → Select → Test

Goal:

Improve generalization, not training score.

---

## Slide 65: Section Divider

# Part 5

## Hands-on: Model Tuning

Supervised learning practical workflow.

---

## Slide 66: Hands-on Problem

Problem:

Predict whether a student will pass.

Features:

| Feature        |
| -------------- |
| Study Hours    |
| Attendance     |
| Previous Score |
| Practice Tests |

Target:

Pass / Fail

---

## Slide 67: Hands-on Dataset

| Student | Study Hours | Attendance | Previous Score | Practice Tests | Result |
| ------- | ----------: | ---------: | -------------: | -------------: | ------ |
| A       |           2 |         55 |             40 |              1 | Fail   |
| B       |           4 |         70 |             55 |              2 | Pass   |
| C       |           3 |         65 |             45 |              1 | Fail   |
| D       |           6 |         85 |             70 |              4 | Pass   |
| E       |           7 |         90 |             80 |              5 | Pass   |
| F       |           5 |         75 |             60 |              3 | Pass   |

---

## Slide 68: Hands-on Step 1

# Baseline Model

Start with a simple Decision Tree.

Baseline result:

| Metric            | Score |
| ----------------- | ----: |
| Training Accuracy |   95% |
| CV Accuracy       |   78% |
| Test Accuracy     |   76% |

Interpretation:

Possible overfitting.

---

## Slide 69: Hands-on Step 2

# Tune Decision Tree

Tune these hyperparameters:

| Hyperparameter    | Values        |
| ----------------- | ------------- |
| max_depth         | 2, 3, 4, 5    |
| min_samples_split | 2, 5, 10      |
| min_samples_leaf  | 1, 2, 4       |
| criterion         | gini, entropy |

---

## Slide 70: Hands-on Step 3

# Compare Results

| Model         | Training Accuracy | CV Accuracy | Test Accuracy |
| ------------- | ----------------: | ----------: | ------------: |
| Baseline Tree |               95% |         78% |           76% |
| Tuned Tree    |               86% |         84% |           82% |

Tuned model has lower training score but better test score.

That is good.

---

## Slide 71: Hands-on Step 4

# Random Forest Tuning

Tune:

| Hyperparameter    | Meaning                         |
| ----------------- | ------------------------------- |
| n_estimators      | Number of trees                 |
| max_depth         | Depth of each tree              |
| max_features      | Features checked at each split  |
| min_samples_split | Minimum samples needed to split |

---

## Slide 72: Hands-on Final Comparison

| Model         | Tuning Method | CV Score | Test Score |
| ------------- | ------------- | -------: | ---------: |
| Decision Tree | Baseline      |     0.78 |       0.76 |
| Decision Tree | Grid Search   |     0.84 |       0.82 |
| Random Forest | Baseline      |     0.85 |       0.83 |
| Random Forest | Random Search |     0.88 |       0.86 |

Best model:

Random Forest with Random Search.

---

## Slide 73: Hands-on Discussion Questions

Ask students:

* Which model performed best?
* Did tuning improve test score?
* Did training score reduce?
* Is that a problem?
* Which metric should we optimize?
* Is the tuned model explainable?

---

## Slide 74: Section Divider

# Part 6

## Ensemble Learning

Combining models for stronger performance.

---

## Slide 75: What is Ensemble Learning?

Ensemble learning means:

Combining multiple models to create a stronger model.

Simple idea:

Many weak learners together can become a strong learner.

---

## Slide 76: Human Analogy

One doctor gives an opinion.

A panel of doctors gives a more reliable decision.

One model gives a prediction.

An ensemble combines multiple predictions.

---

## Slide 77: Why Ensembles Work

One model may make mistakes.

Multiple models may make different mistakes.

When combined, errors can reduce.

This often improves:

* Accuracy
* Stability
* Generalization

---

## Slide 78: Ensemble Types

| Type     | Main Idea                       | Example           |
| -------- | ------------------------------- | ----------------- |
| Bagging  | Train models independently      | Random Forest     |
| Boosting | Train models sequentially       | Gradient Boosting |
| Voting   | Combine different models        | Voting Classifier |
| Stacking | Meta-model combines predictions | Stacked Ensemble  |

---

## Slide 79: Bagging

Bagging means:

Bootstrap Aggregating.

Process:

1. Create many random samples from training data
2. Train one model on each sample
3. Combine predictions

For classification:

Majority vote.

For regression:

Average.

---

## Slide 80: Bootstrap Example

Original data:

A, B, C, D, E

Bootstrap sample:

A, C, C, E, B

Important:

* Some records repeat
* Some records may be missing
* Each model sees a slightly different dataset

---

## Slide 81: Bagging Prediction Example

| Model   | Prediction |
| ------- | ---------- |
| Model 1 | Pass       |
| Model 2 | Pass       |
| Model 3 | Fail       |
| Model 4 | Pass       |
| Model 5 | Pass       |

Final prediction:

Pass

Because majority voted Pass.

---

## Slide 82: What Bagging Reduces

Bagging mainly reduces variance.

Good when base model is unstable.

Example:

Decision Tree has high variance.

Random Forest uses bagging to reduce instability.

---

## Slide 83: Random Forest

Random Forest is a bagging ensemble of decision trees.

It adds randomness in two ways:

* Random data samples
* Random feature subsets

Final output:

Majority vote or average prediction.

---

## Slide 84: Random Forest Example

| Tree   | Prediction |
| ------ | ---------- |
| Tree 1 | Pass       |
| Tree 2 | Fail       |
| Tree 3 | Pass       |
| Tree 4 | Pass       |
| Tree 5 | Pass       |

Final:

Pass

Random Forest is usually more stable than one tree.

---

## Slide 85: Boosting

Boosting trains models sequentially.

Each new model focuses on previous mistakes.

Main idea:

Learn from errors step by step.

---

## Slide 86: Boosting Example

| Stage       | What Happens                |
| ----------- | --------------------------- |
| Model 1     | Learns broad pattern        |
| Model 2     | Focuses on Model 1 mistakes |
| Model 3     | Corrects remaining mistakes |
| Final Model | Combines all models         |

Boosting can be very powerful.

---

## Slide 87: Boosting Mistake Focus Example

Round 1:

Student C predicted incorrectly.

Round 2:

Model pays more attention to Student C-like cases.

Round 3:

Model focuses on remaining hard cases.

Boosting learns progressively.

---

## Slide 88: Bagging vs Boosting

| Aspect           | Bagging         | Boosting                 |
| ---------------- | --------------- | ------------------------ |
| Training         | Independent     | Sequential               |
| Main goal        | Reduce variance | Reduce bias and errors   |
| Example          | Random Forest   | Gradient Boosting        |
| Overfitting risk | Lower           | Can overfit if not tuned |

---

## Slide 89: Ensemble Summary

| Method                        | Best Use               |
| ----------------------------- | ---------------------- |
| Bagging                       | Reduce variance        |
| Random Forest                 | Strong stable baseline |
| Boosting                      | High performance       |
| XGBoost / LightGBM / CatBoost | Industry tabular data  |

---

## Slide 90: Section Divider

# Part 7

## Clustering Introduction

Unsupervised learning.

---

## Slide 91: What is Clustering?

Clustering is unsupervised learning.

It groups similar data points together.

There is no target label.

The model discovers structure by itself.

---

## Slide 92: Classification vs Clustering

| Classification         | Clustering                |
| ---------------------- | ------------------------- |
| Supervised learning    | Unsupervised learning     |
| Has labels             | No labels                 |
| Predicts known classes | Discovers groups          |
| Example: Pass/Fail     | Example: Student segments |

---

## Slide 93: Clustering Example

Student behavior data:

| Student | Study Hours | Practice Tests |
| ------- | ----------: | -------------: |
| A       |           2 |              1 |
| B       |           3 |              1 |
| C       |           6 |              5 |
| D       |           7 |              6 |
| E       |           9 |              8 |

Possible clusters:

* Low engagement
* Medium engagement
* High engagement

---

## Slide 94: Why Use Clustering?

| Use Case              | Example                     |
| --------------------- | --------------------------- |
| Customer segmentation | Premium, regular, low-value |
| Student grouping      | At-risk, developing, strong |
| Document grouping     | Similar topics              |
| Anomaly detection     | Unusual behavior            |
| Image segmentation    | Similar pixel groups        |

---

## Slide 95: Important Point

Clustering does not know the correct names.

It may output:

Cluster 0
Cluster 1
Cluster 2

Humans interpret them later.

Example:

Cluster 0 = At-risk learners
Cluster 1 = Developing learners
Cluster 2 = Strong learners

---

## Slide 96: Similarity and Distance

Clustering depends on similarity.

Common idea:

* Points close to each other are similar
* Points far from each other are different

K-Means uses distance heavily.

---

## Slide 97: Distance Example

Student A:

Study Hours = 2
Practice Tests = 1

Student B:

Study Hours = 3
Practice Tests = 2

Student C:

Study Hours = 8
Practice Tests = 7

A is closer to B than C.

So A and B are more similar.

---

## Slide 98: Euclidean Distance

For two points:

A = (x₁, y₁)
B = (x₂, y₂)

Distance = √[(x₂ - x₁)² + (y₂ - y₁)²]

Example:

A = (2,1)
B = (3,2)

Distance = √[(3-2)² + (2-1)²]
Distance = √2
Distance ≈ 1.41

---

## Slide 99: Scaling for Clustering

Scaling is very important.

Example:

| Feature     |              Range |
| ----------- | -----------------: |
| Study Hours |            1 to 10 |
| Income      | 20,000 to 2,00,000 |

Large-scale features dominate distance.

So scale features before clustering.

---

## Slide 100: Section Divider

# Part 8

## K-Means Clustering

Grouping data using centroids.

---

## Slide 101: What is K-Means?

K-Means is a clustering algorithm.

It groups data into K clusters.

K means:

Number of clusters.

Example:

K = 3 means create 3 groups.

---

## Slide 102: K-Means Goal

K-Means tries to create clusters where:

* Points inside the same cluster are close
* Points in different clusters are far
* Each cluster has a center called centroid

---

## Slide 103: What is a Centroid?

Centroid means:

Center point of a cluster.

Example:

If a cluster contains similar students, the centroid represents average behavior of that group.

---

## Slide 104: K-Means Steps

1. Choose K
2. Initialize K centroids
3. Assign each point to nearest centroid
4. Recalculate centroids
5. Repeat assignment and recalculation
6. Stop when clusters stabilize

---

## Slide 105: K-Means Example Dataset

| Student | Study Hours | Practice Tests |
| ------- | ----------: | -------------: |
| A       |           2 |              1 |
| B       |           3 |              2 |
| C       |           4 |              2 |
| D       |           7 |              6 |
| E       |           8 |              7 |
| F       |           9 |              8 |

Let K = 2.

Expected groups:

* Low practice group
* High practice group

---

## Slide 106: Initial Centroids Example

Suppose initial centroids are:

| Centroid | Study Hours | Practice Tests |
| -------- | ----------: | -------------: |
| C1       |           2 |              1 |
| C2       |           8 |              7 |

Each student will be assigned to the nearest centroid.

---

## Slide 107: Assignment Step Example

| Student | Distance to C1 | Distance to C2 | Assigned Cluster |
| ------- | -------------: | -------------: | ---------------- |
| A       |            0.0 |            8.5 | C1               |
| B       |            1.4 |            7.1 | C1               |
| C       |            2.2 |            6.4 | C1               |
| D       |            7.1 |            1.4 | C2               |
| E       |            8.5 |            0.0 | C2               |
| F       |            9.9 |            1.4 | C2               |

---

## Slide 108: Update Step Example

Cluster C1 contains:

A = (2,1)
B = (3,2)
C = (4,2)

New centroid C1:

Study Hours = (2+3+4)/3 = 3
Practice Tests = (1+2+2)/3 = 1.67

New C1 = (3, 1.67)

---

## Slide 109: Update Step for C2

Cluster C2 contains:

D = (7,6)
E = (8,7)
F = (9,8)

New centroid C2:

Study Hours = (7+8+9)/3 = 8
Practice Tests = (6+7+8)/3 = 7

New C2 = (8, 7)

---

## Slide 110: K-Means Objective

K-Means minimizes within-cluster distance.

Common measure:

WCSS = Within-Cluster Sum of Squares

WCSS means:

Sum of squared distances from each point to its cluster centroid.

Lower WCSS means tighter clusters.

---

## Slide 111: Choosing K

K-Means needs K before training.

Problem:

How do we choose K?

Common methods:

* Elbow Method
* Silhouette Score
* Domain knowledge

---

## Slide 112: Section Divider

# Part 9

## Elbow Method and Silhouette Score

Evaluating clustering quality.

---

## Slide 113: Elbow Method

Elbow method plots:

K vs WCSS

As K increases:

WCSS decreases.

But after a point, improvement becomes small.

That bending point is called the elbow.

---

## Slide 114: Elbow Example

|  K | WCSS |
| -: | ---: |
|  1 | 1000 |
|  2 |  520 |
|  3 |  280 |
|  4 |  240 |
|  5 |  220 |

Big improvement until K = 3.

After that, improvement slows.

Possible K = 3.

---

## Slide 115: Elbow Interpretation

From K = 1 to K = 2:

WCSS reduces a lot.

From K = 2 to K = 3:

WCSS reduces a lot.

From K = 3 to K = 4:

WCSS reduces only slightly.

So K = 3 may be a good choice.

---

## Slide 116: Elbow Method Caution

Elbow is not always clear.

Sometimes curve bends smoothly.

Then use:

* Silhouette score
* Domain understanding
* Business usefulness
* Cluster interpretability

---

## Slide 117: Silhouette Score

Silhouette score measures cluster quality.

It checks:

* How close a point is to its own cluster
* How far it is from other clusters

Range:

-1 to +1

---

## Slide 118: Silhouette Interpretation

|       Score | Meaning                           |
| ----------: | --------------------------------- |
| Close to +1 | Good clustering                   |
|    Around 0 | Overlapping clusters              |
|    Negative | Possibly wrong cluster assignment |

Higher silhouette score is usually better.

---

## Slide 119: Silhouette Formula

For one point:

a = average distance to points in same cluster
b = average distance to points in nearest other cluster

Silhouette = (b - a) / max(a, b)

Good clustering:

a is small, b is large.

---

## Slide 120: Silhouette Example

|  K | Silhouette Score |
| -: | ---------------: |
|  2 |             0.52 |
|  3 |             0.61 |
|  4 |             0.47 |
|  5 |             0.41 |

Best score:

K = 3

So K = 3 may be a good choice.

---

## Slide 121: Elbow + Silhouette Together

|  K | WCSS | Silhouette Score |
| -: | ---: | ---------------: |
|  2 |  520 |             0.52 |
|  3 |  280 |             0.61 |
|  4 |  240 |             0.47 |
|  5 |  220 |             0.41 |

K = 3 is strong because:

* Elbow appears around 3
* Silhouette is highest at 3

---

## Slide 122: K-Means Strengths

Good for:

* Simple clustering
* Fast training
* Large datasets
* Customer segmentation
* Student grouping
* Pattern discovery

---

## Slide 123: K-Means Limitations

K-Means struggles when:

* Clusters are not round
* Clusters have different sizes
* Outliers exist
* Features are not scaled
* K is chosen poorly
* Data has categorical features

---

## Slide 124: Section Divider

# Part 10

## Hands-on: K-Means Clustering

Practical unsupervised learning activity.

---

## Slide 125: Hands-on Goal

Problem:

Group students based on learning behavior.

Features:

| Feature          |
| ---------------- |
| Study Hours      |
| Attendance       |
| Practice Tests   |
| Assignment Score |

No target column.

Goal:

Discover natural student segments.

---

## Slide 126: Hands-on Dataset

| Student | Study Hours | Attendance | Practice Tests | Assignment Score |
| ------- | ----------: | ---------: | -------------: | ---------------: |
| A       |           2 |         55 |              1 |               45 |
| B       |           3 |         60 |              1 |               50 |
| C       |           5 |         75 |              3 |               65 |
| D       |           7 |         85 |              5 |               78 |
| E       |           8 |         90 |              6 |               85 |
| F       |           9 |         92 |              7 |               88 |

---

## Slide 127: Hands-on Steps

1. Load dataset
2. Select clustering features
3. Scale the features
4. Try different K values
5. Plot elbow curve
6. Calculate silhouette scores
7. Train K-Means with selected K
8. Assign cluster labels
9. Interpret clusters

---

## Slide 128: Expected Cluster Output

| Student | Cluster |
| ------- | ------: |
| A       |       0 |
| B       |       0 |
| C       |       1 |
| D       |       2 |
| E       |       2 |
| F       |       2 |

Cluster numbers are not names.

Humans must interpret them.

---

## Slide 129: Cluster Interpretation Example

| Cluster   | Behavior                  | Possible Name       |
| --------- | ------------------------- | ------------------- |
| Cluster 0 | Low study, low attendance | At-risk learners    |
| Cluster 1 | Medium engagement         | Developing learners |
| Cluster 2 | High study, high practice | Strong learners     |

---

## Slide 130: K-Means Evaluation Table

|  K | WCSS | Silhouette Score | Interpretation  |
| -: | ---: | ---------------: | --------------- |
|  2 |  520 |             0.52 | Too broad       |
|  3 |  280 |             0.61 | Good balance    |
|  4 |  240 |             0.47 | Too many groups |
|  5 |  220 |             0.41 | Over-clustering |

Best practical choice:

K = 3

---

## Slide 131: Hands-on Discussion Questions

Ask students:

* What does each cluster represent?
* Which students are at risk?
* Which students are strong learners?
* Does K = 3 make business sense?
* What happens if K = 2?
* What happens if K = 5?

---

## Slide 132: Day 4 Full Workflow

Supervised tuning workflow:

Train → Validate → Tune → Test

Unsupervised clustering workflow:

Select features → Scale → Cluster → Evaluate K → Interpret clusters

Both require careful evaluation.

---

## Slide 133: Final Day 4 Summary

Today we learned:

* Overfitting and underfitting
* Bias-variance trade-off
* Cross-validation
* Grid Search and Random Search
* Hands-on model tuning workflow
* Ensemble learning
* Bagging and Boosting
* Clustering basics
* K-Means clustering
* Elbow method
* Silhouette score

---

## Slide 134: Final Takeaway

Good ML is not only about training a model.

Good ML means:

* Detecting overfitting
* Validating properly
* Tuning carefully
* Combining models wisely
* Discovering hidden patterns
* Evaluating results correctly

Day 4 connects model building to real ML practice.
