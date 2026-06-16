# Section 6: Scaling, Normalization, and Encoding

## Gamma-Ready Deck

Audience:

```text
Beginner learners who have cleaned, summarized, and visualized data, and are ready to prepare columns for later analysis and machine learning.
```

Training intent:

```text
Teach preprocessing as column preparation.
Explain numeric scaling and categorical encoding with simple examples before showing code.
```

Core message:

```text
Clean data is easier for humans to read.
Preprocessed data is easier for later workflows and models to use.
Scaling prepares numeric columns. Encoding prepares categorical columns.
```

---

# Slide 1 - Title

## Scaling, Normalization, and Encoding

### Preparing Data for Later Workflows

In this section, we will learn:

- Why preprocessing matters
- Why numeric scale can affect analysis
- Standard scaling
- Min-max normalization
- `fit`, `transform`, and `fit_transform`
- Why categories need encoding
- One-hot encoding
- Ordered mapping
- How to check and save preprocessed data

Speaker note:

```text
Position this section as the bridge from human-readable cleaned data to model-readable prepared data. Keep it practical and avoid advanced ML depth.
```

---

# Slide 2 - Why Preprocessing Matters

## Good Columns Make Later Work Easier

Preprocessing means converting columns into useful forms.

Two common needs:

- Numeric columns may be on very different scales
- Text categories may need numeric representation

Example:

```text
monthly_spend: 700 to 1600
visits_per_month: 1 to 6
membership: Gold, Silver, Bronze
```

Memory line:

```text
Preprocessing prepares columns for the next step.
```

---

# Slide 3 - Cleaned vs Preprocessed Data

## Different Purposes

Cleaned data:

- Human-readable
- Corrected for basic quality problems
- Useful for EDA and reports

Preprocessed data:

- Transformed for later workflows
- May include scaled numeric columns
- May include encoded category columns
- Useful for modeling and repeatable pipelines

Trainer line:

```text
Cleaned data is understandable. Preprocessed data is usable by algorithms.
```

---

# Slide 4 - Column Preparation Map

## What Should Happen to Each Column?

| Column Type | Example | Common Preparation |
|---|---|---|
| Identifier | customer_id | Keep for reference, not a model feature |
| Text label | name | Keep for readability, usually not a feature |
| Numeric | monthly_spend | Scale or normalize |
| Category | city | One-hot encode |
| Ordered category | membership | Ordered mapping if order is meaningful |

Memory line:

```text
Different columns need different preparation.
```

---

# Slide 5 - Scale

## What Does Scale Mean?

Scale means the size range of values in a column.

Example:

```text
monthly_spend: 700, 850, 1200, 1450
visits_per_month: 2, 3, 4, 5
```

Monthly spend uses larger numbers.

Visits uses smaller numbers.

Trainer line:

```text
When columns use very different ranges, some later calculations can be dominated by larger-valued columns.
```

---

# Slide 6 - Why Scale Can Matter

## Large Numbers Can Dominate

Imagine comparing customers using:

- Monthly spend
- Visits per month

If spend is hundreds or thousands, and visits is single digits, spend may influence calculations more strongly.

Simple idea:

```text
Large numeric range can overpower small numeric range.
```

Memory line:

```text
Scaling helps numeric columns speak on a more comparable level.
```

---

# Slide 7 - Original Values Still Matter

## Do Not Lose Business Meaning

Original values are easy to explain:

```text
monthly_spend = 1200 rupees
visits_per_month = 4 visits
```

Scaled values are useful for algorithms:

```text
monthly_spend_standard_scaled = 0.35
```

Important:

```text
Keep readable columns while learning so you can interpret results.
```

Trainer line:

```text
Preprocessing helps workflows, but original units help humans understand.
```

---

# Slide 8 - Standard Scaling

## Distance From Average

Standard scaling changes values so:

- Mean is near 0
- Standard deviation is near 1

Formula idea:

```text
standard scaled value = (value - mean) / standard deviation
```

Simple meaning:

```text
How far is this value from average?
```

Memory line:

```text
Standard scaling answers: how far from average?
```

---

# Slide 9 - Reading Standard Scaled Values

## Above or Below Average

Interpretation:

| Value | Simple Meaning |
|---:|---|
| 0 | Close to average |
| Positive | Above average |
| Negative | Below average |
| Large absolute value | Farther from average |

Example:

```text
-1.2 means below average
0.0 means near average
1.5 means above average
```

Trainer line:

```text
Standard scaled values can be negative. That is expected.
```

---

# Slide 10 - Standard Scaling Example

## Monthly Spend

Original values:

```text
700, 850, 1200, 1450, 1600
```

After standard scaling:

```text
Values are centered around 0
Values show distance from average
```

Plain-English explanation:

```text
A positive scaled spend means the customer spends above average.
```

Memory line:

```text
Standard scaling changes the unit from rupees to distance-from-average.
```

---

# Slide 11 - Min-Max Normalization

## Position Between Minimum and Maximum

Min-max normalization changes values to a fixed range, usually 0 to 1.

Formula idea:

```text
normalized value = (value - minimum) / (maximum - minimum)
```

Simple meaning:

```text
Where does this value sit between the smallest and largest value?
```

Memory line:

```text
Normalization answers: where between min and max?
```

---

# Slide 12 - Reading Normalized Values

## 0 to 1

Interpretation:

| Value | Simple Meaning |
|---:|---|
| 0 | Smallest value in that column |
| 1 | Largest value in that column |
| 0.5 | Around the middle of min and max |
| Between 0 and 1 | Relative position |

Example:

```text
0.75 means closer to the maximum than the minimum.
```

Trainer line:

```text
Normalized values should usually stay between 0 and 1 when using the same fitted range.
```

---

# Slide 13 - Scaling vs Normalization

## Similar Goal, Different Meaning

| Method | Result | Simple Meaning |
|---|---|---|
| Standard scaling | Mean near 0, standard deviation near 1 | How far from average? |
| Min-max normalization | Values between 0 and 1 | Where between min and max? |
| Original values | Actual business units | What does this mean in real life? |

Memory line:

```text
Scaling compares distance from average. Normalization compares position in a range.
```

---

# Slide 14 - When to Use Which?

## Practical Beginner Guidance

Use standard scaling when:

- You care about distance from average
- Later methods are sensitive to scale
- Values may not need a strict 0 to 1 range

Use min-max normalization when:

- You want values in a fixed 0 to 1 range
- You want simple relative position
- The minimum and maximum are meaningful

Trainer line:

```text
For Day 1, the goal is to understand both ideas, not memorize every modeling rule.
```

---

# Slide 15 - `fit`, `transform`, `fit_transform`

## Scalers Learn From Data

Scalers need to learn settings.

| Step | Meaning |
|---|---|
| `fit` | Learn mean, standard deviation, min, or max |
| `transform` | Apply the learned transformation |
| `fit_transform` | Learn and apply on the same data |

Example:

```text
fit learns the average spend.
transform uses that average to scale spend values.
```

Memory line:

```text
Fit learns. Transform applies.
```

---

# Slide 16 - Data Leakage Caution

## Do Not Learn From Test Data

In real modeling workflows:

```text
Fit preprocessing on training data.
Transform validation or test data using the same fitted object.
```

Why?

- Test data should represent unseen data
- Learning from it gives unfair information
- This can make results look better than they really are

Trainer line:

```text
This is called data leakage. Day 1 only introduces the idea, but it matters later.
```

---

# Slide 17 - Encoding

## Turning Categories Into Numbers

Many later workflows need numbers.

Text categories:

```text
Gold, Silver, Bronze
Mumbai, Delhi, Chennai
```

Need a numeric representation.

Encoding means:

```text
Convert category values into numeric columns.
```

Memory line:

```text
Encoding makes categories usable for numeric workflows.
```

---

# Slide 18 - Why Not Just Number Every Category?

## Fake Order Problem

Bad idea:

```text
Mumbai = 1
Delhi = 2
Chennai = 3
```

This can imply:

```text
Chennai is greater than Delhi
Delhi is greater than Mumbai
```

But city names do not have natural order.

Trainer line:

```text
Do not create fake order where no real order exists.
```

---

# Slide 19 - One-Hot Encoding

## Separate 0/1 Columns

One-hot encoding creates one column per category.

Example city values:

```text
Mumbai, Delhi, Chennai
```

One-hot columns:

```text
city_Mumbai
city_Delhi
city_Chennai
```

Each row gets:

```text
1 for the matching city
0 for other cities
```

Memory line:

```text
One-hot encoding avoids fake order.
```

---

# Slide 20 - One-Hot Example

## City Encoding

| City | city_Mumbai | city_Delhi | city_Chennai |
|---|---:|---:|---:|
| Mumbai | 1 | 0 | 0 |
| Delhi | 0 | 1 | 0 |
| Chennai | 0 | 0 | 1 |

Plain-English explanation:

```text
Each city becomes its own yes/no column.
```

Trainer line:

```text
For beginners, one-hot encoding is easier to understand when all category columns are visible.
```

---

# Slide 21 - Validate One-Hot Encoding

## Check the Rows

For one-hot encoding of one column, each row should usually have one `1`.

Example:

```text
city_Mumbai + city_Delhi + city_Chennai = 1
```

If the sum is not 1:

- Category may be missing
- Encoding may be incomplete
- There may be multi-label data

Memory line:

```text
After encoding, check that the rows still make sense.
```

---

# Slide 22 - Encoding Multiple Columns

## More Categories, More Columns

We can one-hot encode multiple columns:

- City
- Membership
- Signup month

Result:

```text
Original categorical columns become many 0/1 columns.
```

Possible issue:

```text
Many categories can create many columns.
```

Trainer line:

```text
Encoding expands the dataset horizontally.
```

---

# Slide 23 - `drop_first`

## Why One Column May Be Removed

Some workflows use:

```text
drop_first=True
```

This removes one dummy column to reduce repeated information.

For Day 1:

```text
Keep all columns because it is easier to learn and inspect.
```

Memory line:

```text
Learning first: keep encoding readable.
```

---

# Slide 24 - Ordered Mapping

## Use Only When Order Is Real

Some categories have meaningful order.

Example:

```text
Bronze < Silver < Gold
```

Mapping:

```text
Bronze = 1
Silver = 2
Gold = 3
```

This is reasonable because membership level has rank.

Trainer line:

```text
Ordered mapping is useful only when the category order is real.
```

---

# Slide 25 - Ordered Mapping Caution

## Do Not Force Order

Bad ordered mapping:

```text
Mumbai = 1
Delhi = 2
Chennai = 3
```

Why bad?

- Cities do not have numeric rank
- The numbers imply false distance
- Later calculations may be misleading

Memory line:

```text
Only ordered categories should get ordered numbers.
```

---

# Slide 26 - Unknown Categories

## What If a Category Is New?

Real projects may receive new values later.

Example:

```text
Training data cities: Mumbai, Delhi, Chennai
New data city: Pune
```

Questions:

- Should it become `Unknown`?
- Should the encoder handle unknown values?
- Should the category list be updated?

Trainer line:

```text
Preprocessing decisions must handle future data, not only today's file.
```

---

# Slide 27 - Missing Categories Before Encoding

## Clean Before Encoding

Before encoding, check:

- Missing values
- Extra spaces
- Different casing
- Spelling variants
- Unexpected labels

Example:

```text
Gold
gold
 GOLD
```

Clean first:

```text
Gold
```

Memory line:

```text
Encoding preserves category problems if you do not clean first.
```

---

# Slide 28 - Row Alignment

## Keep Rows Matched Correctly

When combining transformed columns:

- Row order must remain the same
- Index alignment matters
- Row count should match original data
- No accidental missing values should appear

Good check:

```text
original rows == preprocessed rows
```

Trainer line:

```text
A preprocessing table is only useful if the transformed values still belong to the correct rows.
```

---

# Slide 29 - Preprocessed Table

## What Should It Include?

A beginner-friendly preprocessed table may include:

- Customer ID
- Name
- Original city and membership for readability
- Standard-scaled numeric columns
- Normalized numeric columns
- One-hot encoded category columns
- Ordered membership level

Memory line:

```text
Keep readable columns while learning, and add transformed columns beside them.
```

---

# Slide 30 - Quality Checks Before Saving

## Verify the Prepared Data

Before saving, check:

- Row count
- Column count
- Missing values
- Encoded column names
- Scaled value summary
- Normalized value range
- Ordered mapping missing values

Simple checklist:

```text
Rows match?
Missing values okay?
Columns clear?
```

Trainer line:

```text
Preprocessing is incomplete until the prepared table is checked.
```

---

# Slide 31 - Save Preprocessed Data

## Create a Handoff File

Save prepared data separately:

```text
customer_activity_preprocessed.csv
```

Why?

- Later notebooks can reuse it
- The workflow becomes repeatable
- Raw, cleaned, and preprocessed files stay separate
- Future modeling steps have a prepared starting point

Memory line:

```text
Separate files preserve the project journey.
```

---

# Slide 32 - File Journey

## Raw to Cleaned to Preprocessed

Simple project file flow:

```text
customer_activity_raw.csv
    -> customer_activity_clean.csv
    -> customer_activity_preprocessed.csv
```

Meaning:

- Raw: original learning dataset
- Cleaned: quality issues handled
- Preprocessed: transformed for later workflows

Trainer line:

```text
Each file represents a different stage of trust and readiness.
```

---

# Slide 33 - Common Beginner Mistakes

## What We Will Avoid

Beginners often:

- Think scaling and normalization are the same
- Forget standard-scaled values can be negative
- Expect normalized values to go outside 0 and 1
- Create fake order for unordered categories
- Encode before cleaning text categories
- Drop readable columns too early
- Forget row alignment
- Forget to check before saving

Memory line:

```text
Preprocessing changes data, so every change needs a reason and a check.
```

---

# Slide 34 - Simple Example Summary

## Customer Activity Preparation

Original columns:

```text
monthly_spend
visits_per_month
city
membership
```

Prepared columns:

```text
monthly_spend_standard_scaled
visits_per_month_normalized
city_Mumbai
city_Delhi
membership_level
```

Trainer line:

```text
The prepared table contains the same customers, but the columns are easier for later workflows to use.
```

---

# Slide 35 - Preprocessing Workflow

## A Practical Sequence

Use this sequence:

```text
1. Identify column roles
2. Choose numeric transformations
3. Fit and apply scalers
4. Choose categorical encodings
5. Validate transformed columns
6. Combine into one table
7. Check row count and missing values
8. Save preprocessed data
```

Memory line:

```text
Prepare columns deliberately, then verify.
```

---

# Slide 36 - Notebook 06 Mapping

## How This Section Connects to the Lab

In Notebook 06, learners will practice:

- Comparing numeric column scales
- Standard scaling
- Min-max normalization
- Reading scaler settings
- One-hot encoding
- Validating one-hot rows
- Ordered mapping
- Creating a preprocessing-ready table
- Saving and reloading preprocessed data

Trainer line:

```text
Notebook 06 turns column preparation concepts into Pandas and scikit-learn practice.
```

---

# Slide 37 - Trainer Demo Flow

## Recommended Live Sequence

Suggested sequence:

1. Show original columns
2. Compare numeric ranges
3. Standard scale numeric columns
4. Normalize numeric columns
5. Explain fit and transform
6. Inspect category values
7. One-hot encode city
8. Map membership order
9. Combine transformed columns
10. Verify and save

Memory line:

```text
Transform one column type at a time.
```

---

# Slide 38 - Discussion Prompt

## Choose the Transformation

Ask learners:

```text
Should city be encoded with one-hot encoding or ordered mapping?
```

Expected answer:

```text
One-hot encoding, because city has no natural order.
```

Follow-up:

```text
Should membership be one-hot encoded or ordered mapped?
```

Expected thinking:

```text
Either can be useful, but ordered mapping is reasonable if Bronze < Silver < Gold is meaningful.
```

---

# Slide 39 - Section Summary

## What We Learned

Key takeaways:

- Preprocessing prepares columns for later workflows
- Scaling handles numeric columns with different ranges
- Standard scaling shows distance from average
- Normalization shows position between minimum and maximum
- Fit learns and transform applies
- Encoding turns categories into numeric form
- One-hot encoding avoids fake order
- Ordered mapping is only for real order
- Preprocessed data should be checked and saved separately

Memory line:

```text
Good preprocessing makes later analysis safer and more repeatable.
```

---

# Slide 40 - Transition to Hands-On

## Now We Prepare the Data

Next, we move into Notebook 06.

We will:

- Load the cleaned customer dataset
- Scale and normalize numeric columns
- Encode categorical columns
- Build a preprocessing-ready table
- Save the preprocessed dataset for later use

Closing trainer line:

```text
After this step, learners will understand how clean data starts becoming ready for future machine learning work.
```

---

# Gamma Prompt

```text
Create a professional beginner-friendly training deck titled "Scaling, Normalization, and Encoding: Preparing Data for Later Workflows".
Use a clean modern technical design, light theme, left-aligned tables, simple before-and-after column visuals, and trainer-ready speaker notes.
Focus on practical preprocessing: cleaned vs preprocessed data, numeric scale, standard scaling, min-max normalization, fit/transform/fit_transform, data leakage caution, one-hot encoding, ordered mapping, unknown categories, row alignment, quality checks, saving preprocessed data, and notebook mapping.
Avoid emojis. Avoid cartoon style. Use professional icons, simple process diagrams, and clean tables.
```
