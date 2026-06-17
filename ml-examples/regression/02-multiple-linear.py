import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "area": [1000, 1500, 2000, 900, 1800, 2200, 1300, 2500],
    "bedrooms": [2, 3, 4, 2, 3, 4, 2, 4],
    "age": [5, 3, 2, 10, 4, 2, 6, 1],
    "distance": [8, 5, 4, 12, 6, 3, 9, 2],
    "price": [55, 82, 120, 42, 95, 130, 65, 155]
}

df = pd.DataFrame(data)

X = df[["area", "bedrooms", "age", "distance"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)

new_house = pd.DataFrame({
    "area": [1700],
    "bedrooms": [3],
    "age": [4],
    "distance": [6]
})

predicted_price = model.predict(new_house)

print("Predicted price:", predicted_price[0], "lakhs")



print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)