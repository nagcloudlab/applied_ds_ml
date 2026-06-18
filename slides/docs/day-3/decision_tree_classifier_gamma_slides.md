# Day 3: Supervised Learning — Classification
## Section 4: Decision Tree Classifier

## Slide 1: Section Opening

# Decision Tree Classifier

### A flowchart-style classification algorithm

In the previous section, we learned **Naive Bayes**.

Naive Bayes thinks like this:

```text
Which class has higher probability?
```

Decision Tree thinks like this:

```text
Ask questions step by step and reach a final class.
```

---

## Slide 2: What Is Decision Tree Classifier?

Decision Tree Classifier is a classification algorithm.

Simple meaning:

> **Decision Tree Classifier predicts a category by asking a series of questions.**

It works like a flowchart.

Example:

```text
Is attendance >= 75?
    Yes → Is previous marks >= 60?
        Yes → Predict Pass
        No  → Predict Fail
    No → Is study hours >= 5?
        Yes → Predict Pass
        No  → Predict Fail
```

---

## Slide 3: Final Output Is a Class

For our student example, the final output is:

```text
Pass or Fail
```

This is a category.

So this is classification.

Simple memory:

```text
Decision Tree Classifier = flowchart for predicting classes
```

---

## Slide 4: Why Is It Called a Tree?

It is called a **tree** because the structure looks like a tree.

```text
Root question
    ├── Branch
    │       ├── Leaf
    │       └── Leaf
    └── Branch
            ├── Leaf
            └── Leaf
```

Each question splits the data.

Each final answer is called a **leaf node**.

---

## Slide 5: Example Tree

```text
Attendance >= 75?
    ├── Yes
    │     └── Previous Marks >= 60?
    │            ├── Yes → Pass
    │            └── No  → Fail
    └── No
          └── Study Hours >= 5?
                 ├── Yes → Pass
                 └── No  → Fail
```

This is easy to explain because it looks like human decision-making.

---

## Slide 6: Running Example

We want to predict whether a student will **Pass** or **Fail**.

Dataset:

| Study Hours | Attendance | Previous Marks | Result |
|---:|---:|---:|---|
| 2 | 60 | 40 | Fail |
| 5 | 85 | 70 | Pass |
| 6 | 90 | 80 | Pass |
| 1 | 45 | 25 | Fail |
| 4 | 75 | 60 | Pass |
| 3 | 55 | 45 | Fail |

---

## Slide 7: Features and Target

Features:

```text
Study Hours
Attendance
Previous Marks
```

Target:

```text
Result = Pass / Fail
```

Because the target has categories, this is classification.

The model learns:

```text
Study Hours + Attendance + Previous Marks → Result
```

---

## Slide 8: How Decision Tree Learns

Decision Tree tries to find the best questions to split the data.

Example questions:

```text
Is attendance >= 70?
Is previous marks >= 50?
Is study hours >= 4?
```

It chooses questions that separate classes well.

The goal is to create groups that are mostly Pass or mostly Fail.

---

## Slide 9: Pass Group Pattern

Students with:

```text
Attendance >= 75
Previous marks >= 60
```

may mostly be:

```text
Pass
```

The tree learns this kind of rule.

---

## Slide 10: Fail Group Pattern

Students with:

```text
Attendance < 60
Previous marks < 50
```

may mostly be:

```text
Fail
```

The tree learns such conditions and builds decision rules.

---

## Slide 11: Prediction Example 1

Suppose the tree learned this:

```text
Attendance >= 70?
    Yes:
        Previous Marks >= 60?
            Yes → Pass
            No  → Fail
    No:
        Study Hours >= 5?
            Yes → Pass
            No  → Fail
```

New student:

```text
Study Hours = 5
Attendance = 80
Previous Marks = 65
```

---

## Slide 12: Prediction Path 1

Tree path:

```text
Attendance >= 70? Yes
Previous Marks >= 60? Yes
Prediction = Pass
```

The model predicts:

```text
Pass
```

Reason:

```text
Attendance is high and previous marks are high.
```

---

## Slide 13: Prediction Example 2

Another student:

```text
Study Hours = 2
Attendance = 50
Previous Marks = 35
```

Tree path:

```text
Attendance >= 70? No
Study Hours >= 5? No
Prediction = Fail
```

The model predicts:

```text
Fail
```

---

## Slide 14: Why Decision Tree Is Easy to Explain

Decision Tree gives rule-based logic.

Example explanation:

```text
The model predicted Pass because:
Attendance is high
Previous marks are high
```

This is useful in:

- Training
- Business discussions
- Client demos
- Model explanation sessions

---

## Slide 15: Classifier vs Regressor

We already learned Decision Tree Regression earlier.

Now we are learning Decision Tree Classification.

| Model | Output | Example |
|---|---|---|
| Decision Tree Regressor | Number | Price = ₹90 lakh |
| Decision Tree Classifier | Category | Result = Pass |

Simple memory:

```text
Regressor predicts number.
Classifier predicts category.
```

---

## Slide 16: Scikit-learn Classes

For regression:

```python
DecisionTreeRegressor
```

For classification:

```python
DecisionTreeClassifier
```

In this section, we use:

```python
from sklearn.tree import DecisionTreeClassifier
```

---

## Slide 17: Important Term — Root Node

The first question in the tree is called the **root node**.

Example:

```text
Attendance >= 70?
```

This is where decision-making starts.

---

## Slide 18: Important Term — Branch

A branch is the path after answering a question.

Example:

```text
Yes branch
No branch
```

Each branch leads to another question or a final answer.

---

## Slide 19: Important Term — Leaf Node

A leaf node is the final prediction.

Example:

```text
Pass
Fail
```

In classification, the leaf node gives a class/category.

---

## Slide 20: What Is Splitting?

Splitting means dividing data based on a condition.

Example:

```text
Attendance >= 70?
```

This creates two groups:

```text
Group 1: Attendance >= 70
Group 2: Attendance < 70
```

The tree checks which group has more Pass or Fail students.

---

## Slide 21: Why Tree Depth Matters

Tree depth means how many levels/questions the tree can ask.

Small tree:

- Few questions
- Easy to understand
- Less chance of overfitting

Large tree:

- Many questions
- Can become complex
- May memorize training data
- Higher overfitting risk

---

## Slide 22: max_depth

Example:

```python
max_depth=3
```

Meaning:

```text
The tree can grow up to 3 levels deep.
```

This is useful for beginner demos because it keeps the tree controlled and explainable.

---

## Slide 23: Overfitting in Decision Tree

Decision Trees can overfit easily.

Overfitting means:

> **The model memorizes the training data too much and fails on new data.**

Example of over-specific rules:

```text
If study_hours = 4.5 and attendance = 70 and previous_marks = 58 → Pass
If study_hours = 4.4 and attendance = 69 and previous_marks = 57 → Fail
```

Too many tiny rules may not generalize well.

---

## Slide 24: How to Reduce Overfitting

To reduce overfitting, control tree growth using parameters like:

```text
max_depth
min_samples_split
min_samples_leaf
```

For now, remember:

```text
Control tree size to reduce overfitting.
```

---

## Slide 25: Decision Tree Classifier Code

Basic code:

```python
from sklearn.tree import DecisionTreeClassifier

model = DecisionTreeClassifier(
    random_state=42,
    max_depth=3
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
```

Meaning:

```text
Create classifier
Train using training data
Predict test data
```

---

## Slide 26: Complete Demo — Imports

```python
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.tree import export_text
```

We use:

- pandas for data
- train_test_split for splitting
- DecisionTreeClassifier for model
- metrics for evaluation
- export_text for tree rules

---

## Slide 27: Complete Demo — Dataset

```python
data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 1.5, 2.5, 3.5, 4.5],
    "attendance": [40, 50, 55, 65, 75, 85, 90, 95, 45, 52, 60, 70],
    "previous_marks": [25, 35, 45, 55, 65, 75, 85, 90, 30, 38, 48, 58],
    "result": ["Fail", "Fail", "Fail", "Pass", "Pass", "Pass",
               "Pass", "Pass", "Fail", "Fail", "Fail", "Pass"]
}

df = pd.DataFrame(data)
```

---

## Slide 28: Complete Demo — X and y

```python
X = df[["study_hours", "attendance", "previous_marks"]]
y = df["result"]
```

Here:

```text
X = input features
y = target class
```

The model learns:

```text
study_hours + attendance + previous_marks → Pass/Fail
```

---

## Slide 29: Complete Demo — Train-Test Split

```python
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)
```

Meaning:

```text
75% training
25% testing
```

`stratify=y` keeps Pass/Fail ratio balanced.

---

## Slide 30: Complete Demo — Train and Predict

```python
model = DecisionTreeClassifier(
    random_state=42,
    max_depth=3
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
```

Simple memory:

```text
fit = learn
predict = answer
```

---

## Slide 31: Complete Demo — Evaluation

```python
print("Actual:", list(y_test))
print("Predicted:", list(y_pred))

print("Accuracy:", accuracy_score(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("Classification Report:")
print(classification_report(y_test, y_pred))
```

This compares actual class labels with predicted class labels.

---

## Slide 32: Predict New Student — Pass Example

```python
new_student = pd.DataFrame({
    "study_hours": [5],
    "attendance": [82],
    "previous_marks": [72]
})

prediction = model.predict(new_student)

print("Prediction:", prediction[0])
```

Expected idea:

```text
Pass
```

---

## Slide 33: Predict New Student — Fail Example

```python
new_student = pd.DataFrame({
    "study_hours": [2],
    "attendance": [50],
    "previous_marks": [35]
})

prediction = model.predict(new_student)

print("Prediction:", prediction[0])
```

Expected idea:

```text
Fail
```

---

## Slide 34: Prediction Probability

Decision Tree can also give class probabilities.

```python
probabilities = model.predict_proba(new_student)

print("Classes:", model.classes_)
print("Probabilities:", probabilities)
```

Example output:

```text
Classes: ['Fail', 'Pass']
Probabilities: [[0.80, 0.20]]
```

Meaning:

```text
Fail probability = 0.80
Pass probability = 0.20
```

---

## Slide 35: Visualizing Tree Rules

You can print tree rules using Scikit-learn:

```python
from sklearn.tree import export_text

tree_rules = export_text(
    model,
    feature_names=list(X.columns)
)

print(tree_rules)
```

This helps learners see how the model made decisions.

---

## Slide 36: Example Rule Output

Example output idea:

```text
|--- previous_marks <= 51.50
|   |--- class: Fail
|--- previous_marks >  51.50
|   |--- class: Pass
```

This is very useful for teaching.

Learners can see that the model made rules based on feature values.

---

## Slide 37: Strengths of Decision Tree Classifier

Decision Tree Classifier is useful because:

- Easy to understand
- Easy to explain
- Works for binary and multi-class classification
- Can handle non-linear patterns
- Does not usually require feature scaling
- Can show decision rules

Good for teaching because it feels like real-life decision-making.

---

## Slide 38: Limitations of Decision Tree Classifier

Decision Tree has limitations:

- Can overfit easily
- Small data changes can change the tree
- May not be as stable as Random Forest
- Deep trees become hard to interpret
- Sometimes less accurate than ensemble models

This is why Random Forest is often used after Decision Tree.

---

## Slide 39: When to Use Decision Tree Classifier

Use it when:

- You want explainable rules
- You need a simple classification model
- Data has condition-based patterns
- You want to teach classification clearly
- You want quick baseline performance

Examples:

- Student pass/fail prediction
- Loan approval rules
- Customer churn classification
- Medical risk category
- Ticket priority classification

---

## Slide 40: Final Summary

Remember:

```text
Decision Tree Classifier = classification model that asks questions step by step.
```

It works like:

```text
Question → Branch → Question → Branch → Final Class
```

For student prediction:

```text
Attendance high?
Previous marks high?
Study hours enough?
Result = Pass or Fail
```

---

## Slide 41: Memory Hook

```text
Decision Tree Classifier = flowchart for classification
```

Simple explanation:

```text
Ask questions.
Follow branches.
Reach final class.
```

Next topic:

# Random Forest Classifier
