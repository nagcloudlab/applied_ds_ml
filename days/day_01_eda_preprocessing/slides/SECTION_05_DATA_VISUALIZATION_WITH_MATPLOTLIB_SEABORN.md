# Section 5: Data Visualization with Matplotlib and Seaborn

## Gamma-Ready Deck

Audience:

```text
Beginner learners who have cleaned data and calculated basic statistics, and are ready to communicate patterns visually.
```

Training intent:

```text
Teach charts as answers to questions, not decoration.
Help learners choose the right chart, read it correctly, and write plain-English observations from visual evidence.
```

Core message:

```text
Visualization helps humans see patterns quickly.
A good chart starts with a question, uses the right chart type, and makes the evidence easier to explain.
```

---

# Slide 1 - Title

## Data Visualization

### Seeing Patterns Clearly

In this section, we will learn:

- Why visualization matters in EDA
- How to choose charts based on questions
- Bar charts
- Line charts
- Histograms
- Box plots
- Scatter plots
- Count plots
- How to format and interpret charts

Speaker note:

```text
Frame visualization as communication. Learners should not think the goal is to create a pretty chart. The goal is to make a pattern easier to see and explain.
```

---

# Slide 2 - Why Visualization Matters

## Tables Are Not Always Enough

Tables are useful, but charts help us quickly see:

- Which category is highest
- Where values concentrate
- Whether values are spread out
- Whether unusual values exist
- Whether two numeric columns move together
- Whether a trend rises or falls

Memory line:

```text
Charts help our eyes find patterns faster.
```

---

# Slide 3 - Start With the Question

## Do Not Draw Charts Randomly

Before choosing a chart, ask:

- What question am I answering?
- Which columns are involved?
- Are the columns numeric or categorical?
- Am I comparing, showing distribution, or showing relationship?
- What should the audience notice first?

Trainer line:

```text
A chart without a question is decoration. A chart with a question is evidence.
```

---

# Slide 4 - Chart Selection Map

## Match the Chart to the Question

| Question | Useful Chart | Example |
|---|---|---|
| Compare categories | Bar chart | Average spend by membership |
| Count categories | Count plot | Customers by city |
| Show ordered trend | Line chart | Spend by signup month |
| See distribution | Histogram | Monthly spend distribution |
| Compare spread | Box plot | Spend by membership |
| Compare two numbers | Scatter plot | Visits vs spend |

Memory line:

```text
The question chooses the chart.
```

---

# Slide 5 - Chart Anatomy

## What Every Chart Needs

A readable chart usually needs:

- Clear title
- X-axis label
- Y-axis label
- Meaningful scale
- Useful color choice
- Legend only when needed
- Enough whitespace

Simple checklist:

```text
Can someone understand this chart in 10 seconds?
```

Trainer line:

```text
If the reader needs a long explanation just to read the chart, the chart needs improvement.
```

---

# Slide 6 - Column Types Matter

## Numeric vs Categorical

Categorical columns:

- City
- Membership
- Signup month

Numeric columns:

- Monthly spend
- Visits per month

Examples:

| Column Type | Good Chart |
|---|---|
| Category count | Count plot or bar chart |
| Numeric distribution | Histogram |
| Numeric by category | Bar chart or box plot |
| Numeric vs numeric | Scatter plot |

Memory line:

```text
Chart choice depends on column type.
```

---

# Slide 7 - Bar Chart

## Compare Categories

A bar chart compares values across categories.

Example question:

```text
Which membership type has the highest average monthly spend?
```

Data needed:

- Category: membership
- Measure: average monthly spend

Plain-English observation:

```text
Gold membership customers have the highest average monthly spend in this dataset.
```

---

# Slide 8 - Reading a Bar Chart

## Look at Height or Length

When reading a bar chart:

- Identify the tallest or longest bar
- Compare category sizes
- Read the axis label
- Check whether the measure is count, sum, average, or median
- Do not assume color means something unless there is a legend

Memory line:

```text
Bar height shows the comparison.
```

---

# Slide 9 - Bar Chart Mistake

## Count vs Average

These are different questions:

```text
How many customers are in each membership group?
```

and

```text
What is the average monthly spend by membership group?
```

The first uses counts.

The second uses averages.

Trainer line:

```text
Always know what the y-axis is measuring.
```

---

# Slide 10 - Count Plot

## Count Rows by Category

A count plot shows how many rows belong to each category.

Example question:

```text
How many customers are in each city?
```

Useful for:

- City counts
- Membership counts
- Signup month counts
- Product category counts

Memory line:

```text
Count plots answer: how many rows?
```

---

# Slide 11 - Reading a Count Plot

## Frequency, Not Value

Count plot interpretation:

- Tallest bar has the most rows
- Shortest bar has the fewest rows
- It does not show average spend
- It does not show total revenue unless the column is revenue count

Example observation:

```text
Mumbai and Delhi have the highest customer counts in this small dataset.
```

Trainer line:

```text
Customer count is not the same as customer value.
```

---

# Slide 12 - Line Chart

## Show Ordered Change

A line chart shows change across an ordered sequence.

Good x-axis examples:

- Date
- Month
- Week number
- Year
- Ordered age group

Example question:

```text
How does average monthly spend change across signup months?
```

Memory line:

```text
Line charts need meaningful order.
```

---

# Slide 13 - Line Chart Caution

## Do Not Connect Unordered Categories

Poor line chart x-axis examples:

- City
- Product category
- Membership labels with no clear numeric order

Why?

```text
The line suggests movement from one category to the next.
```

Trainer line:

```text
If the x-axis has no real order, a line chart can mislead the audience.
```

---

# Slide 14 - Histogram

## See Distribution

A histogram shows how values are distributed across ranges.

Example question:

```text
Where do monthly spend values concentrate?
```

Histogram tells us:

- Low-value ranges
- Middle-value ranges
- High-value ranges
- Concentration
- Possible skewness

Memory line:

```text
Histogram shows where numeric values fall.
```

---

# Slide 15 - Reading a Histogram

## Bars Are Ranges

In a histogram:

- Each bar represents a value range
- Bar height shows how many values fall in that range
- Wider or narrower bins can change the detail level
- Small datasets should be interpreted carefully

Example observation:

```text
Most monthly spend values appear concentrated around the middle ranges.
```

Trainer line:

```text
Do not read a histogram bar as one exact value. It usually represents a range.
```

---

# Slide 16 - Histogram Bin Size

## Detail Level Matters

Bins are the ranges used by a histogram.

Few bins:

- Simpler picture
- Less detail

Many bins:

- More detail
- Can look noisy with small data

Memory line:

```text
Bins change how the distribution appears.
```

---

# Slide 17 - Box Plot

## Compare Spread

A box plot summarizes distribution and spread.

Useful question:

```text
How does monthly spend vary by membership group?
```

Box plots help show:

- Median
- Middle 50% of values
- Spread
- Possible outliers
- Group differences

Trainer line:

```text
Box plots are compact summaries of spread.
```

---

# Slide 18 - Reading a Box Plot

## The Main Parts

| Box Plot Part | Simple Meaning |
|---|---|
| Middle line | Median |
| Box | Middle 50% of values |
| Whiskers | Typical low and high range |
| Points outside whiskers | Possible unusual values |

Memory line:

```text
The box shows the middle half of the data.
```

---

# Slide 19 - Box Plot Caution

## Possible Outlier Does Not Mean Wrong

A point outside the whiskers may be:

- A real high-value customer
- A rare but valid case
- A data entry issue
- A signal worth investigating

Do not automatically delete it.

Trainer line:

```text
A chart can flag a value for review, but it does not make the cleaning decision for us.
```

---

# Slide 20 - Scatter Plot

## Compare Two Numeric Columns

A scatter plot compares two numeric variables.

Example question:

```text
Do customers with more visits also tend to spend more?
```

Data needed:

- X-axis: visits per month
- Y-axis: monthly spend

Memory line:

```text
Each dot is one row.
```

---

# Slide 21 - Reading a Scatter Plot

## Look for Pattern Direction

Scatter plot patterns:

| Pattern | Meaning |
|---|---|
| Upward pattern | Same-direction movement |
| Downward pattern | Opposite-direction movement |
| Cloud with no direction | Weak or no clear relationship |
| Separate clusters | Groups may behave differently |

Example observation:

```text
The scatter plot suggests visits and spending move together somewhat.
```

---

# Slide 22 - Scatter Plot Caution

## Association Is Not Cause

A scatter plot can suggest association.

It cannot prove cause.

Example:

```text
More visits and higher spend appear together.
```

But it does not prove:

```text
More visits caused higher spend.
```

Memory line:

```text
Scatter plots show relationships, not proof of cause.
```

---

# Slide 23 - Color in Charts

## Use Color With Meaning

Good color use:

- Highlight one key category
- Separate groups
- Show membership type
- Keep one color for one meaning

Poor color use:

- Too many colors
- Random colors
- Color without legend
- Color used only for decoration

Trainer line:

```text
Color should reduce confusion, not add confusion.
```

---

# Slide 24 - Chart Titles

## State the Question

Weak title:

```text
Chart 1
```

Better title:

```text
Average Monthly Spend by Membership
```

Strong title:

```text
Gold Customers Have the Highest Average Monthly Spend
```

Memory line:

```text
A title should help the reader know what to look for.
```

---

# Slide 25 - Axis Labels

## Say What Is Measured

Axis labels should answer:

- What is on the x-axis?
- What is on the y-axis?
- Is the measure count, average, total, or percentage?
- What units are used?

Examples:

```text
X-axis: Membership
Y-axis: Average Monthly Spend
```

Trainer line:

```text
Unlabeled axes force the audience to guess.
```

---

# Slide 26 - Sorting Bars

## Make Comparisons Easier

Sorted bars are easier to read.

Examples:

- Highest to lowest average spend
- Largest to smallest customer count
- Lowest to highest score

Why it helps:

- Main pattern is easier to see
- Reader can compare quickly
- Less visual searching

Memory line:

```text
Sort bars when order helps comparison.
```

---

# Slide 27 - Horizontal Bar Charts

## Useful for Long Labels

Horizontal bars work well when:

- Category names are long
- Many categories exist
- You want easy label reading

Example:

```text
Customer Count by City
```

Trainer line:

```text
Use horizontal bars when vertical labels become crowded.
```

---

# Slide 28 - Annotating Charts

## Highlight the Main Evidence

Annotation means adding a small label to guide attention.

Useful for:

- Highest value
- Lowest value
- Important threshold
- Possible outlier
- Main takeaway

Example:

```text
Highest: Mumbai, 3 customers
```

Memory line:

```text
Annotation tells the reader what not to miss.
```

---

# Slide 29 - Pair Charts With Tables

## Show the Numbers Behind the Picture

A chart shows the pattern.

A table shows exact values.

Example:

| Membership | Average Spend |
|---|---:|
| Gold | 1417 |
| Silver | 992 |
| Bronze | 863 |

Trainer line:

```text
Charts and tables support each other. Charts show pattern; tables show exact evidence.
```

---

# Slide 30 - Misleading Charts

## Technically Correct Can Still Mislead

Common problems:

- Missing title
- Missing axis labels
- Y-axis scale exaggerates differences
- Too many colors
- Wrong chart type
- Line chart for unordered categories
- Small dataset shown as a big conclusion

Memory line:

```text
A chart should clarify, not manipulate.
```

---

# Slide 31 - Small Dataset Caution

## Do Not Overread the Picture

Small datasets are useful for learning.

But:

- One row can change the chart
- Group comparisons may be unstable
- Histogram shapes may be noisy
- Scatter patterns may be weak evidence

Trainer line:

```text
Use charts to learn the workflow. Use larger validated data for serious business decisions.
```

---

# Slide 32 - Matplotlib

## Chart Control

Matplotlib is a Python library for creating charts.

Useful for:

- Basic plots
- Titles
- Axis labels
- Figure size
- Colors
- Custom formatting

Example idea:

```text
plt.title()
plt.xlabel()
plt.ylabel()
plt.show()
```

Memory line:

```text
Matplotlib gives detailed chart control.
```

---

# Slide 33 - Seaborn

## Statistical Charts Made Easier

Seaborn is built on top of Matplotlib.

Useful for:

- Box plots
- Scatter plots
- Count plots
- Grouped visualizations
- Cleaner default styling

Example idea:

```text
sns.boxplot()
sns.scatterplot()
sns.countplot()
```

Trainer line:

```text
Seaborn helps create common statistical charts with less code.
```

---

# Slide 34 - Observation Writing

## Turn Visual Evidence Into Meaning

Weak observation:

```text
The chart is good.
```

Better observation:

```text
Gold membership customers have the highest average monthly spend.
```

Stronger observation:

```text
Gold membership customers have the highest average monthly spend, but the dataset is small, so this should be validated with more rows.
```

Memory line:

```text
A chart observation should include evidence and meaning.
```

---

# Slide 35 - Chart Observation Pattern

## Evidence + Meaning + Caution

Use this pattern:

```text
Chart evidence + plain meaning + caution or next check
```

Examples:

- The tallest bar is Gold, so Gold has the highest average monthly spend.
- The histogram shows spend values concentrated in the middle range.
- The scatter plot suggests visits and spend move together, but it does not prove cause.

Trainer line:

```text
Good chart reading is not just seeing. It is explaining responsibly.
```

---

# Slide 36 - Notebook 05 Mapping

## How This Section Connects to the Lab

In Notebook 05, learners will practice:

- Chart selection
- Bar charts
- Line charts
- Histograms
- Box plots
- Scatter plots
- Count plots
- Chart formatting
- Chart annotations
- Writing observations from charts

Trainer line:

```text
Notebook 05 turns visual thinking into Matplotlib and Seaborn practice.
```

---

# Slide 37 - Trainer Demo Flow

## Recommended Live Sequence

Suggested sequence:

1. Start with a question
2. Choose the columns
3. Choose the chart type
4. Create the chart
5. Add title and labels
6. Read the main pattern
7. Compare with a table if useful
8. Write one observation
9. Add caution if needed

Memory line:

```text
Question first. Chart second. Observation third.
```

---

# Slide 38 - Discussion Prompt

## Choose the Chart

Ask learners:

```text
Which chart would you use to compare average spend by membership?
```

Expected answer:

```text
Bar chart
```

Follow-up:

```text
Which chart would you use to see the distribution of monthly spend?
```

Expected answer:

```text
Histogram
```

---

# Slide 39 - Section Summary

## What We Learned

Key takeaways:

- Charts should answer questions
- Column type affects chart choice
- Bar charts compare categories
- Count plots count category rows
- Line charts need ordered x-axes
- Histograms show distributions
- Box plots show spread
- Scatter plots show relationships
- Titles, labels, color, and scale matter
- Chart observations need evidence and meaning

Memory line:

```text
Good visualization makes data easier to understand and explain.
```

---

# Slide 40 - Transition to Hands-On

## Now We Visualize the Data

Next, we move into Notebook 05.

We will:

- Load the cleaned customer dataset
- Choose charts based on questions
- Create common EDA charts
- Format charts clearly
- Write observations from visual evidence

Closing trainer line:

```text
The goal is not to make charts. The goal is to make patterns clear.
```

---

# Gamma Prompt

```text
Create a professional beginner-friendly training deck titled "Data Visualization: Seeing Patterns Clearly".
Use a clean modern technical design, light theme, left-aligned tables, simple chart mockups, and trainer-ready speaker notes.
Focus on practical chart thinking: question-first visualization, chart selection, bar charts, count plots, line charts, histograms, box plots, scatter plots, chart anatomy, labels, sorting, annotation, misleading charts, small dataset caution, Matplotlib, Seaborn, and plain-English chart observations.
Avoid emojis. Avoid cartoon style. Use professional icons, simple chart visuals, and clean tables.
```
