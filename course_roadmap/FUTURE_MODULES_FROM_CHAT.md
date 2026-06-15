# Future Module Roadmap From Trainer Notes

This file captures future module ideas from planning notes. These are not implemented as notebooks yet.

## Day 2 - Supervised Learning: Regression

Theme:

```text
Teaching machines to predict numbers.
```

Core story:

- Day 1 prepared and understood data.
- Day 2 enters machine learning.
- First major problem type: predicting numeric values.

Important concepts:

- Supervised learning
- Features and target
- Regression definition
- Regression vs classification
- Simple Linear Regression
- Multiple Linear Regression
- Slope and intercept
- Actual vs predicted
- Error
- Train-test split
- Generalization
- Scikit-learn regression flow
- `fit()`
- `predict()`
- Regression metrics:
  - MAE
  - MSE
  - RMSE
  - R2 score
- Overfitting
- Underfitting
- Decision Tree Regression
- Random Forest Regression
- Model comparison
- Feature importance
- PyCaret regression overview

Suggested notebooks:

1. `01_machine_learning_and_regression_foundations.ipynb`
2. `02_simple_linear_regression.ipynb`
3. `03_multiple_linear_regression.ipynb`
4. `04_regression_metrics_and_error_analysis.ipynb`
5. `05_tree_based_regression.ipynb`
6. `06_pycaret_regression_optional.ipynb`
7. `07_day_02_regression_mini_project.ipynb`

Suggested case study:

```text
Predict student final marks.
```

Example columns:

- attendance
- assignment_score
- lab_score
- internal_marks
- department
- final_marks

## Day 3 - Supervised Learning: Classification

Theme:

```text
Teaching machines to predict categories.
```

Core story:

- Regression predicts numbers.
- Classification predicts labels.

Important concepts:

- Classification definition
- Binary classification
- Multi-class classification
- Multi-label classification
- Class
- Probability
- Threshold
- Labeled data
- Class balance
- Encoding target labels
- Naive Bayes
- Decision Tree Classifier
- Random Forest Classifier
- Accuracy
- Confusion matrix
- True positive
- True negative
- False positive
- False negative
- Precision
- Recall
- F1-score
- Classification report
- Class imbalance
- Stratified split
- Threshold tuning
- Feature importance
- PyCaret classification overview

Suggested notebooks:

1. `01_classification_foundations.ipynb`
2. `02_class_balance_and_classification_eda.ipynb`
3. `03_decision_tree_classification.ipynb`
4. `04_random_forest_classification.ipynb`
5. `05_naive_bayes_text_classification.ipynb`
6. `06_classification_metrics_and_confusion_matrix.ipynb`
7. `07_pycaret_classification_optional.ipynb`
8. `08_day_03_classification_mini_project.ipynb`

Suggested case study:

```text
Predict whether a student may need academic support.
```

Example columns:

- attendance
- assignment_score
- lab_score
- internal_marks
- previous_semester_marks
- department
- support_needed

## Design Principle For Future Days

Use the same signature flow:

```text
QUESTION -> DATA -> CODE -> EVIDENCE -> DECISION
```

Keep the training style:

- storytelling first
- one concept per code block
- read-output prompts
- common mistakes
- practice tasks
- exit tickets
- trainer talk tracks

