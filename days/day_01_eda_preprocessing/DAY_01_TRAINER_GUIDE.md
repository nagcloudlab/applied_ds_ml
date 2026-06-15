# Day 1 Trainer Guide - EDA and Preprocessing

## Trainer Objective

By the end of Day 1, learners should be comfortable with the full data understanding workflow.

They do not need to be fast. They need to be clear.

Main teaching message:

```text
Do not rush to algorithms. Understand the data first.
```

## Recommended Delivery Timing

| Segment | Notebook | Suggested time |
|---|---|---|
| Opening slides: AI world and Data Science lifecycle | Slides | 60-90 min |
| Live setup demo | Checklist | 20-40 min |
| Ecosystem and notebook orientation | 01 | 25-35 min |
| Python, NumPy, Pandas | 02 | 45-60 min |
| Inspection and cleaning | 03 | 60-75 min |
| Basic statistics | 04 | 75-90 min |
| Visualization | 05 | 75-90 min |
| Scaling and encoding | 06 | 60-75 min |
| Mini EDA project | 07 | 60-90 min |

If time is limited, reduce practice time but do not skip:

- Data inspection
- Missing values
- Mean vs median
- Standard deviation
- Correlation caution
- Chart interpretation
- Encoding explanation

## Teaching Rhythm

For every concept, follow this pattern:

1. Ask a practical question.
2. Explain the concept.
3. Run one code cell.
4. Read the output.
5. Ask students to explain the output.
6. Write one plain-English observation.

## Opening Flow

Use this order before Notebook 01:

1. Present `slides/SECTION_01_AI_WORLD_AND_DATA_SCIENCE.md`.
2. Present `slides/SECTION_02_DATA_SCIENCE_LIFECYCLE_AND_PROJECT_FLOW.md`.
3. Run the live setup demo using `SETUP_DEMO_CHECKLIST.md`.
4. Open Notebook 01 and verify the kernel.

Trainer line:

```text
Slides create the map. The setup demo prepares the vehicle. The notebook starts the journey.
```

## Core Talk Tracks

### What is data science?

Say:

```text
Data science is the process of converting raw data into useful decisions.
```

### What is EDA?

Say:

```text
EDA means exploring data to understand quality, patterns, and questions before making decisions.
```

### Why clean data?

Say:

```text
Dirty data creates unreliable summaries. Cleaning improves trust in the analysis.
```

### Mean vs median

Say:

```text
Mean is the average. Median is the middle. If one value is unusually high or low, median is often more stable.
```

### Variance vs standard deviation

Say:

```text
Variance is the math version of spread. Standard deviation is the human-friendly version of spread.
```

### Covariance vs correlation

Say:

```text
Covariance tells direction. Correlation tells direction and strength in a standardized way.
```

### Scaling vs normalization

Say:

```text
Standard scaling asks how far a value is from average. Normalization asks where a value sits between minimum and maximum.
```

### Encoding

Say:

```text
Encoding converts categories into numbers so later data workflows can use them.
```

## Questions to Ask Students

Use these throughout Day 1:

- What question are we answering?
- What does each row represent?
- What does each column represent?
- What problem do you see in this dataset?
- What changed after cleaning?
- What does this number mean in plain English?
- What does this chart show?
- What should we check next?

## Common Student Doubts

### "Why do we need Pandas?"

Answer:

```text
Pandas helps us work with tables. Most real-world business data is table-like.
```

### "Why not just use Excel?"

Answer:

```text
Excel is useful, but Python makes repeated analysis, larger data, and reproducible workflows easier.
```

### "Why are there so many charts?"

Answer:

```text
Each chart answers a different kind of question.
```

### "Why do we save cleaned data separately?"

Answer:

```text
We preserve raw data so we can audit or redo cleaning later.
```

## Board Explanation Ideas

Draw these during class:

### Data Science Workflow

```text
Question -> Data -> Cleaning -> EDA -> Insight -> Decision
```

### Table Anatomy

```text
Rows    = records
Columns = variables
Cell    = one value
```

### Spread

```text
Average = center
Standard deviation = usual distance from center
```

### Correlation

```text
Up together     -> positive
Opposite motion -> negative
No clear motion -> near zero
```

## Beyond-TOC Concepts to Include

These are not always listed in beginner TOCs, but they improve training quality.

### Reproducibility

Learners should understand that notebooks should run again and produce similar results.

Say:

```text
Good analysis should be repeatable.
```

### Raw vs cleaned data

Never overwrite raw data too early.

Say:

```text
Raw data is the source of truth. Cleaned data is our working version.
```

### Evidence-based observations

Students should not write unsupported opinions.

Say:

```text
Every observation should point to a number, chart, or table.
```

### Small dataset caution

Say:

```text
This small dataset is for learning. Real business conclusions need more data and validation.
```

### Ethical handling of data

Say:

```text
Use only data you are allowed to use. Avoid exposing private information.
```

## Day 1 Trainer Checklist

Before class:

- Environment is working.
- Jupyter opens.
- Kernel is selected.
- Notebooks 01 to 07 run.
- Icons render.
- Charts display.

During class:

- Ask students to predict output.
- Ask students to explain output.
- Pause for checkpoints.
- Keep observations in plain English.

After class:

- Students should submit the mini EDA report from Notebook 07.
