# Day 1 Practice Answers

These are sample answers. Students may write different correct answers.

## Notebook 01

### Sample answers

- Data science uses data to answer questions and support decisions.
- Notebooks are useful because they combine explanation, code, output, and observations.
- NumPy is used for numbers.
- Pandas is used for tables.
- Charts help us compare patterns visually.

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

