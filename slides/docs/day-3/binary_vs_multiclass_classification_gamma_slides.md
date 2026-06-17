# Day 3: Supervised Learning — Classification
## Section 2: Binary Classification vs Multi-class Classification

## Slide 1: Section Opening

# Binary Classification vs Multi-class Classification

### Understanding classification output types

In the previous section, we learned:

```text
Classification = predicting a category/class
```

Now we learn two common types:

```text
1. Binary Classification
2. Multi-class Classification
```

---

## Slide 2: What Is Binary Classification?

Binary means **two**.

So, Binary Classification means:

> **Predicting one class out of two possible classes.**

Simple examples:

- Pass or Fail
- Spam or Not Spam
- Disease or No Disease
- Loan Approved or Rejected
- Fraud or Not Fraud
- Customer Will Buy or Will Not Buy

There are only two possible answers.

---

## Slide 3: Student Example — Pass or Fail

Dataset:

| Study Hours | Attendance | Previous Marks | Result |
|---:|---:|---:|---|
| 2 | 60 | 40 | Fail |
| 5 | 85 | 70 | Pass |
| 6 | 90 | 80 | Pass |
| 1 | 45 | 25 | Fail |

Target column:

```text
Result
```

Possible target values:

```text
Pass
Fail
```

Only two classes.

So this is **Binary Classification**.

---

## Slide 4: Binary Classification as 0 and 1

In many ML projects, binary classes are written as numbers.

Example:

```text
0 = Fail
1 = Pass
```

Dataset:

| Study Hours | Attendance | Previous Marks | Result |
|---:|---:|---:|---:|
| 2 | 60 | 40 | 0 |
| 5 | 85 | 70 | 1 |
| 6 | 90 | 80 | 1 |
| 1 | 45 | 25 | 0 |

Even though the target is written as numbers, it is still classification.

Why?

```text
0 and 1 are labels, not measurable quantities.
```

---

## Slide 5: Binary Example — Email Spam Detection

Target:

```text
Spam / Not Spam
```

Two classes:

```text
Spam
Not Spam
```

So this is binary classification.

The model predicts whether an email belongs to one of two classes.

---

## Slide 6: Binary Example — Medical Disease Prediction

Target:

```text
Disease / No Disease
```

Two classes:

```text
Disease
No Disease
```

So this is binary classification.

The model predicts whether a patient belongs to the disease class or no-disease class.

---

## Slide 7: Binary Example — Loan Approval

Target:

```text
Approved / Rejected
```

Two classes:

```text
Approved
Rejected
```

So this is binary classification.

The model predicts one of two loan decisions.

---

## Slide 8: Binary Example — Fraud Detection

Target:

```text
Fraud / Not Fraud
```

Two classes:

```text
Fraud
Not Fraud
```

So this is binary classification.

The model predicts whether a transaction is suspicious or normal.

---

## Slide 9: What Is Multi-class Classification?

Multi-class means **more than two classes**.

So, Multi-class Classification means:

> **Predicting one class from three or more possible classes.**

Examples:

- Low / Medium / High
- Cat / Dog / Cow / Horse
- Beginner / Intermediate / Advanced
- Bronze / Silver / Gold / Platinum
- Red / Green / Blue
- Class A / Class B / Class C

There are more than two possible categories.

---

## Slide 10: Student Grade Example

Instead of predicting only Pass/Fail, suppose we predict grade.

Dataset:

| Study Hours | Attendance | Previous Marks | Grade |
|---:|---:|---:|---|
| 2 | 60 | 40 | C |
| 5 | 85 | 70 | B |
| 6 | 90 | 80 | A |
| 1 | 45 | 25 | D |
| 4 | 75 | 60 | B |

Target column:

```text
Grade
```

Possible target values:

```text
A
B
C
D
```

There are four classes.

So this is **Multi-class Classification**.

---

## Slide 11: Risk Level Example

Suppose a bank predicts customer risk level.

Features:

- Income
- Credit score
- Loan amount
- Payment history
- Employment status

Target:

```text
Risk Level
```

Possible values:

```text
Low Risk
Medium Risk
High Risk
```

There are three classes.

So this is multi-class classification.

---

## Slide 12: Binary vs Multi-class Comparison

| Point | Binary Classification | Multi-class Classification |
|---|---|---|
| Number of classes | 2 | 3 or more |
| Example | Pass/Fail | A/B/C/D grade |
| Output | One of two classes | One of many classes |
| Common labels | 0/1 | 0/1/2/3 or text labels |
| Business use | Fraud/Not Fraud | Low/Medium/High Risk |

Simple memory:

```text
Binary = two classes
Multi-class = more than two classes
```

---

## Slide 13: Important: One Prediction at a Time

In multi-class classification, the model usually predicts **one class** from many classes.

Example input:

```text
Study Hours = 6
Attendance = 90
Previous Marks = 80
```

Possible classes:

```text
A, B, C, D
```

Final prediction:

```text
A
```

The model selects the most likely class.

---

## Slide 14: Probability in Binary Classification

Binary classifier may give probabilities like:

```text
Fail probability = 0.20
Pass probability = 0.80
```

Final prediction:

```text
Pass
```

Because Pass has higher probability.

Another example:

```text
Spam probability = 0.92
Not Spam probability = 0.08
```

Final prediction:

```text
Spam
```

---

## Slide 15: Probability in Multi-class Classification

Multi-class classifier may give probabilities like:

```text
A probability = 0.70
B probability = 0.20
C probability = 0.08
D probability = 0.02
```

Final prediction:

```text
A
```

Because A has the highest probability.

---

## Slide 16: Risk Probability Example

Another multi-class example:

```text
Low Risk probability = 0.10
Medium Risk probability = 0.30
High Risk probability = 0.60
```

Final prediction:

```text
High Risk
```

The model chooses the class with the highest probability.

---

## Slide 17: Python Target Example — Binary

Binary classification target:

```python
y = df["result"]
```

Values:

```text
Pass, Fail
```

or:

```text
1, 0
```

Example:

```text
0 = Fail
1 = Pass
```

---

## Slide 18: Python Target Example — Multi-class

Multi-class classification target:

```python
y = df["grade"]
```

Values:

```text
A, B, C, D
```

or:

```text
0, 1, 2, 3
```

Example:

```text
0 = D
1 = C
2 = B
3 = A
```

---

## Slide 19: Same Features, Different Target

Same input data can become binary or multi-class depending on the target.

Student features:

```text
Study Hours
Attendance
Previous Marks
```

Binary target:

```text
Result = Pass / Fail
```

Multi-class target:

```text
Grade = A / B / C / D
```

The target variable decides the classification type.

---

## Slide 20: Real Business Examples — Binary

Binary classification examples:

```text
Will customer churn? Yes/No
Will transaction be fraud? Yes/No
Will loan be approved? Yes/No
Will email be spam? Yes/No
Will student pass? Yes/No
```

Binary means two possible classes.

---

## Slide 21: Real Business Examples — Multi-class

Multi-class classification examples:

```text
Customer segment: Budget / Regular / Premium
Risk level: Low / Medium / High
Ticket priority: Low / Medium / High / Critical
Product category: Electronics / Fashion / Grocery / Furniture
Sentiment: Positive / Neutral / Negative
```

Multi-class means three or more possible classes.

---

## Slide 22: Multi-class vs Multi-label

# Important confusion

Multi-class and multi-label are different.

## Multi-class Classification

One item belongs to **one class only**.

Example:

```text
Image = Cat
```

Possible classes:

```text
Cat, Dog, Cow
```

Final answer is one class.

---

## Slide 23: What Is Multi-label Classification?

In multi-label classification, one item can belong to **multiple classes at the same time**.

Example:

A movie can be:

```text
Action
Comedy
Adventure
```

A news article can be:

```text
Politics
Economy
International
```

Your ToC is mainly about binary and multi-class classification.

---

## Slide 24: Common Confusion 1

# If target has 0 and 1, is it regression?

No.

If 0 and 1 are category codes, it is classification.

Example:

```text
0 = Not Fraud
1 = Fraud
```

This is binary classification.

The numbers are labels, not measurable values.

---

## Slide 25: Common Confusion 2

# If target has 1, 2, 3, is it regression?

Not always.

If numbers represent categories:

```text
1 = Low Risk
2 = Medium Risk
3 = High Risk
```

then it is classification.

If numbers represent measurable values:

```text
Salary = 30000
Price = 120000
Marks = 85
```

then it is regression.

---

## Slide 26: Common Confusion 3

# Can binary classification have probability?

Yes.

Example:

```text
Pass probability = 0.82
Fail probability = 0.18
```

The final class is usually the class with the higher probability.

Probability tells model confidence.

---

## Slide 27: Final Summary

Remember:

```text
Classification = predicting category
```

Two common types:

```text
Binary Classification = two classes
Multi-class Classification = three or more classes
```

Examples:

```text
Pass/Fail → Binary
Spam/Not Spam → Binary
A/B/C/D Grade → Multi-class
Low/Medium/High Risk → Multi-class
```

---

## Slide 28: Memory Hook

```text
Binary = either this or that
Multi-class = choose one from many
```

Examples:

```text
Binary: Pass or Fail
Multi-class: A, B, C, or D
```

---

## Slide 29: Small Quiz

Identify binary or multi-class:

```text
1. Spam / Not Spam
2. Low / Medium / High
3. Pass / Fail
4. Cat / Dog / Cow / Horse
5. Approved / Rejected
```

---

## Slide 30: Quiz Answers

```text
1. Binary
2. Multi-class
3. Binary
4. Multi-class
5. Binary
```

Next topic:

# Naive Bayes
