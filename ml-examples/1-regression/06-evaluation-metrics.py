# ==========================================
# Regression Evaluation Metrics - Complete Code
# MAE, MSE, RMSE, R2 Score
# ==========================================

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# -------------------------------------------------
# 1. Create sample house price dataset
# -------------------------------------------------

data = {
    "area": [900, 1000, 1200, 1500, 1600, 1800, 2000, 2200, 2500, 2800],
    "bedrooms": [2, 2, 2, 3, 3, 3, 4, 4, 4, 5],
    "age": [10, 8, 6, 5, 4, 7, 3, 2, 5, 1],
    "distance": [12, 10, 9, 7, 6, 8, 5, 4, 6, 3],
    "price": [45, 52, 58, 72, 78, 85, 105, 120, 135, 160]
}

df = pd.DataFrame(data)

print("Dataset:")
print(df)


# -------------------------------------------------
# 2. Separate input features and target variable
# -------------------------------------------------

X = df[["area", "bedrooms", "age", "distance"]]
y = df["price"]

print("\nFeatures:")
print(X.head())

print("\nTarget:")
print(y.head())


# -------------------------------------------------
# 3. Train-test split
# -------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTotal rows:", len(df))
print("Training rows:", len(X_train))
print("Testing rows:", len(X_test))


# -------------------------------------------------
# 4. Create models
# -------------------------------------------------

linear_model = LinearRegression()

decision_tree_model = DecisionTreeRegressor(
    random_state=42
)

random_forest_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)


# -------------------------------------------------
# 5. Train models
# -------------------------------------------------

linear_model.fit(X_train, y_train)
decision_tree_model.fit(X_train, y_train)
random_forest_model.fit(X_train, y_train)


# -------------------------------------------------
# 6. Predict using test data
# -------------------------------------------------

linear_pred = linear_model.predict(X_test)
decision_tree_pred = decision_tree_model.predict(X_test)
random_forest_pred = random_forest_model.predict(X_test)


# -------------------------------------------------
# 7. Function to calculate regression metrics
# -------------------------------------------------

def evaluate_model(model_name, actual, predicted):
    mae = mean_absolute_error(actual, predicted)
    mse = mean_squared_error(actual, predicted)
    rmse = np.sqrt(mse)
    r2 = r2_score(actual, predicted)

    print("\n===================================")
    print(model_name)
    print("===================================")
    print("Actual values:   ", list(actual))
    print("Predicted values:", list(np.round(predicted, 2)))
    print("-----------------------------------")
    print("MAE :", round(mae, 2))
    print("MSE :", round(mse, 2))
    print("RMSE:", round(rmse, 2))
    print("R2  :", round(r2, 2))

    return {
        "Model": model_name,
        "MAE": round(mae, 2),
        "MSE": round(mse, 2),
        "RMSE": round(rmse, 2),
        "R2 Score": round(r2, 2)
    }


# -------------------------------------------------
# 8. Evaluate all models
# -------------------------------------------------

results = []

results.append(
    evaluate_model(
        "Linear Regression",
        y_test,
        linear_pred
    )
)

results.append(
    evaluate_model(
        "Decision Tree Regression",
        y_test,
        decision_tree_pred
    )
)

results.append(
    evaluate_model(
        "Random Forest Regression",
        y_test,
        random_forest_pred
    )
)


# -------------------------------------------------
# 9. Compare all models in one table
# -------------------------------------------------

results_df = pd.DataFrame(results)

print("\n\nModel Comparison:")
print(results_df)


# -------------------------------------------------
# 10. Predict price for a new house
# -------------------------------------------------

new_house = pd.DataFrame({
    "area": [1700],
    "bedrooms": [3],
    "age": [4],
    "distance": [6]
})

linear_new_prediction = linear_model.predict(new_house)
tree_new_prediction = decision_tree_model.predict(new_house)
forest_new_prediction = random_forest_model.predict(new_house)

print("\n\nNew House Details:")
print(new_house)

print("\nPredicted Price for New House:")
print("Linear Regression       :", round(linear_new_prediction[0], 2), "lakhs")
print("Decision Tree Regression:", round(tree_new_prediction[0], 2), "lakhs")
print("Random Forest Regression:", round(forest_new_prediction[0], 2), "lakhs")