# Applied Data Science and Machine Learning

Hands-on notebooks for learning Applied Data Science and Machine Learning step by step.

## Start Here

1. Complete the environment setup in `SETUP.md`.
2. Read the notebook style guide in `STYLE_GUIDE.md`.
3. Open the notebooks in day-wise order.
4. Run one notebook at a time.
5. Read the markdown explanation before running each code cell.

## Folder Structure

```text
applied_ds_ml/
  README.md
  SETUP.md
  STYLE_GUIDE.md
  requirements.txt
  requirements-optional-pycaret.txt
  days/
    day_01_eda_preprocessing/
      README.md
      notebooks/
        01_data_science_ecosystem_and_setup.ipynb
```

## Day-Wise Learning Path

### Day 1: Exploratory Data Analysis and Preprocessing

Focus:

- Data science and AI/ML ecosystem
- Python libraries for data science
- NumPy and Pandas foundations
- Data cleaning and preprocessing
- Basic statistics
- Correlation and covariance
- Distribution and skewness
- Visualization with Matplotlib and Seaborn
- Feature scaling and normalization
- Encoding categorical variables

Current notebook:

- `days/day_01_eda_preprocessing/notebooks/01_data_science_ecosystem_and_setup.ipynb`
- `days/day_01_eda_preprocessing/notebooks/02_python_numpy_pandas_foundations.ipynb`
- `days/day_01_eda_preprocessing/notebooks/03_data_inspection_and_cleaning.ipynb`
- `days/day_01_eda_preprocessing/notebooks/04_basic_statistics_for_data_understanding.ipynb`
- `days/day_01_eda_preprocessing/notebooks/05_data_visualization_matplotlib_seaborn.ipynb`
- `days/day_01_eda_preprocessing/notebooks/06_scaling_normalization_encoding.ipynb`
- `days/day_01_eda_preprocessing/notebooks/07_day_01_mini_eda_project.ipynb`

Day 1 support handouts:

- `days/day_01_eda_preprocessing/slides/SECTION_01_AI_WORLD_AND_DATA_SCIENCE.md`
- `days/day_01_eda_preprocessing/slides/SECTION_02_DATA_SCIENCE_LIFECYCLE_AND_PROJECT_FLOW.md`
- `days/day_01_eda_preprocessing/SETUP_DEMO_CHECKLIST.md`
- `days/day_01_eda_preprocessing/DAY_01_STUDENT_GUIDE.md`
- `days/day_01_eda_preprocessing/DAY_01_TRAINER_GUIDE.md`
- `days/day_01_eda_preprocessing/DATA_DICTIONARY.md`
- `days/day_01_eda_preprocessing/GLOSSARY.md`
- `days/day_01_eda_preprocessing/BEYOND_TOC_NOTES.md`
- `days/day_01_eda_preprocessing/solutions/DAY_01_PRACTICE_ANSWERS.md`

Future module planning:

- `course_roadmap/FUTURE_MODULES_FROM_CHAT.md`

### Later Days

Later days will be added one notebook at a time:

- Day 2: Predicting numbers from data
- Day 3: Predicting categories from data
- Day 4: Improving models and finding groups
- Day 5: Neural networks and Generative AI

## Dataset Approach

Different concepts need different dataset sizes.

- Small datasets help with first-time understanding and manual inspection.
- Medium datasets help with EDA, visualization, statistics, scaling, and encoding.
- Larger datasets are useful later when we build and compare learning systems.

Day 1 starts with small, easy-to-read examples before moving into richer EDA datasets.

## Notebook Style

Each notebook follows this pattern:

1. Concept explanation
2. One focused code block
3. Output interpretation
4. Short practice task
