# Day 1: Exploratory Data Analysis — From Question to Decision

## Gamma-Ready Consolidated Deck

Audience:

```text
Beginner learners (2nd-year college students) entering applied data science, machine learning, and AI.
```

Training intent:

```text
One deck to teach the entire Day 1 notebook. Covers AI context, Python essentials framing, and the full Data Science lifecycle from problem understanding through communication.
Flows directly into the Day 1 notebook: day_01_data_science_lifecycle_demo.ipynb
```

Core message:

```text
AI became powerful because data, algorithms, and computing power matured together.
Data Science is the disciplined lifecycle that turns messy data into trustworthy decisions.
Today we walk through every step of that lifecycle on one dataset.
```

---

# Slide 1 - Title

## Entering the AI World

### From Data to Intelligence

In this deck, we will cover:

- Why AI became powerful now
- What the AI family tree looks like
- Where Data Science fits
- The Data Science lifecycle end to end
- Python essentials for data work
- Data inspection, cleaning, EDA, statistics, visualization, and feature preparation

Speaker note:

```text
This is one consolidated deck for the full Day 1. Start with the big picture, then move step by step through the lifecycle. The notebook is the hands-on companion.
```

---

# Slide 2 - Opening Question

## Did AI Start With ChatGPT?

Ask the audience:

```text
Do you think AI started with ChatGPT?
```

The dream of making machines intelligent has existed for decades. What changed recently is that the conditions became right.

Earlier AI was limited by less data, weak computing power, and immature algorithms.

Memory line:

```text
The AI dream was old, but the timing was not ready.
```

---

# Slide 3 - What Changed Now?

## Three Forces Matured Together

| Force | Simple Meaning |
|---|---|
| **Big Data** | Internet, sensors, phones generate massive examples |
| **Algorithms** | Better learning methods — deep learning, transformers |
| **Computing Power** | GPUs and cloud made large-scale training affordable |

No single force was enough. The explosion happened when all three matured at the same time.

Trainer line:

```text
AI did not become powerful because of one invention. It became powerful because the full ecosystem became ready.
```

---

# Slide 4 - AI Family Tree

## How the AI World Is Organized

| Generation | Core Idea |
|---|---|
| **Rule-Based AI** (1950s-80s) | Human writes IF-THEN rules. Brittle. |
| **Machine Learning** (1990s-2010s) | Machine learns patterns from data instead of being told rules. |
| **Deep Learning** (2012+) | Many-layered neural networks learn complex patterns automatically. |
| **Generative AI** (2022+) | Creates new content — text, images, code, music. |
| **Agentic AI** (2024+) | Plans, uses tools, and takes actions autonomously. |

Each generation builds on the previous — they don't replace each other.

Memory line:

```text
Rule-based AI follows rules. Machine Learning learns. Deep Learning handles complexity. Generative AI creates. Agentic AI acts.
```

---

# Slide 5 - Traditional ML vs DL vs GenAI

## Clear Mental Map

| Term | Simple Meaning |
|---|---|
| Machine Learning | Learns patterns from data |
| Deep Learning | ML using deep neural networks |
| Generative AI | Creates new content |
| LLM | Generative AI focused on language |
| Agentic AI | Plans, uses tools, takes actions |

Simple hierarchy:

```text
AI
 ├── Rule-Based AI
 ├── Machine Learning
 │    └── Deep Learning
 │         └── Transformers → LLMs
 └── Generative AI
      └── Agentic AI
```

Memory line:

```text
LLMs are part of Generative AI. Generative AI often uses Deep Learning. Deep Learning is part of Machine Learning.
```

---

# Slide 6 - Data Science vs AI

## Connected but Different

| | Data Science | AI |
|---|---|---|
| **Goal** | Extract insights, inform decisions | Build systems that act intelligently |
| **Focus** | Understanding data, finding patterns | Automating decisions and actions |
| **Output** | Reports, dashboards, recommendations | Models, predictions, autonomous agents |

Machine Learning is the major overlap area.

Data Science often feeds into AI. Today we learn the Data Science foundations.

Trainer line:

```text
Data Science prepares and extracts value from data. AI uses data and algorithms to create intelligent behavior.
```

---

# Slide 7 - What Is Data Science?

## A Practical Definition

Data Science uses data to answer questions, find patterns, support decisions, and build data-driven solutions.

Three pillars:

| Pillar | Role |
|---|---|
| **Domain Knowledge** | Know what questions matter and what answers make sense |
| **Statistics** | Quantify patterns, uncertainty, and relationships |
| **Programming** | Automate analysis at scale |

You need all three. Statistics without domain knowledge finds meaningless patterns. Domain knowledge without data is just opinion.

Memory line:

```text
Data Science turns raw data into useful decisions.
```

---

# Slide 8 - The Data Science Lifecycle

## From Question to Decision

```text
1. Problem Understanding
2. Data Collection
3. Data Understanding / Inspection
4. Data Cleaning
5. Exploratory Data Analysis
6. Statistics
7. Visualization
8. Feature Preparation
9. Modeling (Day 2-3)
10. Evaluation (Day 2-3)
11. Tuning (Day 4)
12. Deployment (Day 5)
13. Monitoring (Day 5)
```

Today we cover Steps 1 through 8, plus Communication.

The lifecycle is **iterative**, not linear. Cleaning reveals new questions. Modeling failures send you back to feature preparation. Going back is the process working correctly.

Memory line:

```text
Start with the question, not the tool.
```

---

# Slide 9 - Data Science Is More Than Models

## Model Building Is Only One Part

Many beginners think Data Science means only machine learning models.

But real Data Science includes:

- Business understanding
- Data quality checks
- Exploratory analysis
- Statistical thinking
- Feature preparation
- Data storytelling
- Responsible decision-making

Trainer line:

```text
In real projects, understanding and preparing data often takes more effort than training the model.
```

---

# Slide 10 - Common Beginner Mistakes

## What We Will Avoid

Beginners often:

- Start coding without understanding the problem
- Jump to machine learning too early
- Ignore missing values and duplicates
- Treat every number as meaningful
- Use charts without a question
- Trust accuracy without checking mistakes
- Explain code but not insight
- Forget the final business decision

Memory line:

```text
This training builds the habit of asking why before asking how.
```

---

# Slide 11 - Python Essentials

## NumPy and Pandas

### NumPy — The Math Engine

Regular Python lists are slow for math. NumPy arrays are optimized for numerical computation.

| Capability | What It Gives You |
|---|---|
| Element-wise operations | Apply math to all values at once — no loops |
| Boolean filtering | Select values matching a condition |
| Built-in statistics | Mean, std, min, max, sum in one call |
| Multi-dimensional arrays | Rows and columns with axis-based operations |

NumPy is the foundation — every data science library in Python is built on top of it.

Memory line:

```text
NumPy gives Python fast math.
```

---

# Slide 12 - Pandas

## Why NumPy Alone Is Not Enough

Real data has column names, mixed types (numbers + text), and missing values. NumPy cannot handle that. Pandas gives us labeled tables.

| Concept | What It Is |
|---|---|
| **Series** | A single labeled column |
| **DataFrame** | A labeled table — rows and columns, like a spreadsheet |

| Operation | What It Does |
|---|---|
| Select | Pick specific columns or rows |
| Filter | Keep only rows matching a condition |
| Group and Aggregate | Split data into groups, compute stats per group |
| Sort | Order rows by a column's values |

NumPy = fast math. Pandas = structured tables. Together = the backbone of data science in Python.

Memory line:

```text
NumPy handles numbers. Pandas handles tables.
```

---

# Slide 13 - Step 1: Problem Understanding

## Before Touching Data, Answer These

| Question | Why It Matters |
|---|---|
| **What problem?** | Defines what you are looking for |
| **Who needs the answer?** | Shapes how you communicate results |
| **What decision depends on it?** | Ensures your work leads to action |
| **What action will follow?** | Grounds analysis in real-world impact |

Weak question:

```text
Analyze student data.
```

Better question:

```text
What factors influence student performance, and can we predict outcomes?
```

Memory line:

```text
A clear problem creates clear analysis.
```

---

# Slide 14 - Step 2: Data Collection

## Garbage In, Garbage Out

Without data, there is no data science. The quality and relevance of your data determines everything that follows.

| Source | Example |
|---|---|
| Structured | CSV files, databases, spreadsheets |
| Semi-structured | APIs, JSON, XML |
| Unstructured | Text, images, web scraping |
| Primary | Surveys, experiments you design |

Good collection questions:

- Is the data relevant to the problem?
- Is it reliable?
- Is it legal and ethical to use?
- Does it cover enough examples?

Memory line:

```text
Relevant and reliable data is better than simply more data.
```

---

# Slide 15 - Step 3: Data Understanding

## Look Before You Clean

Before cleaning, understand what you have. Inspect first, change later.

| What to Check | What It Tells You |
|---|---|
| **Shape** | How many rows and columns |
| **Data types** | Which columns are numbers vs text |
| **Unique values** | Spot inconsistencies in text columns |
| **Missing values** | Where are the gaps |
| **Duplicates** | Are any records repeated |
| **Value ranges** | Are numbers within valid bounds |

Trainer line:

```text
Inspection is how we learn the shape and health of the data. Like a doctor examining before prescribing.
```

---

# Slide 16 - Data Dictionary

## Every Column Needs Meaning

A data dictionary explains what each column means, its data type, and valid range.

If you do not understand the columns, you do not understand the data.

Without a data dictionary:

- Column names are guesses
- Valid ranges are unknown
- Cleaning decisions are arbitrary
- Results cannot be trusted

Memory line:

```text
A data dictionary is the contract between data and analyst.
```

---

# Slide 17 - Step 4: Data Cleaning

## Building Trust Before Analysis

Cleaning is 60-80% of a data scientist's work. Messy data leads to wrong conclusions.

**Rule:** Always work on a copy. Keep raw data untouched.

Professional workflow:

```text
Inspect
    -> Understand the issue
    -> Decide the cleaning rule
    -> Apply the cleaning rule
    -> Verify the result
```

Trainer line:

```text
Cleaning without inspection is guessing. Inspection turns cleaning into a reasoned decision.
```

---

# Slide 18 - Cleaning: Messy Text

## Same Meaning, Different Text

To humans, these may look similar:

```text
CSE, cse, Cse, CSE , cse
```

To software, these are five different category values.

Problems caused:

- Extra categories in counts
- Wrong group summaries
- Messy charts
- Broken filters

Fix: Strip whitespace, standardize case. Always check unique values after.

Memory line:

```text
Software treats different spelling as different data.
```

---

# Slide 19 - Cleaning: Duplicates

## Repeated Records Distort Analysis

Duplicates inflate counts, skew averages, and make patterns appear stronger than they are. A student counted twice looks like two students.

Ask before removing:

- Is the entire row repeated?
- Could the same person have multiple valid records?
- What does one row represent?

Memory line:

```text
One real event should not accidentally count twice.
```

---

# Slide 20 - Cleaning: Missing Values

## Empty Data Needs a Decision

| Strategy | When to Use |
|---|---|
| **Fill with median** | Numeric columns — median is robust to outliers |
| **Fill with mode** | Categorical columns — use the most common value |
| **Fill with "Unknown"** | When absence itself is informative |
| **Drop the row** | When very few rows are affected |
| **Investigate source** | When missingness is unexpected or risky |

Trainer line:

```text
There is no universal best fix. The right choice depends on the column and the project question.
```

---

# Slide 21 - Cleaning: Invalid vs Outlier

## Different Problems Need Different Decisions

| | Invalid | Outlier |
|---|---|---|
| **Definition** | Impossible value — violates real-world rules | Extreme but possible value |
| **Cause** | Data entry error, system bug | Natural variation, rare event |
| **Detection** | Domain knowledge | Statistical methods (IQR, z-score) |
| **Action** | Must fix — cap, replace, or remove | Investigate first — may be real |

Attendance of 110% is invalid. Study hours of 50/week is unusual but possible. Know the difference.

Memory line:

```text
Invalid values are wrong. Outliers are unusual. Do not confuse the two.
```

---

# Slide 22 - Cleaning: Before vs After

## Your Proof That Cleaning Worked

Always compare before and after. It is your evidence that cleaning worked and nothing was accidentally broken.

| Check | Before | After |
|---|---|---|
| Rows | Original count | After dedup |
| Missing values | Count per column | Should be 0 or justified |
| Unique categories | Messy count | Clean count |
| Value ranges | May have invalids | Within valid bounds |

Memory line:

```text
If you cannot show what changed, the cleaning is hard to trust.
```

---

# Slide 23 - Ethics and Privacy

## Data Work Affects People

| Principle | What It Means |
|---|---|
| **Privacy** | Student and personal records are legally protected |
| **Bias** | Check if your data or model treats any group unfairly |
| **Consent** | People should know their data is being analyzed |
| **Purpose** | Only use data for its intended purpose |

Technical skill without ethical awareness is dangerous.

Memory line:

```text
Good Data Science is not only accurate. It must also be responsible.
```

---

# Slide 24 - Step 5: Exploratory Data Analysis

## A Conversation Between Analyst and Data

EDA means exploring data before making strong conclusions. You ask questions, data answers through numbers and charts.

| Operation | Question It Answers |
|---|---|
| **Value counts** | How many in each category? |
| **Sorting** | Who are the top or bottom performers? |
| **Filtering** | Which records meet a condition? |
| **Grouping** | How do subgroups differ? |
| **Cross-tabulation** | How do two categories interact? |

EDA turns raw curiosity into structured findings.

Memory line:

```text
EDA is how we listen to the data before asking it to support decisions.
```

---

# Slide 25 - Step 6: Statistics Overview

## Summarize Data Without Reading Every Row

Statistics gives short answers to large tables.

| Big Idea | Question | Measures |
|---|---|---|
| **Center** | What is typical? | Mean, median, mode |
| **Spread** | How different are values? | Range, variance, std dev, IQR |
| **Shape** | Is the distribution symmetric or skewed? | Skewness |
| **Position** | Where does a value rank? | Percentiles, quartiles |
| **Relationship** | Do two columns move together? | Covariance, correlation |

Trainer line:

```text
Each statistic is useful because it answers a question. Do not start with formulas — start with questions.
```

---

# Slide 26 - Center: Mean, Median, Mode

## What Is a Typical Value?

The first question about any numeric column.

| Measure | What It Is | Best When |
|---|---|---|
| **Mean** | Sum divided by count | Data is symmetric, no outliers |
| **Median** | Middle value when sorted | Outliers or skewed data present |
| **Mode** | Most frequent value | Categorical data |

One outlier can drag the mean far from the true center. Median resists this pull. Always check both.

Memory line:

```text
Mean tells average. Median tells middle. Compare both before concluding.
```

---

# Slide 27 - Spread: Range, Variance, Std Dev

## Center Alone Is Not Enough

Two groups can have the same mean but very different spread.

| Measure | What It Captures | Limitation |
|---|---|---|
| **Range** | Max minus min | Uses only 2 values — one outlier wrecks it |
| **Variance** | Average squared distance from mean | Units are squared — hard to interpret |
| **Std Dev** | Square root of variance | Back to original units — interpretable |

Why square the differences? Raw differences cancel out (negatives + positives = 0). Squaring keeps them all positive.

Std Dev tells you: on average, how far values sit from the mean. Small std = consistent. Large std = variable.

Memory line:

```text
Average tells center. Spread tells consistency.
```

---

# Slide 28 - Percentiles and IQR

## Position in the Data

Mean and std dev assume a bell curve. Percentiles work for any distribution shape.

| Concept | Meaning |
|---|---|
| **Percentile** | The value below which a given percentage of data falls |
| **Q1 (25th)** | 25% of data falls below this |
| **Q2 (50th)** | The median |
| **Q3 (75th)** | 75% of data falls below this |
| **IQR** | Q3 minus Q1 — the range of the middle 50% |

Outlier detection: values beyond Q1 minus 1.5 times IQR or Q3 plus 1.5 times IQR are flagged as outliers.

Memory line:

```text
Percentiles describe position. IQR measures the spread of the middle half.
```

---

# Slide 29 - Distribution and Skewness

## The Shape Tells the Real Story

Knowing the mean is 50 tells you nothing about whether most students scored near 50 or half scored 20 and half scored 80. Shape reveals what is really happening.

| Skewness | Shape | Mean vs Median |
|---|---|---|
| Near 0 | Symmetric | Mean and median are close |
| Positive (right) | Long tail to the right | Mean is greater than median |
| Negative (left) | Long tail to the left | Mean is less than median |

When skewed, mean gets pulled toward the tail. Median stays put.

Memory line:

```text
Skewness tells which side has the longer tail.
```

---

# Slide 30 - Covariance and Correlation

## Do Two Columns Move Together?

**Covariance** tells direction but depends on scale — hard to compare.

**Correlation** standardizes to a fixed range.

| Correlation Value | Strength |
|---|---|
| 0.0 to 0.3 | Weak |
| 0.3 to 0.7 | Moderate |
| 0.7 to 1.0 | Strong |

Sign tells direction: positive means same direction, negative means opposite.

**Correlation does NOT prove causation.** Two things can move together without one causing the other.

Memory line:

```text
Correlation is evidence of association, not proof of cause.
```

---

# Slide 31 - Grouped Statistics

## Overall Averages Can Hide Important Differences

The overall average might be 50, but Department A averages 60 and Department B averages 40. The combined number masks a real gap.

Always break down by relevant categories before drawing conclusions from overall numbers.

Also check group size — a high average from two rows is not strong evidence.

Trainer line:

```text
Grouping reveals what the overall number hides.
```

---

# Slide 32 - describe() Dashboard

## One Command, Eight Statistics

Instead of writing 8 separate calculations, one command gives count, mean, std, min, percentiles, and max.

| Statistic | What It Tells You |
|---|---|
| **Count** | Completeness — are values missing? |
| **Mean and Std** | Center and spread |
| **Min and Max** | Range — are values within valid bounds? |
| **25%, 50%, 75%** | Distribution shape — where most data falls |

The first thing experienced data scientists run on any new dataset.

Memory line:

```text
describe() is your statistics dashboard.
```

---

# Slide 33 - Step 7: Visualization

## Seeing Patterns Clearly

Charts help humans see patterns faster than tables. But a chart without a question is decoration.

Before choosing a chart, ask: What question am I answering?

| Question | Right Chart |
|---|---|
| Compare group averages | Bar chart |
| How many in each category | Count plot |
| How is data distributed | Histogram |
| How does spread differ across groups | Box plot |
| Is there a relationship between two numbers | Scatter plot |
| Is there a trend over ordered values | Line chart |

Memory line:

```text
The question chooses the chart.
```

---

# Slide 34 - Reading a Box Plot

## Compact Summary of Spread

| Element | Meaning |
|---|---|
| **Middle line** | Median |
| **Box** | Middle 50% of values (IQR) |
| **Whiskers** | Extend to 1.5 times IQR |
| **Points beyond whiskers** | Possible outliers |

Box plots let you compare center, spread, and outliers across groups at a glance.

A point outside the whiskers may be a real rare case, not necessarily a mistake. Investigate before removing.

Memory line:

```text
The box shows the middle half. The whiskers show the typical range.
```

---

# Slide 35 - Chart Quality

## Make Charts Trustworthy

A readable chart needs:

- Clear title that states the question or finding
- Labeled axes with units
- Meaningful color — not decoration
- Honest scale — not exaggerated
- Sorted bars when order helps comparison

Weak title: "Chart 1"

Strong title: "Average Total Marks by Department"

Memory line:

```text
A chart should clarify, not manipulate.
```

---

# Slide 36 - Step 8: Feature Preparation

## Translating Human Data Into Model-Ready Data

ML models only understand numbers. They cannot read "CSE" or "Female." And they are sensitive to scale — a column ranging 0 to 100 will dominate one ranging 0 to 1 just because the numbers are bigger.

Feature preparation converts human-readable data into model-ready data.

Three tasks:

- Create new features from existing columns
- Scale numeric columns to comparable ranges
- Encode text categories as numbers

Memory line:

```text
Clean data is human-readable. Prepared data is model-readable.
```

---

# Slide 37 - Creating New Features

## Relationships Between Columns

Sometimes the most useful information is not in any single column but in the relationship between columns.

| Approach | Purpose |
|---|---|
| Ratios | Relative performance |
| Combinations | Aggregate measures |
| Differences | Change or gap between two measures |

A well-crafted feature can be more predictive than any raw column.

Memory line:

```text
New features reveal patterns the raw data does not show directly.
```

---

# Slide 38 - Scaling

## Putting Features on the Same Playing Field

Without scaling, features with larger ranges dominate smaller ones.

| Method | Result | When to Use |
|---|---|---|
| **Standard Scaling** | Mean equals 0, Std equals 1 | Algorithms assuming normal distribution |
| **Min-Max Normalization** | Values in 0 to 1 | Algorithms needing bounded inputs |

Standard scaling answers: how far from average?

Min-Max answers: where between minimum and maximum?

Scaling does not change the shape of the data — it just makes all features comparable.

Memory line:

```text
Scaling compares distance from average. Normalization compares position in a range.
```

---

# Slide 39 - Encoding Categorical Variables

## Categories Must Become Numbers

| Situation | Method | Why |
|---|---|---|
| No natural order | **One-hot encoding** | Creates separate 0/1 columns per category |
| Meaningful order | **Ordered mapping** | Preserves ranking |
| Binary (2 values) | **0/1 mapping** | Simple and sufficient |
| IDs and names | **Do not encode** | No predictive value |

Wrong encoding creates wrong patterns. A model should not think "CSE is greater than CE" just because you assigned them 3 and 1.

Memory line:

```text
One-hot encoding avoids fake order. Ordered mapping is only for real order.
```

---

# Slide 40 - Step 9: Communication and Decision

## Data Science Is Incomplete Without Communication

An insight nobody acts on has zero value.

A good report has four components:

| Component | Purpose |
|---|---|
| **Findings** | What did the data reveal? State clearly. |
| **Evidence** | What charts and numbers support each finding? |
| **Caution** | What are the limitations? What could be wrong? |
| **Recommendation** | What action should be taken based on findings? |

Memory line:

```text
A good analyst does not only show output. A good analyst explains what it means.
```

---

# Slide 41 - Observation Writing

## Turn Numbers Into Meaning

Weak observation:

```text
The mean is 49.2.
```

Better observation:

```text
The average total marks is 49.2, while the median is 49.1, suggesting a roughly symmetric distribution.
```

Stronger observation:

```text
The average total marks is 49.2. ME department averages highest at 50.8, while ECE is lowest at 48.4. The difference is small and may not be statistically significant given the sample size.
```

Pattern: statistic plus value plus meaning plus caution.

Memory line:

```text
A statistic becomes useful when you explain what it means.
```

---

# Slide 42 - The Iterative Nature

## Data Science Is Not a Straight Line

In real projects, you often go back:

```text
EDA finds a data issue
    -> return to cleaning

Model performs poorly
    -> return to features

Stakeholder asks a better question
    -> return to problem understanding
```

This is not failure. This is how better solutions are built.

Memory line:

```text
Iteration is the process working correctly.
```

---

# Slide 43 - Day 1 Recap

## What We Covered

| Step | What You Learned |
|---|---|
| AI World | Three forces, AI family tree, where DS fits |
| Python Essentials | NumPy for math, Pandas for tables |
| Problem Understanding | Start with the question, not the tool |
| Data Collection | Quality and relevance determine everything |
| Data Understanding | Look before you clean |
| Data Cleaning | Fix text, duplicates, missing, invalid |
| EDA | Filter, sort, group to explore patterns |
| Statistics | Center, spread, shape, relationships |
| Visualization | Right chart for the right question |
| Feature Preparation | Scale, encode, engineer for models |
| Communication | Findings plus evidence plus caution plus recommendation |

Memory line:

```text
Day 1 builds the ground. Later days build models on that ground.
```

---

# Slide 44 - What Comes Next

## Five-Day Journey

| Day | Focus |
|---|---|
| **Day 1** | EDA — question to decision (today) |
| **Day 2** | Supervised Learning — Regression (predict final exam marks) |
| **Day 3** | Supervised Learning — Classification (predict pass/fail) |
| **Day 4** | Model Tuning and Clustering |
| **Day 5** | Neural Networks and Generative AI |

Same dataset across all five days. Today's cleaned data is tomorrow's model input.

Trainer line:

```text
Everything we cleaned and prepared today feeds directly into the models we build starting tomorrow.
```

---

# Slide 45 - Discussion

## Think Like a Data Scientist

Ask learners:

```text
You have student performance data. What is the first thing you should do?
```

Follow-up questions:

- What is the problem you are solving?
- What data quality issues might exist?
- What statistics would you check first?
- What chart would answer your first question?
- How would you explain a finding to a non-technical faculty member?

Trainer line:

```text
If you can answer these questions, you are thinking like a data scientist.
```

---

# Gamma Prompt

```text
Create a professional beginner-friendly training deck titled "Day 1: Exploratory Data Analysis — From Question to Decision".
Use a clean modern technical design, dark theme, clear visual hierarchy, left-aligned tables, simple diagrams, strong section dividers, and trainer-ready speaker notes.
Flow: AI World (why AI became powerful, AI family tree, DS vs AI), Python essentials framing (NumPy and Pandas), then full Data Science lifecycle — problem understanding, data collection, data understanding, data cleaning (text, duplicates, missing, invalid vs outlier, before/after), ethics, EDA, statistics (center, spread, percentiles, skewness, correlation, grouped stats, describe), visualization (chart selection, box plots, chart quality), feature preparation (new features, scaling, encoding), communication (findings + evidence + caution + recommendation), iteration, recap, and five-day roadmap.
Avoid emojis. Avoid cartoon style. Use professional icons, simple process visuals, and clean tables.
```
