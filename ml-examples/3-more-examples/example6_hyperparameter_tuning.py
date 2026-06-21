# Example 6: Hyperparameter Tuning
# Grid Search and Random Search on Decision Tree

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV, train_test_split

# Student pass/fail dataset
np.random.seed(42)
n = 120
study_hours = np.random.uniform(1, 10, n)
attendance = np.random.uniform(50, 100, n)
previous_score = np.random.uniform(30, 100, n)
practice_tests = np.random.randint(0, 8, n)

score = 0.3 * study_hours + 0.2 * attendance + 0.3 * previous_score + 0.2 * practice_tests
result = (score > 30).astype(int)
flip = np.random.choice(n, size=12, replace=False)
result[flip] = 1 - result[flip]

X = pd.DataFrame({
    'study_hours': study_hours,
    'attendance': attendance,
    'previous_score': previous_score,
    'practice_tests': practice_tests,
})
y = pd.Series(result)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# --- Part 1: Baseline (default settings) ---
print("=" * 55)
print("Part 1: Baseline Decision Tree (no tuning)")
print("=" * 55)
baseline = DecisionTreeClassifier(random_state=42)
baseline.fit(X_train, y_train)
print(f"  Training Accuracy: {baseline.score(X_train, y_train):.2%}")
print(f"  Test Accuracy:     {baseline.score(X_test, y_test):.2%}")

# --- Part 2: Grid Search ---
print("\n" + "=" * 55)
print("Part 2: Grid Search")
print("=" * 55)

param_grid = {
    'max_depth': [2, 3, 4, 5],
    'min_samples_split': [2, 5, 10],
    'min_samples_leaf': [1, 2, 4],
    'criterion': ['gini', 'entropy']
}

total = 1
for v in param_grid.values():
    total *= len(v)
print(f"  Search space: {total} combinations x 5 folds = {total * 5} fits\n")

grid_search = GridSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_grid,
    cv=5,
    scoring='accuracy',
    n_jobs=-1
)
grid_search.fit(X_train, y_train)

print(f"  Best params:    {grid_search.best_params_}")
print(f"  Best CV Score:  {grid_search.best_score_:.2%}")
print(f"  Test Accuracy:  {grid_search.score(X_test, y_test):.2%}")

# --- Part 3: Random Search ---
print("\n" + "=" * 55)
print("Part 3: Random Search")
print("=" * 55)

param_dist = {
    'max_depth': list(range(2, 20)),
    'min_samples_split': list(range(2, 20)),
    'min_samples_leaf': list(range(1, 10)),
    'criterion': ['gini', 'entropy']
}

random_search = RandomizedSearchCV(
    DecisionTreeClassifier(random_state=42),
    param_dist,
    n_iter=30,
    cv=5,
    scoring='accuracy',
    random_state=42,
    n_jobs=-1
)
random_search.fit(X_train, y_train)

print(f"  Tried 30 random combinations from a large space")
print(f"  Best params:    {random_search.best_params_}")
print(f"  Best CV Score:  {random_search.best_score_:.2%}")
print(f"  Test Accuracy:  {random_search.score(X_test, y_test):.2%}")

# --- Comparison ---
print("\n" + "=" * 55)
print("Comparison")
print("=" * 55)
print(f"  {'Model':<20} {'CV Score':<12} {'Test Score'}")
print(f"  {'-'*48}")
print(f"  {'Baseline':<20} {'N/A':<12} {baseline.score(X_test, y_test):.2%}")
print(f"  {'Grid Search':<20} {grid_search.best_score_:<12.2%} {grid_search.score(X_test, y_test):.2%}")
print(f"  {'Random Search':<20} {random_search.best_score_:<12.2%} {random_search.score(X_test, y_test):.2%}")

print("\nKey Takeaway:")
print("- Grid Search: exhaustive, best for small search spaces")
print("- Random Search: faster, samples from large spaces")
print("- Always compare against a baseline model")
