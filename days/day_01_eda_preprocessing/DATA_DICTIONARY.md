# Day 1 Data Dictionary

## Dataset Files

Notebook 03 creates:

- `data/customer_activity_raw.csv`
- `data/customer_activity_clean.csv`

Notebook 06 creates:

- `data/customer_activity_preprocessed.csv`

## Dataset Domain

The dataset represents customer activity for a small retail business.

Each row represents one customer.

## Raw and Clean Dataset Columns

| Column | Type | Example | Meaning | Used for |
|---|---|---|---|---|
| `customer_id` | Numeric identifier | `101` | Unique customer number | Identifying rows |
| `name` | Text | `Asha` | Customer name for practice | Readability |
| `city` | Category | `Mumbai` | Customer city | Grouping, counting, encoding |
| `membership` | Category | `Gold` | Customer membership level | Grouping, spend comparison, encoding |
| `monthly_spend` | Numeric | `1200` | Amount spent in a month | Statistics and visualization |
| `visits_per_month` | Numeric | `4` | Number of customer visits in a month | Statistics and relationship checks |
| `signup_month` | Category | `Jan` | Month when customer signed up | Trend-style practice |

## Preprocessed Dataset Columns

The preprocessed dataset includes original readable columns plus transformed columns.

Examples:

| Column pattern | Meaning |
|---|---|
| `monthly_spend_standard_scaled` | Standard-scaled monthly spend |
| `visits_per_month_standard_scaled` | Standard-scaled visits |
| `monthly_spend_normalized` | Monthly spend transformed to 0-1 range |
| `visits_per_month_normalized` | Visits transformed to 0-1 range |
| `city_*` | One-hot encoded city columns |
| `membership_*` | One-hot encoded membership columns |
| `membership_level` | Ordered membership mapping |

## Notes

- The dataset is intentionally small for learning.
- It includes simple data quality issues in the raw version.
- The cleaned version should be used for statistics and charts.
- The preprocessed version is used to understand scaling and encoding.

