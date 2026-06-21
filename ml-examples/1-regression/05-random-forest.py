import pandas as pd
from sklearn.ensemble import RandomForestRegressor

data = {
    "area": [900, 1000, 1500, 1800, 2000, 2200, 2500],
    "bedrooms": [2, 2, 3, 3, 4, 4, 4],
    "age": [10, 5, 3, 4, 2, 2, 1],
    "distance": [12, 8, 5, 6, 4, 3, 2],
    "price": [42, 55, 82, 95, 120, 130, 155]
}

df = pd.DataFrame(data)

X = df[["area", "bedrooms", "age", "distance"]]
y = df["price"]

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

new_house = pd.DataFrame({
    "area": [1700],
    "bedrooms": [3],
    "age": [4],
    "distance": [6]
})

prediction = model.predict(new_house)

print("Predicted price:", prediction[0], "lakhs")