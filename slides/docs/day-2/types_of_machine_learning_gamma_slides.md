# Types of Machine Learning

## Beginner-Friendly Deep Dive

Using simple examples to understand supervised, unsupervised, and semi-supervised learning.

---

# Big Idea

Machine Learning types depend on one key question:

**Do we already have the answer column in the data?**

- If the answer column is available → Supervised Learning
- If the answer column is not available → Unsupervised Learning
- If only some answers are available → Semi-supervised Learning

---

# The Three Main Types

1. **Supervised Learning**
2. **Unsupervised Learning**
3. **Semi-supervised Learning**

These are not just theory terms.

They tell us how the machine learns from data.

---

# Supervised Learning

## Simple Meaning

Supervised Learning means:

**We train the machine using data where the correct answer is already available.**

Think of it like a student learning with an answer key.

```text
Question + Correct Answer
Question + Correct Answer
Question + Correct Answer
```

The model studies these examples and learns the pattern.

---

# Supervised Learning: House Price Example

| Area | Bedrooms | House Age | Distance | Price |
|---:|---:|---:|---:|---:|
| 1000 | 2 | 5 | 8 km | ₹55 lakh |
| 1500 | 3 | 3 | 5 km | ₹82 lakh |
| 2000 | 4 | 2 | 4 km | ₹120 lakh |
| 900 | 2 | 10 | 12 km | ₹42 lakh |

The answer column is:

**Price**

The model learns:

```text
Area + Bedrooms + Age + Distance → Price
```

---

# Why This Is Supervised Learning

Because the correct output is already given during training.

The machine sees examples like:

```text
1000 sqft, 2 bedrooms, 5 years, 8 km → ₹55 lakh
1500 sqft, 3 bedrooms, 3 years, 5 km → ₹82 lakh
```

Then it learns how house details relate to price.

---

# Student Result Example

| Study Hours | Attendance | Previous Marks | Result |
|---:|---:|---:|---|
| 2 | 60% | 40 | Fail |
| 5 | 85% | 70 | Pass |
| 6 | 90% | 80 | Pass |
| 1 | 45% | 25 | Fail |

The answer column is:

**Result**

The model learns:

```text
Study Hours + Attendance + Previous Marks → Pass or Fail
```

---

# Two Types Inside Supervised Learning

Supervised Learning has two important branches:

```text
Supervised Learning
    ├── Regression
    └── Classification
```

- **Regression** predicts a number
- **Classification** predicts a category

---

# Regression

Regression means:

**Predicting a number.**

Examples:

- Predict house price
- Predict salary
- Predict marks
- Predict sales
- Predict temperature
- Predict delivery time

House price example:

```text
Input: Area, Bedrooms, Age, Distance
Output: ₹90 lakh
```

Because output is a number, it is Regression.

---

# Classification

Classification means:

**Predicting a category or class.**

Examples:

- Pass or Fail
- Spam or Not Spam
- Disease or No Disease
- Loan Approved or Rejected
- Customer Will Buy or Not Buy

Student result example:

```text
Input: Study hours, attendance, previous marks
Output: Pass
```

Because output is a category, it is Classification.

---

# Regression vs Classification

| Question | ML Type |
|---|---|
| How much is the house price? | Regression |
| Will the student pass or fail? | Classification |
| What will be tomorrow’s temperature? | Regression |
| Is this email spam? | Classification |
| What salary should be offered? | Regression |
| Is this transaction fraud? | Classification |

Memory rule:

```text
Number output → Regression
Category output → Classification
```

---

# Unsupervised Learning

## Simple Meaning

Unsupervised Learning means:

**We give data to the machine, but there is no answer column.**

The machine tries to find hidden patterns by itself.

There is no teacher answer key.

---

# Customer Grouping Example

| Customer | Age | Monthly Income | Spending Score |
|---|---:|---:|---:|
| A | 22 | ₹30,000 | High |
| B | 45 | ₹1,20,000 | Medium |
| C | 23 | ₹28,000 | High |
| D | 50 | ₹1,50,000 | Low |
| E | 35 | ₹80,000 | Medium |

There is no answer column like:

```text
Premium customer
Budget customer
Luxury customer
```

The machine groups similar customers automatically.

---

# Possible Customer Groups

The model may discover groups like:

- Group 1: Young customers with high spending
- Group 2: High income customers with low spending
- Group 3: Middle income customers with medium spending

This is Unsupervised Learning because the model is discovering structure.

It is not predicting a known answer column.

---

# House Example: No Price Column

| Area | Bedrooms | Age | Distance |
|---:|---:|---:|---:|
| 900 | 2 | 10 | 12 |
| 1100 | 2 | 8 | 10 |
| 2000 | 4 | 2 | 4 |
| 2200 | 4 | 3 | 5 |
| 1500 | 3 | 5 | 7 |

No price is given.

The model may group houses as:

- Small and far houses
- Large and near-city houses
- Medium houses

---

# Use Cases of Unsupervised Learning

Unsupervised Learning is useful for:

- Customer segmentation
- Product recommendation patterns
- Grouping similar documents
- Finding unusual behavior
- Market basket analysis
- Image grouping

Example:

An e-commerce company can group customers into discount seekers, premium buyers, frequent buyers, and window shoppers.

---

# Supervised vs Unsupervised

| Point | Supervised Learning | Unsupervised Learning |
|---|---|---|
| Answer column available? | Yes | No |
| Learns from correct answers? | Yes | No |
| Main goal | Prediction | Pattern discovery |
| Example | Predict house price | Group similar houses |
| Output | Known target | Hidden pattern |

Memory trick:

```text
Supervised = With answer
Unsupervised = Without answer
```

---

# Semi-supervised Learning

## Simple Meaning

Semi-supervised Learning means:

**Some data has answers, but a lot of data does not have answers.**

It sits between supervised and unsupervised learning.

---

# Medical Image Example

A hospital has 10,000 X-ray images.

Only 500 images are labeled by doctors.

| Image | Label |
|---|---|
| Image 1 | Normal |
| Image 2 | Pneumonia |
| Image 3 | Normal |
| Image 4 | Unknown |
| Image 5 | Unknown |
| Image 6 | Unknown |

The model learns from small labeled data and large unlabeled data.

---

# House Price Semi-supervised Example

| Area | Bedrooms | Age | Distance | Price |
|---:|---:|---:|---:|---:|
| 1000 | 2 | 5 | 8 | ₹55 lakh |
| 1500 | 3 | 3 | 5 | ₹82 lakh |
| 2000 | 4 | 2 | 4 | Unknown |
| 900 | 2 | 10 | 12 | Unknown |
| 2200 | 4 | 3 | 5 | Unknown |

Some rows have price.

Many rows do not have price.

This is Semi-supervised Learning.

---

# Classroom Analogy

## Supervised Learning

Teacher gives questions and answers.

```text
Question: 2 + 2
Answer: 4
```

## Unsupervised Learning

Teacher gives only objects.

```text
Apple, Banana, Carrot, Potato, Mango
```

Student groups them.

## Semi-supervised Learning

Teacher gives some answers only.

```text
Apple = Fruit
Carrot = Vegetable
Banana = ?
Potato = ?
```

---

# How to Identify the ML Type

Ask this first:

**Is there a target or answer column?**

- Yes → Supervised Learning
- No → Unsupervised Learning
- Some rows only → Semi-supervised Learning

Then ask:

**If supervised, what type of answer?**

- Number → Regression
- Category → Classification

---

# Practice 1

Data:

```text
Area, Bedrooms, Location, Price
```

Goal:

```text
Predict house price
```

Answer:

```text
Supervised Learning → Regression
```

Why?

Price is available, and price is a number.

---

# Practice 2

Data:

```text
Email text, Sender, Links, Spam/Not Spam
```

Goal:

```text
Predict whether a new email is spam
```

Answer:

```text
Supervised Learning → Classification
```

Why?

The answer is available, and output is a category.

---

# Practice 3

Data:

```text
Customer age, income, spending score
```

Goal:

```text
Group similar customers
```

Answer:

```text
Unsupervised Learning
```

Why?

There is no answer column.

---

# Practice 4

Data:

```text
10,000 product images
Only 500 images have labels
Remaining images are unlabeled
```

Goal:

```text
Learn product categories
```

Answer:

```text
Semi-supervised Learning
```

Why?

Only some data has labels.

---

# Common Confusions

## Confusion 1

Supervised does not mean a human is watching the model.

It means the training data contains correct answers.

## Confusion 2

Unsupervised learning also learns.

But it learns hidden patterns without answer labels.

## Confusion 3

Regression and Classification are inside Supervised Learning.

---

# Final Summary

Remember:

```text
Supervised Learning = Data has answer column
Unsupervised Learning = Data has no answer column
Semi-supervised Learning = Some data has answer, most data does not
```

Inside Supervised Learning:

```text
Regression = Predict number
Classification = Predict category
```

---

# Quick Quiz

A bank has old customer data:

```text
Age, income, credit score, loan amount, loan approved or rejected
```

They want to predict whether a new customer’s loan should be approved.

What type is it?

---

# Quick Quiz Answer

```text
Supervised Learning → Classification
```

Why?

- The answer column is available: approved/rejected
- The output is a category
