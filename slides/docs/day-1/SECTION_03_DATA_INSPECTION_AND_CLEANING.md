# Section 3: Data Inspection and Cleaning

## Gamma-Ready Deck

Audience:

```text
Beginner learners who understand the Data Science lifecycle and are ready to inspect and clean their first dataset.
```

Training intent:

```text
Move learners from project flow into hands-on data quality thinking.
Teach inspection before cleaning, and cleaning as a decision-making process rather than random code.
```

Core message:

```text
Data inspection helps us understand what we have.
Data cleaning helps us make the data trustworthy enough for analysis.
Good analysts do not clean blindly. They inspect, decide, clean, and verify.
```

---

# Slide 1 - Title

## Data Inspection and Cleaning

### Building Trust Before Analysis

In this section, we will learn:

- Why data quality matters
- How to inspect rows, columns, and data types
- How to find missing values
- How to detect duplicates
- How to clean text inconsistencies
- How to handle unusual values
- How to verify cleaned data
- Why raw and cleaned data should be saved separately

Speaker note:

```text
Position this section as the bridge between lifecycle theory and practical notebook work. Learners should understand that cleaning is not a side task. It is what makes later analysis trustworthy.
```

---

# Slide 2 - Why This Section Matters

## Bad Data Creates Bad Decisions

If data has quality problems, then:

- Averages may be wrong
- Charts may be misleading
- Groups may be counted incorrectly
- Patterns may be false
- Reports may lose trust
- Models may learn the wrong behavior

Memory line:

```text
Before trusting analysis, trust the data.
```

---

# Slide 3 - The Big Idea

## Inspect Before You Clean

A beginner mistake is to start fixing data immediately.

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

# Slide 4 - What Is Data Inspection?

## First Look at the Dataset

Data inspection means checking what the dataset contains before making changes.

We inspect:

- Number of rows
- Number of columns
- Column names
- First few rows
- Last few rows
- Data types
- Missing values
- Duplicate records
- Unusual values
- Category spelling

Memory line:

```text
Inspection is how we learn the shape and health of the data.
```

---

# Slide 5 - What Is Data Cleaning?

## Improving Data Quality

Data cleaning means fixing or handling problems that can harm analysis.

Common cleaning actions:

- Remove duplicate rows
- Fill missing values
- Standardize text
- Fix incorrect data types
- Correct invalid values
- Review outliers
- Rename unclear columns
- Save a cleaned version

Important idea:

```text
Cleaning does not mean making data perfect. It means making it reliable enough for the current purpose.
```

---

# Slide 6 - Raw Data vs Cleaned Data

## Do Not Lose the Original

Raw data:

- Original source version
- Useful for audit
- Should not be overwritten too early
- Helps us repeat or review cleaning

Cleaned data:

- Working version after cleaning rules
- Used for statistics, charts, and reports
- Should be saved separately

Simple flow:

```text
Raw data
    -> inspect
    -> clean
    -> verify
    -> cleaned data
```

Memory line:

```text
Raw data is the source of truth. Cleaned data is the working version.
```

---

# Slide 7 - Example Dataset Story

## Customer Activity Data

In the hands-on notebook, we use a small customer activity dataset.

Columns may include:

- Customer ID
- Name
- City
- Membership type
- Monthly spend
- Visits per month
- Signup month

Possible business questions:

- Which membership group spends more?
- Which city has more customers?
- Are visits related to spending?
- Which rows need cleaning before analysis?

Trainer line:

```text
Keep the dataset small on purpose. Small data lets beginners inspect problems manually before automating.
```

---

# Slide 8 - Dataset Anatomy

## Rows, Columns, and Cells

Simple table language:

| Term | Simple Meaning | Example |
|---|---|---|
| Row | One record | One customer |
| Column | One variable | monthly_spend |
| Cell | One value | 1200 |
| Data type | Kind of value | number, text, date |

Memory line:

```text
Rows are records. Columns are variables. Cells are values.
```

---

# Slide 9 - First Inspection Questions

## What Should We Ask First?

Before cleaning, ask:

- How many rows are present?
- How many columns are present?
- What are the column names?
- What does each column mean?
- Are data types reasonable?
- Are there missing values?
- Are there duplicate rows?
- Do category values look consistent?
- Do numeric values look possible?

Notebook connection:

```text
This is where Pandas commands like shape, head, info, isna, duplicated, and describe become useful.
```

---

# Slide 10 - Pandas Inspection Commands

## The First Toolkit

Common commands:

| Command | Purpose |
|---|---|
| `.shape` | Count rows and columns |
| `.head()` | View first rows |
| `.tail()` | View last rows |
| `.columns` | See column names |
| `.info()` | Check data types and non-null counts |
| `.describe()` | Summarize numeric columns |
| `.isna().sum()` | Count missing values |
| `.duplicated().sum()` | Count duplicate rows |

Trainer line:

```text
These commands are not just code. They are questions we ask the dataset.
```

---

# Slide 11 - Shape

## How Big Is the Dataset?

The shape tells us:

```text
(rows, columns)
```

Example:

```text
(10, 7)
```

Means:

- 10 records
- 7 variables

Why it matters:

- Confirms expected size
- Helps detect accidental row loss
- Helps compare before and after cleaning

Memory line:

```text
Always know how many rows you started with.
```

---

# Slide 12 - First Rows

## Look at the Data Like a Human

The first rows help us see:

- Example values
- Column meaning
- Text formatting
- Missing values
- Suspicious values
- Whether columns match expectations

Good analyst habit:

```text
Read a few rows manually before writing many cleaning commands.
```

Trainer line:

```text
Manual inspection is not unprofessional. It is how we build intuition before automation.
```

---

# Slide 13 - Data Types

## Does Each Column Have the Right Kind of Value?

Common data types:

| Type | Simple Meaning | Example |
|---|---|---|
| integer | Whole number | 5 |
| float | Decimal number | 1200.50 |
| object/string | Text | Mumbai |
| datetime | Date or time | 2026-06-15 |
| boolean | True or False | True |

Why data types matter:

- Numeric summaries need numeric columns
- Dates need date handling
- Text categories need text cleaning
- Wrong types can break calculations

Memory line:

```text
The same value can behave differently if the data type is wrong.
```

---

# Slide 14 - Missing Values

## Empty Data Needs a Decision

Missing values may appear as:

- Blank cells
- `NaN`
- `None`
- `null`
- `Unknown`
- `Not available`

Missing values can happen because:

- Data was not entered
- The value does not apply
- The source system failed
- The data was removed
- The file is incomplete

Memory line:

```text
Missing does not always mean mistake. It means investigate.
```

---

# Slide 15 - Missing Value Decisions

## How Can We Handle Missing Data?

Possible actions:

| Action | Use When |
|---|---|
| Keep missing | Missingness itself may be meaningful |
| Fill numeric value | A suitable statistic makes sense |
| Fill category | A label like Unknown is useful |
| Remove row | Very few rows affected and row is unusable |
| Remove column | Column is mostly missing and not important |
| Investigate source | Missingness is unexpected or risky |

Trainer line:

```text
There is no universal best missing-value fix. The right choice depends on the column and the project question.
```

---

# Slide 16 - Numeric Missing Values

## Filling Numbers Carefully

For numeric columns, common fill choices include:

- Mean
- Median
- Zero
- A domain-specific value

Beginner guidance:

- Median is often safer when values have outliers
- Mean can be pulled by extreme values
- Zero should be used only when zero has real meaning

Example:

```text
monthly_spend missing -> fill with median spend
```

Memory line:

```text
Never fill a number unless you can explain why that value makes sense.
```

---

# Slide 17 - Categorical Missing Values

## Filling Text Categories

For categorical columns, common choices include:

- `Unknown`
- Most common category
- A domain-specific label
- Keep as missing

Example:

```text
city missing -> Unknown
```

Why this can help:

- Keeps the row
- Makes missingness visible
- Avoids pretending we know the real city

Trainer line:

```text
Using Unknown is honest when we do not know the actual category.
```

---

# Slide 18 - Duplicate Rows

## Repeated Records Can Distort Analysis

A duplicate row is the same record repeated.

Duplicates can cause:

- Overcounting customers
- Inflated totals
- Wrong averages
- Misleading charts
- Repeated evidence in reports

Common command:

```text
duplicated()
```

Memory line:

```text
One real event should not accidentally count twice.
```

---

# Slide 19 - Duplicate Decisions

## Remove or Keep?

Not every similar row is a duplicate.

Ask:

- Is the entire row repeated?
- Is the customer ID repeated?
- Could the same customer have multiple valid transactions?
- Does each row represent a customer, visit, order, or event?
- What does the data dictionary say?

Trainer line:

```text
Duplicate decisions depend on what one row represents.
```

---

# Slide 20 - Text Inconsistency

## Same Meaning, Different Text

To humans, these may look similar:

```text
Mumbai
 mumbai
MUMBAI
Mumbai 
```

To software, these are different category values.

Problems caused:

- Extra categories
- Wrong counts
- Wrong group summaries
- Messy charts

Memory line:

```text
Software treats different spelling as different data.
```

---

# Slide 21 - Text Cleaning

## Standardize Text Categories

Common text cleaning steps:

- Remove extra spaces
- Use consistent case
- Replace known variants
- Keep category labels clear

Example:

```text
strip spaces
convert to title case
map known variants
```

Pandas idea:

```text
.str.strip().str.title()
```

Trainer line:

```text
Text cleaning makes category counts meaningful.
```

---

# Slide 22 - Invalid Values

## Values That Should Not Exist

Invalid values break business meaning.

Examples:

- Monthly spend = -500
- Visits per month = -3
- Age = 300
- Attendance = 150%
- Signup month = "Banana"

Ask:

- Is the value impossible?
- Is it a data entry issue?
- Can it be corrected?
- Should it be set to missing?
- Should the source be checked?

Memory line:

```text
Invalid values are not outliers. They are values that violate the rules of the data.
```

---

# Slide 23 - Outliers

## Unusual Does Not Always Mean Wrong

An outlier is very different from most values.

Outliers can be:

- Real rare cases
- Important customers
- Data entry mistakes
- System errors
- One-time events

Example:

```text
Most monthly spend values: 700 to 1600
One value: 8000
```

Trainer line:

```text
Do not delete outliers automatically. First ask whether they are real, wrong, or important.
```

---

# Slide 24 - Invalid Value vs Outlier

## Different Problems Need Different Decisions

| Situation | Example | Meaning | Action |
|---|---|---|---|
| Invalid value | spend = -500 | Violates business rule | Fix, remove, or mark missing |
| Outlier | spend = 8000 | Unusual but possible | Investigate before changing |
| Missing value | city is blank | Unknown value | Decide fill, keep, or investigate |
| Duplicate | same row repeated | Repeated record | Remove if truly duplicate |

Memory line:

```text
Wrong, missing, repeated, and unusual are different data problems.
```

---

# Slide 25 - Cleaning Rules

## Document the Decision

Every cleaning step should answer:

- What issue did we find?
- Which column was affected?
- What rule did we apply?
- Why is the rule reasonable?
- How many rows changed?
- Did we verify the result?

Example:

```text
Issue: Missing monthly_spend
Rule: Fill with median monthly_spend
Reason: Median is stable when values vary
Verification: Missing count is now 0
```

Trainer line:

```text
Cleaning is easier to trust when the rule is documented.
```

---

# Slide 26 - Copy Before Cleaning

## Keep a Safe Working Version

Good workflow:

```text
clean_customers = raw_customers.copy()
```

Why this matters:

- Raw data stays unchanged
- Mistakes can be reviewed
- Cleaning can be repeated
- Before and after can be compared

Memory line:

```text
Do not destroy your original evidence.
```

---

# Slide 27 - Verify After Cleaning

## Did the Cleaning Work?

After cleaning, rerun checks:

- Row count
- Missing value count
- Duplicate count
- Data types
- Category values
- Numeric minimum and maximum
- Sample rows

Simple flow:

```text
Before cleaning checks
    -> cleaning actions
    -> after cleaning checks
```

Trainer line:

```text
Cleaning is incomplete until verification passes.
```

---

# Slide 28 - Row Count Awareness

## Know What Changed

Cleaning can change row count.

Examples:

- Removing duplicates reduces rows
- Removing invalid rows reduces rows
- Filling missing values keeps rows
- Standardizing text keeps rows

Ask:

- How many rows before cleaning?
- How many rows after cleaning?
- Did the change make sense?
- Can I explain why rows changed?

Memory line:

```text
If rows disappeared, you should know why.
```

---

# Slide 29 - Data Quality Report

## Summarize the Health of the Dataset

A simple quality report can include:

| Check | Before | After |
|---|---:|---:|
| Rows | 10 | 9 |
| Missing values | 2 | 0 |
| Duplicate rows | 1 | 0 |
| Invalid spend values | 1 | 0 |

Why it helps:

- Shows progress
- Builds trust
- Helps trainers and stakeholders understand the work
- Makes cleaning repeatable

---

# Slide 30 - Saving Cleaned Data

## Create a Reusable File

After cleaning, save a new file:

```text
customer_activity_clean.csv
```

Why save cleaned data?

- Later notebooks can reuse it
- Analysis becomes repeatable
- Raw and cleaned versions stay separate
- The workflow is easier to audit

Memory line:

```text
Save clean data separately so the project can continue safely.
```

---

# Slide 31 - Cleaning Is Iterative

## One Pass Is Not Always Enough

Cleaning often repeats:

```text
Inspect
    -> clean
    -> summarize
    -> find another issue
    -> clean again
    -> verify again
```

Examples:

- A chart reveals an impossible value
- A group summary reveals inconsistent spelling
- A missing count reveals a column problem
- A model later reveals suspicious records

Trainer line:

```text
Finding another issue later is normal. Good workflows make it easy to go back.
```

---

# Slide 32 - Ethics and Privacy

## Clean Data Responsibly

Data cleaning can affect people.

Responsible questions:

- Is private information protected?
- Are cleaning decisions fair?
- Did we remove rows from one group more than another?
- Are assumptions documented?
- Could a missing value represent a real accessibility or system issue?
- Should sensitive columns be masked or removed?

Memory line:

```text
Data quality work is also responsibility work.
```

---

# Slide 33 - Common Beginner Mistakes

## What We Will Avoid

Beginners often:

- Start cleaning before inspecting
- Overwrite raw data
- Fill missing values blindly
- Delete outliers automatically
- Ignore duplicate rows
- Ignore data types
- Treat text variations as separate real categories
- Forget to verify after cleaning
- Forget to explain cleaning choices

Trainer line:

```text
The goal is not to run many commands. The goal is to make trustworthy decisions about the data.
```

---

# Slide 34 - Before and After Thinking

## Cleaning Should Have Evidence

For each cleaning action, compare before and after.

Example:

```text
Before:
missing monthly_spend = 1

Action:
fill with median

After:
missing monthly_spend = 0
```

Memory line:

```text
If you cannot show what changed, the cleaning is hard to trust.
```

---

# Slide 35 - Notebook 03 Mapping

## How This Section Connects to the Lab

In Notebook 03, learners will practice:

- Creating a messy dataset
- Inspecting rows and columns
- Checking data types
- Counting missing values
- Detecting duplicate rows
- Creating a cleaning copy
- Standardizing text
- Removing duplicates
- Filling missing numeric values
- Filling missing categorical values
- Handling unusual values
- Saving cleaned data

Trainer line:

```text
The notebook is not only about Pandas syntax. It is about building the habit of inspecting, deciding, cleaning, and verifying.
```

---

# Slide 36 - Trainer Demo Flow

## Recommended Live Sequence

Suggested sequence:

1. Show the raw dataset
2. Ask learners what looks wrong
3. Run shape and head
4. Run info
5. Count missing values
6. Find duplicates
7. Clean one issue at a time
8. Verify after every major step
9. Save the cleaned dataset

Memory line:

```text
One issue, one decision, one verification.
```

---

# Slide 37 - Discussion Prompt

## Think Like an Analyst

Ask learners:

```text
If monthly_spend is missing for one customer, what should we do?
```

Possible answers:

- Fill with mean
- Fill with median
- Leave missing
- Remove the row
- Ask the source system

Trainer response:

```text
All of these can be reasonable in different situations. The important skill is explaining the decision.
```

---

# Slide 38 - Mini Case

## Cleaning Decisions in Context

Scenario:

```text
Customer data has one missing city, one missing monthly_spend, one duplicate row, and one negative monthly_spend.
```

Possible cleaning plan:

- Fill missing city with `Unknown`
- Fill missing monthly spend with median
- Remove exact duplicate row
- Replace negative monthly spend with a reasonable value or investigate source
- Verify missing values and duplicates again

Trainer line:

```text
The cleaning plan should be simple, explainable, and checked.
```

---

# Slide 39 - Section Summary

## What We Learned

Key takeaways:

- Data inspection comes before cleaning
- Shape, head, info, missing counts, and duplicate checks are first tools
- Missing values require decisions
- Duplicate handling depends on what one row represents
- Text values must be standardized before category analysis
- Invalid values and outliers are not the same thing
- Cleaning rules should be documented
- Cleaned data should be verified and saved separately

Memory line:

```text
Trustworthy analysis starts with trustworthy data.
```

---

# Slide 40 - Transition to Hands-On

## Now We Inspect and Clean Data

Next, we move into Notebook 03.

We will:

- Create a messy customer dataset
- Inspect data quality
- Clean selected problems
- Verify the cleaned result
- Save the cleaned dataset for statistics and visualization

Closing trainer line:

```text
From this point onward, every chart, statistic, and insight depends on the quality of the cleaned data.
```

---

# Gamma Prompt

```text
Create a professional beginner-friendly training deck titled "Data Inspection and Cleaning: Building Trust Before Analysis".
Use a clean modern technical design, light theme, left-aligned tables, simple before-and-after visuals, and trainer-ready speaker notes.
Focus on practical data quality thinking: inspect before cleaning, rows and columns, data types, missing values, duplicates, text inconsistency, invalid values, outliers, raw vs cleaned data, verification, documentation, ethics, and transition to a hands-on Pandas notebook.
Avoid emojis. Avoid cartoon style. Use professional icons, simple process diagrams, and clean tables.
```
