# Example 4: Overfitting vs Underfitting
# Shows how tree depth affects model generalization

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# Student pass/fail dataset
np.random.seed(42)
n = 100
study_hours = np.random.uniform(1, 10, n)
attendance = np.random.uniform(50, 100, n)
previous_score = np.random.uniform(30, 100, n)
practice_tests = np.random.randint(0, 8, n)

# Rule: pass if weighted combo is above threshold
score = 0.3 * study_hours + 0.2 * attendance + 0.3 * previous_score + 0.2 * practice_tests
result = (score > 30).astype(int)
# Add some noise
flip = np.random.choice(n, size=10, replace=False)
result[flip] = 1 - result[flip]

df = pd.DataFrame({
    'study_hours': study_hours,
    'attendance': attendance,
    'previous_score': previous_score,
    'practice_tests': practice_tests,
    'result': result
})

X = df[['study_hours', 'attendance', 'previous_score', 'practice_tests']]
y = df['result']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Compare different tree depths
print("=" * 55)
print("Overfitting vs Underfitting: Decision Tree Depth")
print("=" * 55)
print(f"{'max_depth':<12} {'Train Acc':<12} {'Test Acc':<12} {'Status'}")
print("-" * 55)

for depth in [1, 2, 4, 7, 15, None]:
    model = DecisionTreeClassifier(max_depth=depth, random_state=42)
    model.fit(X_train, y_train)
    train_acc = model.score(X_train, y_train)
    test_acc = model.score(X_test, y_test)

    if train_acc < 0.75 and test_acc < 0.75:
        status = "Underfitting"
    elif train_acc - test_acc > 0.15:
        status = "Overfitting"
    else:
        status = "Good Fit"

    label = str(depth) if depth else "None(full)"
    print(f"{label:<12} {train_acc:<12.2%} {test_acc:<12.2%} {status}")

print("\nKey Takeaway:")
print("- Too shallow (depth=1): underfits, misses patterns")
print("- Too deep (None):       overfits, memorizes noise")
print("- Balanced depth:        good fit, generalizes well")
