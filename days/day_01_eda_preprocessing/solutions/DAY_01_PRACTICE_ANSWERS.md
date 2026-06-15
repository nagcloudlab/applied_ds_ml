# Day 1 Practice Answers

These are sample answers. Students may write different correct answers.

---

## Answer Quality Rubric

Use this rubric to evaluate written answers throughout Day 1.

**Basic** -- The answer is correct but minimal. It may be one sentence or simply restate a definition.

**Good** -- The answer is correct and includes an example or connects the idea to the dataset.

**Strong** -- The answer is correct, includes an example, connects to the dataset, and mentions a limitation or next step.

---

## Notebook 01

### Sample answers

- Data science uses data to answer questions and support decisions.
- Notebooks are useful because they combine explanation, code, output, and observations.
- NumPy is used for numbers.
- Pandas is used for tables.
- Charts help us compare patterns visually.

### Practice Task answers

1. Add one more question: any clear, data-answerable question is acceptable (e.g., "Which signup month has the most customers?").
2. Add one row: the new row should have values for all columns (customer_id, city, membership, monthly_spend, visits_per_month). Check `customers.shape` shows one extra row.
3. Change bar chart: replace `y="monthly_spend"` with `y="visits_per_month"` and update `plt.ylabel("Visits per Month")`.
4. Sample observations: "I notice that customer 105 has the highest monthly spend because the data shows 2200 in the monthly_spend column."

### Exit Ticket answers

1. Data science is the process of using data to answer questions and support decisions.
2. Data science is the full workflow (cleaning, analysis, visualization, communication). Machine learning is one tool within data science that learns patterns from data.
3. NumPy provides efficient numerical arrays and math operations. Pandas provides DataFrames for working with table-like data.
4. Notebooks combine explanation, code, output, and observations in one place, making analysis reproducible and easy to share.

## Notebook 02

### List vs dictionary

- A list stores ordered values.
- A dictionary stores labeled values.

### Series vs DataFrame

- A Series is one column.
- A DataFrame is a full table.

### Filtering

Filtering keeps rows that match a condition.

### Grouping

Grouping splits data by category and calculates summaries.

### Common Wrong Answers

**Series vs DataFrame:** A Series is NOT just a smaller DataFrame. A Series is one column of data with an index. A DataFrame is a full table with rows and columns. Selecting one column with `df["col"]` returns a Series; selecting multiple columns with `df[["col1", "col2"]]` returns a DataFrame.

## Notebook 03

### Why inspect before cleaning?

Inspection helps us understand the problems before changing the data.

### What does `isna().sum()` show?

It shows how many missing values are in each column.

### Why create a copy before cleaning?

It preserves the raw data.

### Why use `Unknown`?

It keeps the row and clearly shows that the category was missing.

## Notebook 04

### Mean vs median

- Mean is the average.
- Median is the middle value.
- Median is more stable when unusual high or low values exist.

### Why square differences in variance?

Squaring prevents positive and negative differences from canceling each other.

### Why is standard deviation easier than variance?

Standard deviation is in the original unit, while variance is in squared units.

### Why is correlation not cause?

Two columns can move together without one directly causing the other.

### Common Wrong Answers

**Correlation is not causation:** A correlation of 0.8 does NOT mean one column causes the other to change. It means they move together, but the reason could be a third factor or coincidence. Always say "associated with" rather than "causes."

**Standard deviation units:** Standard deviation is in the same unit as the original column. If monthly_spend is in rupees, standard deviation is also in rupees. Variance is in squared units (squared rupees), which is why standard deviation is easier to explain.

## Notebook 05

### Chart choices

- Compare categories: bar chart
- Show distribution: histogram
- Compare two numeric columns: scatter plot
- Compare spread by group: box plot
- Show ordered trend: line chart

### Why titles and axis labels matter

They help readers understand what the chart shows without guessing.

## Notebook 06

### Standard scaling

Changes values so the column has mean near 0 and standard deviation near 1.

### Min-max normalization

Changes values to a 0 to 1 range.

### One-hot encoding

Creates separate 0/1 columns for each category.

### Ordered mapping

Use only when categories have a real order.

## Notebook 07

### What is EDA?

EDA means exploring data to understand quality, patterns, and useful questions.

### Sample Day 1 business observation

Gold membership customers appear to have higher average monthly spend in this practice dataset.

### Sample recommendation

The business should investigate what benefits Gold members use most, because they appear to spend more on average.

### Sample EDA report observation

Gold membership customers have the highest average monthly spend at approximately 1417 rupees, but only 3 customers are in this group, so this pattern needs validation with more data.

### Sample histogram observation

Monthly spend values appear concentrated between 850 and 1200 rupees based on the histogram, with the highest value at 1600 rupees.

### Sample scatter observation

The scatter plot suggests that customers with more visits tend to spend more, but with only 9 data points this pattern needs validation with a larger dataset.

