import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# 1. Create dataset
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


# 2. Separate features and target
X = df[["area", "bedrooms", "age", "distance"]]
y = df["price"]

print("\nFeatures:")
print(X)

print("\nTarget:")
print(y)


# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining rows:", len(X_train))
print("Testing rows:", len(X_test))


# 4. Create model
model = LinearRegression()


# 5. Train model
model.fit(X_train, y_train)


# 6. Predict test data
y_pred = model.predict(X_test)

print("\nActual prices:")
print(list(y_test))

print("\nPredicted prices:")
print(list(np.round(y_pred, 2)))


# 7. Evaluate model
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE :", round(mae, 2))
print("MSE :", round(mse, 2))
print("RMSE:", round(rmse, 2))
print("R2  :", round(r2, 2))


# 8. Check model coefficients
coefficients = pd.DataFrame({
    "Feature": X.columns,
    "Coefficient": model.coef_
})

print("\nModel Coefficients:")
print(coefficients)

print("\nIntercept:", round(model.intercept_, 2))


# 9. Predict new house price
new_house = pd.DataFrame({
    "area": [1700],
    "bedrooms": [3],
    "age": [4],
    "distance": [6]
})

predicted_price = model.predict(new_house)

print("\nNew House Details:")
print(new_house)

print("\nPredicted price for new house:", round(predicted_price[0], 2), "lakhs")