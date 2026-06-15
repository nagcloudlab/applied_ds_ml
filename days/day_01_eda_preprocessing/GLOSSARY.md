# Day 1 Glossary

## Core Terms

### Data Science

Using data to answer questions and support decisions.

### EDA

Exploratory Data Analysis. The process of inspecting, summarizing, and visualizing data to understand it.

Introduced in NB07.

### Dataset

A collection of data, usually arranged as rows and columns.

### Row

One record or observation.

### Column

One variable or attribute.

### DataFrame

A Pandas table with rows and columns.

Example: `pd.DataFrame({"city": ["Mumbai", "Delhi"], "spend": [1200, 850]})`

See also: Series. Introduced in NB02.

### Series

One Pandas column.

See also: DataFrame. Introduced in NB02.

### Missing Value

A value that is not available.

Example: `NaN` in a Pandas column means the value is not available.

See also: Duplicate Row. Introduced in NB03.

### Duplicate Row

A row repeated in the dataset.

See also: Missing Value. Introduced in NB03.

### Data Type

The kind of value in a column, such as number or text.

## Statistics Terms

### Mean

The average value.

See also: Median, Mode. Introduced in NB04.

### Median

The middle value after sorting.

See also: Mean, Mode. Introduced in NB04.

### Mode

The most common value.

See also: Mean, Median. Introduced in NB04.

### Variance

Squared spread from the average.

See also: Standard Deviation. Introduced in NB04.

### Standard Deviation

Typical spread from the average in the original unit.

Example: if the mean monthly spend is 1100 and the standard deviation is 283, most customers spend within roughly 283 rupees of the average.

See also: Variance. Introduced in NB04.

### Range

Maximum value minus minimum value.

### Percentile

A position-based summary value.

### Covariance

Shows whether two numeric columns move together.

See also: Correlation. Introduced in NB04.

### Correlation

Shows direction and strength of movement between two numeric columns.

Example: a correlation of 0.85 between visits and spend means they tend to move strongly in the same direction.

See also: Covariance. Introduced in NB04.

### Distribution

How values are spread across low, middle, and high values.

### Skewness

Whether a distribution is stretched more to one side.

## Visualization Terms

### Bar Chart

Compares values across categories.

Introduced in NB05.

### Line Chart

Shows change across an ordered sequence.

### Histogram

Shows the distribution of one numeric column.

Introduced in NB05.

### Box Plot

Shows spread and helps compare groups.

Introduced in NB05.

### Scatter Plot

Compares two numeric columns using points.

Introduced in NB05.

### Count Plot

Shows how many rows belong to each category.

## Preprocessing Terms

### Scaling

Changing numeric columns so their values are easier to compare.

See also: Standard Scaling, Normalization. Introduced in NB06.

### Standard Scaling

Transforms values so the column has mean near 0 and standard deviation near 1.

See also: Scaling, Normalization. Introduced in NB06.

### Normalization

Transforms values to a fixed range, commonly 0 to 1.

See also: Scaling, Standard Scaling. Introduced in NB06.

### Encoding

Converting text categories into numeric columns.

### One-Hot Encoding

Creates separate 0/1 columns for each category.

Example: a `city` column with values Mumbai, Delhi, Chennai becomes three columns: `city_Mumbai`, `city_Delhi`, `city_Chennai`, each containing 0 or 1.

See also: Ordered Mapping. Introduced in NB06.

### Ordered Mapping

Converts ordered categories into numbers.

See also: One-Hot Encoding. Introduced in NB06.

## Reporting Terms

### Observation

A plain-English statement based on data output.

Introduced in NB07.

### Evidence

The number, table, or chart that supports an observation.

Introduced in NB07.

### Recommendation

A suggested action based on evidence.

Introduced in NB07.

