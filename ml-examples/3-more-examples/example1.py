import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    'study-hours': [1, 2, 3, 4, 5],
    'Exam-Score': [36,44,48,52,55]
}
df = pd.DataFrame(data)

X = df[['study-hours']]
y = df['Exam-Score']

model = LinearRegression()
model.fit(X, y)

print("m:", model.coef_[0])
print("c:", model.intercept_)