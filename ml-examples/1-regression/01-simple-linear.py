import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "area": [1000, 1200, 1500, 1800, 2000],
    "price": [50, 60, 75, 90, 100]
}

df = pd.DataFrame(data)

X = df[["area"]]
y = df["price"]

model = LinearRegression()
model.fit(X, y)

new_house = pd.DataFrame({
    "area": [1600]
})

predicted_price = model.predict(new_house)

print("Predicted price:", predicted_price[0], "lakhs")

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)