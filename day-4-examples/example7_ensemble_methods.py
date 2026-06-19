# Example 7: Ensemble Methods
# Bagging (Random Forest) and Boosting (Gradient Boosting)

import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import (
    BaggingClassifier,
    RandomForestClassifier,
    GradientBoostingClassifier
)
from sklearn.model_selection import cross_val_score, train_test_split

# Student pass/fail dataset
np.random.seed(42)
n = 150
study_hours = np.random.uniform(1, 10, n)
attendance = np.random.uniform(50, 100, n)
previous_score = np.random.uniform(30, 100, n)
practice_tests = np.random.randint(0, 8, n)

score = 0.3 * study_hours + 0.2 * attendance + 0.3 * previous_score + 0.2 * practice_tests
result = (score > 30).astype(int)
flip = np.random.choice(n, size=15, replace=False)
result[flip] = 1 - result[flip]

X = pd.DataFrame({
    'study_hours': study_hours,
    'attendance': attendance,
    'previous_score': previous_score,
    'practice_tests': practice_tests,
})
y = pd.Series(result)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Define models
models = {
    "Decision Tree":      DecisionTreeClassifier(max_depth=4, random_state=42),
    "Bagging (10 trees)": BaggingClassifier(
                              estimator=DecisionTreeClassifier(max_depth=4),
                              n_estimators=10, random_state=42),
    "Random Forest":      RandomForestClassifier(n_estimators=100, max_depth=5, random_state=42),
    "Gradient Boosting":  GradientBoostingClassifier(n_estimators=100, max_depth=3,
                              learning_rate=0.1, random_state=42),
}

# --- Compare all models ---
print("=" * 65)
print("Ensemble Methods Comparison")
print("=" * 65)
print(f"  {'Model':<22} {'Train Acc':<12} {'CV Acc (5F)':<14} {'Test Acc'}")
print(f"  {'-'*60}")

for name, model in models.items():
    model.fit(X_train, y_train)
    train_acc = model.score(X_train, y_train)
    cv_scores = cross_val_score(model, X_train, y_train, cv=5, scoring='accuracy')
    test_acc = model.score(X_test, y_test)
    print(f"  {name:<22} {train_acc:<12.2%} {cv_scores.mean():<14.2%} {test_acc:.2%}")

# --- Show how bagging reduces variance ---
print("\n" + "=" * 65)
print("Variance Reduction: Single Tree vs Random Forest")
print("=" * 65)
print(f"  {'Model':<22} {'Scores across 5 folds':<35} {'Std Dev'}")
print(f"  {'-'*60}")

for name in ["Decision Tree", "Random Forest"]:
    model = models[name]
    cv = cross_val_score(model, X, y, cv=5, scoring='accuracy')
    scores_str = ", ".join(f"{s:.2f}" for s in cv)
    print(f"  {name:<22} [{scores_str}]  {cv.std():.4f}")

print("\n  Random Forest has lower std dev = more stable predictions")

# --- Feature importance from Random Forest ---
print("\n" + "=" * 65)
print("Feature Importance (Random Forest)")
print("=" * 65)
rf = models["Random Forest"]
for feat, imp in sorted(zip(X.columns, rf.feature_importances_), key=lambda x: -x[1]):
    bar = "#" * int(imp * 40)
    print(f"  {feat:<18} {imp:.3f}  {bar}")

print("\nKey Takeaway:")
print("- Bagging: trains models independently, reduces variance")
print("- Random Forest: bagging + random feature subsets")
print("- Boosting: trains sequentially, each model corrects errors")
print("- Ensembles are usually more stable and accurate than single trees")
