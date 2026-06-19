# Example 5: Cross-Validation
# Shows why CV is more reliable than a single train-test split

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import cross_val_score, StratifiedKFold, train_test_split

# Student pass/fail dataset
np.random.seed(42)
n = 100
study_hours = np.random.uniform(1, 10, n)
attendance = np.random.uniform(50, 100, n)
previous_score = np.random.uniform(30, 100, n)
practice_tests = np.random.randint(0, 8, n)

score = 0.3 * study_hours + 0.2 * attendance + 0.3 * previous_score + 0.2 * practice_tests
result = (score > 30).astype(int)
flip = np.random.choice(n, size=10, replace=False)
result[flip] = 1 - result[flip]

X = pd.DataFrame({
    'study_hours': study_hours,
    'attendance': attendance,
    'previous_score': previous_score,
    'practice_tests': practice_tests,
})
y = pd.Series(result)

# --- Part 1: Single split can be misleading ---
print("=" * 50)
print("Part 1: Single Train-Test Split (varies by split)")
print("=" * 50)
for seed in [0, 7, 42, 99, 123]:
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=seed)
    model = DecisionTreeClassifier(max_depth=4, random_state=42)
    model.fit(X_train, y_train)
    print(f"  random_state={seed:<4}  Test Accuracy: {model.score(X_test, y_test):.2%}")

print("\nDifferent splits give different scores!")

# --- Part 2: 5-Fold Cross-Validation ---
print("\n" + "=" * 50)
print("Part 2: 5-Fold Cross-Validation")
print("=" * 50)
model = DecisionTreeClassifier(max_depth=4, random_state=42)
cv_scores = cross_val_score(model, X, y, cv=5, scoring='accuracy')

for i, s in enumerate(cv_scores, 1):
    print(f"  Fold {i}: {s:.2%}")
print(f"\n  Average CV Score: {cv_scores.mean():.2%}")
print(f"  Std Deviation:    {cv_scores.std():.2%}")

# --- Part 3: Stratified K-Fold ---
print("\n" + "=" * 50)
print("Part 3: Stratified K-Fold (preserves class ratio)")
print("=" * 50)
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
strat_scores = cross_val_score(model, X, y, cv=skf, scoring='accuracy')

for i, s in enumerate(strat_scores, 1):
    print(f"  Fold {i}: {s:.2%}")
print(f"\n  Average Stratified CV Score: {strat_scores.mean():.2%}")
print(f"  Std Deviation:               {strat_scores.std():.2%}")

print("\nKey Takeaway:")
print("- Single split can be lucky or unlucky")
print("- CV averages across folds for a stable estimate")
print("- Stratified K-Fold keeps class balance in each fold")
