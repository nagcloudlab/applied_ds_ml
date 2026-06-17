# Day 3: Supervised Learning — Classification
## Section 3: Naive Bayes

## Slide 1: Section Opening

# Naive Bayes

### A simple probability-based classification algorithm

Naive Bayes is one of the simplest and fastest classification algorithms.

It is commonly used for:

- Email spam detection
- Text classification
- Sentiment analysis
- Document categorization
- Basic medical diagnosis
- Recommendation filtering

---

## Slide 2: What Is Naive Bayes?

Naive Bayes is a classification algorithm based on **probability**.

Simple meaning:

> **Naive Bayes predicts a class by calculating which class is more probable.**

Example:

```text
Study Hours = Low
Attendance = Low
Previous Marks = Low
```

Naive Bayes asks:

```text
Which is more likely?
Pass or Fail?
```

If probability of Fail is higher, it predicts:

```text
Fail
```

---

## Slide 3: Why the Name “Bayes”?

The name comes from **Bayes’ Theorem**.

Bayes’ Theorem is a probability formula.

Beginner-friendly meaning:

> **Use existing evidence to update the probability of an outcome.**

Example:

```text
If an email contains words like "win", "free", "offer", "urgent",
what is the probability that it is spam?
```

Bayes helps answer this kind of question.

---

## Slide 4: Why the Word “Naive”?

Naive means simple.

In Naive Bayes, the algorithm makes a simple assumption:

> **All features are independent of each other.**

Example student features:

- Study hours
- Attendance
- Previous marks

Naive Bayes treats each feature as if it independently contributes to the final result.

---

## Slide 5: Independence Assumption

In real life, features may be connected.

Example:

```text
A student who studies more may also get better previous marks.
```

So study hours and previous marks may not be fully independent.

But Naive Bayes still works well in many problems, especially text classification.

That is why it is called **Naive**.

---

## Slide 6: Core Idea

Naive Bayes compares probabilities.

For classification:

```text
Probability of Class A given features
Probability of Class B given features
```

Then it chooses the class with the highest probability.

For student result:

```text
P(Pass | Study Hours, Attendance, Previous Marks)
P(Fail | Study Hours, Attendance, Previous Marks)
```

---

## Slide 7: Highest Probability Wins

If:

```text
P(Pass) > P(Fail)
```

Prediction:

```text
Pass
```

If:

```text
P(Fail) > P(Pass)
```

Prediction:

```text
Fail
```

Simple memory:

```text
Naive Bayes = probability-based decision
```

---

## Slide 8: Email Spam Example

Suppose we classify email as:

```text
Spam
Not Spam
```

Email text:

```text
"Win free money now"
```

Naive Bayes checks words:

```text
win
free
money
now
```

It asks:

```text
How often do these words appear in spam emails?
How often do these words appear in normal emails?
```

---

## Slide 9: Spam Prediction Logic

If words like:

```text
win
free
money
urgent
offer
```

appear more often in spam emails, the model predicts:

```text
Spam
```

This is why Naive Bayes is popular for text classification.

It works well with word frequency patterns.

---

## Slide 10: Simple Student Dataset

| Study Level | Attendance Level | Previous Marks Level | Result |
|---|---|---|---|
| Low | Low | Low | Fail |
| Low | Medium | Low | Fail |
| Medium | Medium | Medium | Pass |
| High | High | High | Pass |
| Medium | High | Medium | Pass |
| Low | Low | Medium | Fail |

New student:

```text
Study Level = Low
Attendance Level = Low
Previous Marks Level = Low
```

Likely prediction:

```text
Fail
```

---

## Slide 11: How Naive Bayes Thinks

Naive Bayes is like a probability-based judge.

It says:

```text
Given this evidence, which class is more likely?
```

Evidence:

```text
Low study hours
Low attendance
Low previous marks
```

Possible classes:

```text
Pass
Fail
```

It calculates probability for both classes and selects the bigger one.

---

## Slide 12: Types of Naive Bayes

Common Naive Bayes variants:

```text
Gaussian Naive Bayes
Multinomial Naive Bayes
Bernoulli Naive Bayes
```

Each one is useful for different kinds of data.

---

## Slide 13: Gaussian Naive Bayes

Used mostly for continuous numerical features.

Examples:

- Study hours
- Attendance percentage
- Previous marks
- Age
- Income
- Blood pressure

Scikit-learn class:

```python
GaussianNB
```

For our student dataset, we use **GaussianNB**.

---

## Slide 14: Multinomial Naive Bayes

Used mostly for count-based data.

Common in text classification.

Examples:

```text
Word count in email
Word count in document
Frequency of terms
```

Scikit-learn class:

```python
MultinomialNB
```

Best fit:

```text
Spam detection
Document classification
News category prediction
```

---

## Slide 15: Bernoulli Naive Bayes

Used for binary yes/no features.

Examples:

```text
Email contains word "free" = Yes/No
Email contains link = Yes/No
User clicked ad = Yes/No
```

Scikit-learn class:

```python
BernoulliNB
```

Best fit:

```text
Features are 0/1 or True/False
```

---

## Slide 16: Which Naive Bayes Should Beginners Use?

For numerical student data:

```text
study_hours
attendance
previous_marks
```

Use:

```python
GaussianNB
```

For email spam text classification:

```python
MultinomialNB
```

For binary word presence features:

```python
BernoulliNB
```

---

## Slide 17: Naive Bayes in Scikit-learn

For student Pass/Fail prediction:

```python
from sklearn.naive_bayes import GaussianNB

model = GaussianNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)
```

Flow is same as other ML models:

```text
Create model
Train model
Predict
Evaluate
```

---

## Slide 18: Complete Demo — Imports

```python
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
```

We use:

- pandas for dataset
- train_test_split for splitting data
- GaussianNB for Naive Bayes model
- metrics for evaluation

---

## Slide 19: Complete Demo — Dataset

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

Target:

```text
result = Pass / Fail
```

---

## Slide 20: Complete Demo — X and y

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
study_hours + attendance + previous_marks → result
```

---

## Slide 21: Complete Demo — Train-Test Split

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
75% data → training
25% data → testing
```

`stratify=y` keeps Pass/Fail ratio balanced in train and test data.

---

## Slide 22: Complete Demo — Train Model

```python
model = GaussianNB()

model.fit(X_train, y_train)
```

Meaning:

```text
Create Gaussian Naive Bayes model
Train it using training data
```

Simple memory:

```text
fit = learn
```

---

## Slide 23: Complete Demo — Predict and Evaluate

```python
y_pred = model.predict(X_test)

print("Actual:", list(y_test))
print("Predicted:", list(y_pred))

print("Accuracy:", accuracy_score(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("Classification Report:")
print(classification_report(y_test, y_pred))
```

This compares actual results with predicted results.

---

## Slide 24: Predict New Student — Fail Example

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

## Slide 25: Predict New Student — Pass Example

```python
new_student = pd.DataFrame({
    "study_hours": [6],
    "attendance": [85],
    "previous_marks": [75]
})

prediction = model.predict(new_student)

print("Prediction:", prediction[0])
```

Expected idea:

```text
Pass
```

---

## Slide 26: Prediction Probability

Naive Bayes can also give class probabilities.

```python
probabilities = model.predict_proba(new_student)

print("Classes:", model.classes_)
print("Probabilities:", probabilities)
```

Example output:

```text
Classes: ['Fail', 'Pass']
Probabilities: [[0.90, 0.10]]
```

Meaning:

```text
Fail probability = 0.90
Pass probability = 0.10
```

---

## Slide 27: Strengths of Naive Bayes

Naive Bayes is useful because:

- Simple to understand
- Fast to train
- Works well with small datasets
- Works very well for text classification
- Can output probabilities
- Good baseline model

In many text classification problems, Naive Bayes is surprisingly strong.

---

## Slide 28: Limitations of Naive Bayes

Naive Bayes has limitations:

- Assumes features are independent
- May not work well when features are strongly related
- May perform worse than advanced models on complex data
- Probability estimates may not always be perfectly calibrated

Example:

```text
Study hours and previous marks are related.
```

But Naive Bayes treats them as independent.

---

## Slide 29: When to Use Naive Bayes

Use Naive Bayes when:

- You need a simple baseline classifier
- You work with text classification
- You need fast training
- Dataset is not very large
- You want probability output

Common use cases:

- Spam detection
- Sentiment analysis
- News classification
- Document tagging
- Basic medical classification

---

## Slide 30: Final Summary

Remember:

```text
Naive Bayes = probability-based classifier
```

It asks:

```text
Given the features, which class is more likely?
```

For student prediction:

```text
P(Pass | study, attendance, marks)
P(Fail | study, attendance, marks)
```

Highest probability wins.

---

## Slide 31: Memory Hook

```text
Naive Bayes = probability voting
```

Simple explanation:

```text
Look at evidence.
Calculate class probabilities.
Choose the most likely class.
```

Next topic:

# Decision Tree Classifier
