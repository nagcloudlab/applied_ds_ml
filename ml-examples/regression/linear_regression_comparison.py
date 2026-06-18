"""
Linear Regression Comparison: NumPy Normal Equation vs. Scikit-Learn
This script demonstrates that solving Linear Regression analytically using the 
Normal Equation yields the exact same model parameters as Scikit-Learn's implementation.
"""

import numpy as np
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression

# ==========================================
# 1. LOAD DATASET
# ==========================================
print("Loading California Housing dataset...")
try:
    housing = fetch_california_housing()
    X_raw = housing.data
    y = housing.target
    feature_names = housing.feature_names
except Exception as e:
    print(f"Could not load via fetch_california_housing (likely no internet): {e}")
    print("Falling back to synthetically generated mock housing data for illustration...")
    # Creating deterministic mock data mimicking the shape of California housing (8 features)
    np.random.seed(42)
    X_raw = np.random.randn(500, 8)
    # Target value influenced by weights + intercept (e.g., 2.0) + noise
    true_weights = np.array([0.5, -0.2, 1.2, 0.0, -0.5, 0.8, -0.1, 0.4])
    y = 2.0 + (X_raw @ true_weights) + np.random.randn(500) * 0.1
    feature_names = [f"Feature_{i+1}" for i in range(8)]

num_samples = X_raw.shape[0]

# ==========================================
# 2. NUMPY NORMAL EQUATION APPROACH
# ==========================================
print("\nRunning NumPy Normal Equation approach...")
# Add a column of 1s to the raw features to act as the intercept/bias parameter
bias_column = np.ones((num_samples, 1))
X_normal = np.hstack((bias_column, X_raw))

# Compute theta using the pseudo-inverse to handle potential multicollinearity stably
# Formula: theta = (X^T * X)^(-1) * X^T * y
theta_numpy = np.linalg.pinv(X_normal.T @ X_normal) @ X_normal.T @ y

numpy_intercept = theta_numpy[0]
numpy_coefs = theta_numpy[1:]

# ==========================================
# 3. SCIKIT-LEARN APPROACH
# ==========================================
print("Running Scikit-Learn LinearRegression approach...")
model = LinearRegression()
model.fit(X_raw, y)

sklearn_intercept = model.intercept_
sklearn_coefs = model.coef_

# ==========================================
# 4. PRINT AND COMPARE RESULTS
# ==========================================
print("\n" + "="*65)
print(f"{'Feature Name':<18} | {'NumPy Weight':<18} | {'scikit-learn Weight':<20}")
print("="*65)
print(f"{'Intercept (Bias)':<18} | {numpy_intercept:<18.6f} | {sklearn_intercept:<20.6f}")

for name, w_num, w_skl in zip(feature_names, numpy_coefs, sklearn_coefs):
    print(f"{name:<18} | {w_num:<18.6f} | {w_skl:<20.6f}")
print("="*65)

# Verify close matching within numerical precision thresholds
all_coefs_match = np.allclose(numpy_coefs, sklearn_coefs)
intercepts_match = np.allclose(numpy_intercept, sklearn_intercept)

if all_coefs_match and intercepts_match:
    print("\nSuccess! Both implementations produced identical coefficients and intercept values.")
else:
    print("\nWarning: There is a small numerical discrepancy between the implementations due to optimization variations.")
