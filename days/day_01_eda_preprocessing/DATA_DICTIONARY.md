# Day 1 Data Dictionary

## Dataset Files

The table below lists which notebook creates each file and what to do if the file is missing.

| File | Created by | If file not found |
|---|---|---|
| `data/customer_activity_raw.csv` | Notebook 03 (NB03) | Run NB03 first |
| `data/customer_activity_clean.csv` | Notebook 03 (NB03) | Run NB03 first |
| `data/customer_activity_preprocessed.csv` | Notebook 06 (NB06) | Run NB06 first |

## Dataset Domain

The dataset represents customer activity for a small retail business.

Each row represents one customer.

## Primary Key

`customer_id` is the unique identifier. No two rows share the same `customer_id` value in the cleaned dataset.

## Raw and Clean Dataset Columns

| Column | dtype | Example | Meaning | Used for | Unique Values | Range / Values |
|---|---|---|---|---|---|---|
| `customer_id` | int64 | `101` | Unique customer number | Identifying rows | 9 | 101-109 |
| `name` | object | `Asha` | Customer name for practice | Readability | 9 | Asha, Ravi, Meera, John, Fatima, Chen, Sara, Vikram, Nina |
| `city` | object | `Mumbai` | Customer city | Grouping, counting, encoding | 4 | Mumbai, Delhi, Chennai, Unknown |
| `membership` | object | `Gold` | Customer membership level | Grouping, spend comparison, encoding | 4 | Gold, Silver, Bronze, Unknown |
| `monthly_spend` | float64 | `1200` | Amount spent in a month | Statistics and visualization | - | 700-1600 |
| `visits_per_month` | float64 | `4` | Number of customer visits in a month | Statistics and relationship checks | - | 1-6 |
| `signup_month` | object | `Jan` | Month when customer signed up | Trend-style practice | 6 | Jan, Feb, Mar, Apr, May, Jun |

### Sample Rows (Cleaned Dataset)

| customer_id | name | city | membership | monthly_spend | visits_per_month | signup_month |
|---|---|---|---|---|---|---|
| 101 | Asha | Mumbai | Gold | 1200.0 | 4.0 | Jan |
| 102 | Ravi | Delhi | Silver | 850.0 | 3.0 | Feb |
| 103 | Meera | Chennai | Gold | 1450.0 | 5.0 | Feb |

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
