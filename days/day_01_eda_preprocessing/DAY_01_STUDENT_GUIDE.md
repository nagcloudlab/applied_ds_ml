# Day 1 Student Guide - EDA and Preprocessing

## Day 1 Purpose

Day 1 teaches how to understand data before building advanced systems.

The goal is not to memorize code. The goal is to learn a repeatable workflow:

```text
QUESTION -> DATA -> CODE -> EVIDENCE -> DECISION
```

## What You Will Learn

By the end of Day 1, you should be able to:

- Explain what data science means.
- Use a Jupyter notebook.
- Create basic Python, NumPy, and Pandas objects.
- Inspect a dataset.
- Find and fix simple data quality problems.
- Calculate basic statistics.
- Create common charts.
- Scale and normalize numeric columns.
- Encode categorical columns.
- Write observations and a short EDA report.

## Notebook Order

Run the notebooks in this order.

1. `notebooks/01_data_science_ecosystem_and_setup.ipynb`
2. `notebooks/02_python_numpy_pandas_foundations.ipynb`
3. `notebooks/03_data_inspection_and_cleaning.ipynb`
4. `notebooks/04_basic_statistics_for_data_understanding.ipynb`
5. `notebooks/05_data_visualization_matplotlib_seaborn.ipynb`
6. `notebooks/06_scaling_normalization_encoding.ipynb`
7. `notebooks/07_day_01_mini_eda_project.ipynb`

## How to Use Each Notebook

For every concept:

1. Read the explanation.
2. Predict what the code will do.
3. Run the code.
4. Read the output carefully.
5. Write one observation in plain English.

## Day 1 Dataset

The main practice dataset is a small customer activity dataset.

It includes:

- Customer identity
- City
- Membership type
- Monthly spend
- Visits per month
- Signup month

The dataset is intentionally small so you can inspect it manually.

## Files Created During Day 1

Notebook 03 creates:

- `data/customer_activity_raw.csv`
- `data/customer_activity_clean.csv`

Notebook 06 creates:

- `data/customer_activity_preprocessed.csv`

## Expected Skills After Each Notebook

### Notebook 01

You should be able to:

- Explain data science in one sentence.
- Explain why notebooks are useful.
- Identify the purpose of NumPy, Pandas, Matplotlib, and Seaborn.

### Notebook 02

You should be able to:

- Create variables, lists, and dictionaries.
- Create NumPy arrays.
- Create Pandas Series and DataFrames.
- Select, filter, sort, add columns, and group data.

### Notebook 03

You should be able to:

- Inspect data shape, columns, and types.
- Count missing values.
- Detect duplicate rows.
- Clean text values.
- Fill missing numeric and categorical values.
- Save cleaned data.

### Notebook 04

You should be able to:

- Calculate mean, median, and mode.
- Explain variance and standard deviation.
- Explain covariance and correlation.
- Understand distribution and skewness.

### Notebook 05

You should be able to:

- Choose the right chart for a question.
- Create bar, line, histogram, box, scatter, and count plots.
- Write observations from charts.

### Notebook 06

You should be able to:

- Apply standard scaling.
- Apply min-max normalization.
- Apply one-hot encoding.
- Apply ordered mapping.
- Save a preprocessed dataset.

### Notebook 07

You should be able to:

- Combine inspection, statistics, visualization, and reporting.
- Write a short EDA report.
- Support observations with evidence.

## How to Write Good Observations

Weak observation:

```text
The chart is good.
```

Better observation:

```text
Gold membership customers have the highest average monthly spend in this dataset.
```

Strong observation:

```text
Gold membership customers have the highest average monthly spend, but the dataset is small, so this should be checked with more data before making a business decision.
```

## Day 1 Final Checklist

Before moving to Day 2, confirm that you can:

- Open and run notebooks.
- Explain rows and columns.
- Inspect and clean a small dataset.
- Calculate basic statistics.
- Create and interpret common charts.
- Scale and encode columns.
- Write a short EDA summary.

