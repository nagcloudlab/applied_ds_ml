# Section 2: Data Science Lifecycle and Project Flow

## Gamma-Ready Deck

Audience:

```text
Beginner learners who have just completed the AI World and Data Science introduction.
```

Training intent:

```text
Move from big-picture AI context into the practical Data Science way of working.
Show learners how a real data project flows from question to decision.
```

Core message:

```text
Data Science is not a random collection of tools. It is a disciplined lifecycle for turning messy data into useful decisions.
```

---

# Slide 1 - Title

## Data Science Lifecycle

### From Question to Decision

In this section, we will learn:

- How a data science project starts
- Why problem understanding comes before coding
- How raw data becomes useful insight
- Where statistics and visualization fit
- When machine learning becomes useful
- How Day 1 labs connect to the full project flow

Speaker note:

```text
This section should make learners feel that Data Science is a structured journey, not just Python commands.
```

---

# Slide 2 - Why This Section Matters

## Tools Are Not the Starting Point

Many beginners start with:

- Python
- Pandas
- Charts
- Machine learning algorithms
- AI tools

But professionals start with:

- The problem
- The decision
- The data
- The risk
- The expected outcome

Memory line:

```text
Start with the question, not the tool.
```

---

# Slide 3 - The Big Idea

## Data Science Is a Flow

Data Science is a flow that converts:

```text
Raw Data
    -> Clean Data
    -> Understood Data
    -> Insight
    -> Decision
    -> Action
```

Important point:

```text
The goal is not to produce a notebook. The goal is to support a better decision.
```

---

# Slide 4 - Simple Project Story

## A Practical Example

Imagine an organization wants to understand customer activity.

Questions:

- Which customers are active?
- Which customers are less active?
- What spending patterns are visible?
- Which groups need attention?
- What actions can improve engagement?

This is a Data Science problem because we need:

- Data
- Analysis
- Interpretation
- Communication
- Decision support

---

# Slide 5 - Lifecycle Overview

## The End-to-End Data Science Lifecycle

```text
1. Problem Understanding
2. Data Collection
3. Data Understanding
4. Data Cleaning
5. Exploratory Data Analysis
6. Statistics
7. Visualization
8. Feature Preparation
9. Modeling
10. Evaluation
11. Communication
12. Deployment or Decision
13. Monitoring and Improvement
```

Speaker note:

```text
Tell learners that Day 1 will deeply cover the early and most important foundation steps.
```

---

# Slide 6 - Step 1

## Problem Understanding

Before touching data, ask:

- What problem are we solving?
- Who needs the answer?
- What decision will be made?
- What action will follow?
- What does success look like?
- What should not happen?

Memory line:

```text
A clear problem creates clear analysis.
```

---

# Slide 7 - Weak vs Strong Problem Statement

## Better Questions Produce Better Work

Weak problem statement:

```text
Analyze customer data.
```

Better problem statement:

```text
Understand customer activity patterns and identify which customer groups may need attention.
```

Why better?

- It has a clear focus
- It suggests useful columns
- It guides analysis
- It connects to possible action

---

# Slide 8 - Business Question vs Data Question

## Translate the Problem

Business question:

```text
How can we improve customer engagement?
```

Data questions:

- How many customers are active?
- What is the average monthly spend?
- Which membership groups spend more?
- Which customers visit less often?
- Are visits and spend related?

Trainer line:

```text
Data Science often starts by converting a business question into data questions.
```

---

# Slide 9 - Step 2

## Data Collection

Data may come from:

- CSV files
- Excel files
- Databases
- APIs
- Web applications
- Surveys
- Transaction systems
- Logs
- Sensors

Good collection questions:

- Is this data relevant?
- Is it reliable?
- Is it recent enough?
- Is it allowed to use?
- Is anything important missing?

---

# Slide 10 - Data Collection Warning

## More Data Is Not Always Better

More data can help, but only if it is useful.

Bad data can create:

- Wrong conclusions
- Biased results
- Misleading charts
- Poor model performance
- Bad decisions

Memory line:

```text
Relevant and reliable data is better than simply more data.
```

---

# Slide 11 - Step 3

## Data Understanding

Before cleaning deeply, first understand the dataset.

Ask:

- How many rows are there?
- How many columns are there?
- What does each column mean?
- Which columns are numbers?
- Which columns are categories?
- Which column values look unusual?
- What is the unit of measurement?

Notebook connection:

```text
This is where Pandas inspection commands become useful.
```

---

# Slide 12 - Data Dictionary

## Every Column Needs Meaning

A data dictionary explains:

- Column name
- Column meaning
- Data type
- Allowed values
- Example values
- Business meaning

Example:

| Column | Meaning | Example |
|---|---|---|
| monthly_spend | Customer spend per month | 250.50 |
| visits_per_month | Number of monthly visits | 8 |
| membership | Customer membership group | Gold |

Memory line:

```text
If you do not understand the columns, you do not understand the data.
```

---

# Slide 13 - Step 4

## Data Cleaning

Real data is usually messy.

Common issues:

- Missing values
- Duplicate rows
- Wrong data types
- Extra spaces
- Inconsistent spelling
- Invalid numbers
- Impossible dates
- Outliers

Trainer line:

```text
Data cleaning is not boring work. It is trust-building work.
```

---

# Slide 14 - Cleaning Example

## Same Meaning, Different Text

Raw category values:

```text
Gold
gold
 GOLD
Gold Member
```

To humans, these may mean the same thing.

To software, these are different values.

Cleaning goal:

```text
Standardize categories before analysis.
```

---

# Slide 15 - Missing Values

## Missing Data Needs a Decision

Missing values can happen because:

- Data was not entered
- System failed to capture it
- The value does not apply
- The source file is incomplete
- The data was removed for privacy

Common options:

- Keep as missing
- Fill with a suitable value
- Remove affected rows
- Remove affected columns
- Investigate the source

Memory line:

```text
Never fill missing values blindly.
```

---

# Slide 16 - Outliers

## Unusual Values Need Review

An outlier is a value very different from most values.

Examples:

- Age = 300
- Monthly spend = 999999
- Visits per month = -5
- Attendance = 150%

Outliers may be:

- Data entry mistakes
- Real rare cases
- System errors
- Important events

Trainer line:

```text
Do not delete outliers automatically. Understand them first.
```

---

# Slide 17 - Step 5

## Exploratory Data Analysis

EDA means exploring data before making conclusions.

EDA helps us answer:

- What is typical?
- What is unusual?
- Which groups are different?
- Which columns may be related?
- What patterns are visible?
- What data quality issues remain?

Memory line:

```text
EDA is the conversation between the analyst and the data.
```

---

# Slide 18 - EDA Questions

## Ask Better Questions

Useful EDA questions:

- What is the average monthly spend?
- Which membership group spends more?
- Which group visits more often?
- Are visits and spend related?
- Are there customers with very low activity?
- Are there invalid or suspicious records?

Notebook connection:

```text
Groupby, sorting, summary statistics, and plots help answer these questions.
```

---

# Slide 19 - Step 6

## Statistics

Statistics helps summarize data clearly.

Key ideas:

- Mean: typical average
- Median: middle value
- Mode: most common value
- Range: minimum to maximum
- Variance: spread measured with squared distance
- Standard deviation: typical distance from average
- Correlation: relationship direction and strength

Trainer line:

```text
Statistics helps us describe patterns without reading every row.
```

---

# Slide 20 - Why Spread Matters

## Average Alone Is Not Enough

Two groups can have the same average but different spread.

Example:

```text
Group A spend: 100, 100, 100
Group B spend: 50, 100, 150
```

Both averages are 100.

But Group B is more variable.

Memory line:

```text
Average tells center. Spread tells consistency.
```

---

# Slide 21 - Step 7

## Visualization

Charts help humans see patterns quickly.

Use charts to:

- Compare groups
- See distributions
- Detect outliers
- Show relationships
- Communicate insights

Common chart choices:

| Question | Chart |
|---|---|
| Compare groups | Bar chart |
| See spread | Box plot |
| See distribution | Histogram |
| See relationship | Scatter plot |
| See trend | Line chart |

---

# Slide 22 - Chart Thinking

## Do Not Draw Charts Randomly

Before creating a chart, ask:

- What question is this chart answering?
- What should the audience notice?
- Is the chart type suitable?
- Are labels clear?
- Is the scale honest?
- Is the chart too crowded?

Memory line:

```text
A chart is useful only when it makes a point clearer.
```

---

# Slide 23 - Step 8

## Feature Preparation

Feature preparation means creating useful columns for analysis or modeling.

Examples:

- Convert dates into month or year
- Group ages into age bands
- Create total spend
- Create average score
- Encode categories
- Scale numeric columns
- Remove identifier columns

Trainer line:

```text
Feature preparation turns raw columns into useful signals.
```

---

# Slide 24 - Feature Preparation Example

## Raw Column to Useful Feature

Raw columns:

```text
monthly_spend
visits_per_month
```

Possible new feature:

```text
spend_per_visit = monthly_spend / visits_per_month
```

Why useful?

- It gives spending intensity
- It combines two columns into one meaningful measure
- It may reveal behavior not visible from raw values alone

---

# Slide 25 - Step 9

## Modeling

Modeling means using algorithms to learn patterns.

Modeling can help with:

- Predicting a number
- Predicting a category
- Grouping similar records
- Detecting unusual behavior
- Recommending items
- Generating content

Important point:

```text
Not every data science project needs machine learning.
```

---

# Slide 26 - When Modeling Is Needed

## Analysis vs Model

Use analysis when:

- You need to understand past behavior
- You need a clear report
- You need a dashboard
- You need descriptive insights

Use modeling when:

- You need prediction
- You need automation
- You need scoring
- You need pattern learning at scale

Memory line:

```text
Use the simplest method that answers the question well.
```

---

# Slide 27 - Step 10

## Evaluation

Evaluation asks:

- Are the results correct?
- Are the insights useful?
- Are charts and summaries clear?
- Are assumptions documented?
- Are model errors acceptable?
- Does the solution help the decision?

For Day 1:

```text
Evaluation means checking whether our analysis is trustworthy and understandable.
```

---

# Slide 28 - Step 11

## Communication

Data Science is incomplete if findings are not communicated.

Good communication includes:

- Clear summary
- Key findings
- Supporting charts
- Business meaning
- Limitations
- Recommended action

Trainer line:

```text
A good analyst does not only show output. A good analyst explains what it means.
```

---

# Slide 29 - Step 12

## Deployment or Decision

The output may become:

- A report
- A dashboard
- A notebook
- A presentation
- A data pipeline
- A model API
- A business rule
- An automated workflow

Memory line:

```text
The project becomes useful when someone can use the result.
```

---

# Slide 30 - Step 13

## Monitoring and Improvement

After deployment or decision-making, keep checking:

- Is the data changing?
- Are patterns changing?
- Are users still getting value?
- Are errors increasing?
- Are decisions still fair?
- Should the analysis or model be updated?

Trainer line:

```text
Real data science work is iterative. It improves over time.
```

---

# Slide 31 - The Iterative Nature

## Data Science Is Not a Straight Line

In real projects, we often go back:

```text
EDA finds a data issue
    -> return to cleaning

Model performs poorly
    -> return to features

Stakeholder asks a better question
    -> return to problem understanding
```

Memory line:

```text
Iteration is not failure. Iteration is how better solutions are built.
```

---

# Slide 32 - Professional Principles

## How to Think Like a Data Scientist

Principles:

- Start with the decision
- Understand the columns
- Check data quality
- Separate facts from assumptions
- Compare before concluding
- Visualize with purpose
- Explain in simple language
- Respect privacy and fairness
- Document your work

---

# Slide 33 - Responsible Data Science

## Data Work Affects People

Responsible questions:

- Is the data allowed to be used?
- Is sensitive information protected?
- Could the analysis create unfair decisions?
- Are assumptions transparent?
- Can the result be explained?
- Should a human review the final decision?

Trainer line:

```text
Good Data Science is not only accurate. It must also be responsible.
```

---

# Slide 34 - Beginner Mistakes

## What We Will Avoid

Common mistakes:

- Starting with code before the problem
- Ignoring column meaning
- Cleaning without documenting
- Trusting averages alone
- Creating charts without questions
- Jumping to ML too early
- Reporting output without insight
- Ignoring limitations

Memory line:

```text
Do not just produce output. Produce understanding.
```

---

# Slide 35 - Day 1 Project Flow

## What We Will Practice

Our Day 1 hands-on flow:

```text
Setup
    -> Python basics
    -> Load dataset
    -> Inspect data
    -> Clean data
    -> Summarize data
    -> Explore patterns
    -> Visualize insights
    -> Prepare data for later ML
    -> Mini project report
```

This gives learners the first complete data journey.

---

# Slide 36 - Unified Dataset Approach

## One Dataset, Many Lessons

Using one connected dataset helps learners understand:

- How work continues from one step to the next
- Why cleaning affects statistics
- Why statistics supports visualization
- Why visualization supports explanation
- Why preparation matters before ML

Memory line:

```text
Connected learning is stronger than disconnected examples.
```

---

# Slide 37 - End-to-End Demo Preview

## What the Demo Will Show

The end-to-end demo will show:

- How to load a dataset
- How to inspect rows and columns
- How to detect data quality issues
- How to clean selected problems
- How to summarize numeric columns
- How to compare groups
- How to create charts
- How to write final insights

Speaker note:

```text
This slide prepares learners for the notebooks. It tells them why each notebook exists.
```

---

# Slide 38 - Notebook Mapping

## How Slides Connect to Labs

| Concept | Notebook Connection |
|---|---|
| Setup and workflow | Notebook 01 |
| Python, NumPy, Pandas | Notebook 02 |
| Data inspection and cleaning | Notebook 03 |
| Statistics | Notebook 04 |
| Visualization | Notebook 05 |
| Data preparation | Notebook 06 |
| Mini project | Notebook 07 |

Trainer line:

```text
Each notebook is one part of the same data science journey.
```

---

# Slide 39 - Trainer Delivery Flow

## Recommended Teaching Order

Recommended flow:

1. Explain the lifecycle
2. Show the end-to-end roadmap
3. Introduce the dataset
4. Demonstrate one small inspection
5. Let learners repeat
6. Add cleaning
7. Add statistics
8. Add visualization
9. End with a mini report

Memory line:

```text
Teach the journey, not only the command.
```

---

# Slide 40 - Section Summary

## What We Learned

Key takeaways:

- Data Science starts with a problem
- Data must be understood before cleaning
- Cleaning builds trust
- EDA reveals patterns
- Statistics summarizes data
- Visualization communicates patterns
- Feature preparation creates useful signals
- Modeling is useful when prediction or automation is needed
- Communication turns analysis into action
- Data Science is iterative and responsible

---

# Slide 41 - Transition to Labs

## Now We Move to Hands-On

Next, we start Notebook 01.

We will learn:

- How to set up the working environment
- How notebooks are used
- How code and markdown work together
- How to follow lab instructions
- How this training will move from concept to practice

Closing line:

```text
Now we understand the full journey. Next, we start walking through it step by step.
```

---

# Gamma Prompt

```text
Create a professional beginner-friendly training deck titled "Data Science Lifecycle: From Question to Decision".
Use a clean modern technical design, white or light theme, left-aligned tables, strong section dividers, simple lifecycle diagrams, and trainer-ready storytelling.
Focus on the disciplined flow of Data Science: problem understanding, data collection, data understanding, cleaning, EDA, statistics, visualization, feature preparation, modeling, evaluation, communication, deployment or decision, monitoring, principles, responsible data science, and notebook mapping.
Avoid emojis. Avoid cartoon style. Use professional icons, simple process visuals, and clean tables.
```
