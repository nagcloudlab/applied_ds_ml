import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    "area": [1000, 1500, 2000, 900, 1800, 2200, 1300, 2500, 1600, 2800],
    "bedrooms": [2, 3, 4, 2, 3, 4, 2, 4, 3, 5],
    "age": [5, 3, 2, 10, 4, 2, 6, 1, 5, 1],
    "distance": [8, 5, 4, 12, 6, 3, 9, 2, 7, 2],
    "price": [55, 82, 120, 42, 95, 130, 65, 155, 78, 175]
}

df = pd.DataFrame(data)

X = df[["area", "bedrooms", "age", "distance"]]
y = df["price"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Actual prices:")
print(y_test.values)

print("Predicted prices:")
print(y_pred)
