import numpy as np
from sklearn.datasets import fetch_california_housing

# ==========================================
# 1. LOAD AND PREPARE THE DATASET
# ==========================================

# Fetch the California Housing dataset
housing = fetch_california_housing()

# X contains the features (e.g., MedInc, HouseAge, AveRooms)
# y contains the target variable (Median House Value)
X_raw = housing.data
y = housing.target

# Get the number of samples (m) and features (n)
num_samples = X_raw.shape[0]

# ==========================================
# 2. ADD THE BIAS TERM (Intercept)
# ==========================================

# The Normal Equation requires a column of 1s to represent the bias (x0 = 1).
# We create a column matrix of ones with the same number of rows as our data.
bias_column = np.ones((num_samples, 1))

# Concatenate the bias column to the front of our feature matrix X_raw
X = np.hstack((bias_column, X_raw))

# ==========================================
# 3. APPLY THE NORMAL EQUATION
# ==========================================

# Formula: theta = inverse(X.T @ X) @ X.T @ y
# '@' is the matrix multiplication operator in NumPy.
# '.T' computes the transpose of the matrix.

# Step A: Compute (X^T * X)
X_transpose = X.T
X_transpose_dot_X = X_transpose @ X

# Step B: Compute the pseudo-inverse of (X^T * X)
# We use pinv (pseudo-inverse) instead of inv because it is computationally 
# more stable if the matrix is non-invertible (multicollinearity).
X_blank_inverse = np.linalg.pinv(X_transpose_dot_X)

# Step C: Multiply by X^T and y to get the final weights (theta)
theta = X_blank_inverse @ X_transpose @ y

# ==========================================
# 4. DISPLAY THE RESULTS
# ==========================================

print("--- Linear Regression Results ---")
print(f"Intercept (Bias): {theta[0]:.4f}")

# Map each weight to its respective feature name
print("\nFeature Weights:")
for feature_name, weight in zip(housing.feature_names, theta[1:]):
    print(f"{feature_name:<12} : {weight:.4f}")

# ==========================================
# 5. MAKING PREDICTIONS (Example)
# ==========================================

# Let's predict the first 3 houses in our dataset to verify it works
predictions = X[:3] @ theta
actual_values = y[:3]

print("\n--- Sample Predictions ---")
for i in range(3):
    print(f"House {i+1} -> Predicted: ${predictions[i]*100k:.2f}k | Actual: ${actual_values[i]*100k:.2f}k")
