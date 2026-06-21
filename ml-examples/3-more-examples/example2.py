import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    'student': ['A', 'B', 'C', 'D', 'E'],
    'study_hrs': [2, 3, 4, 5, 6],
    'attendance': [80, 85, 90, 95, 100],
    'prev_scores': [50, 60, 70, 80, 90],
    'sleep_hrs': [6, 7, 8, 5, 6],
    'final_score': [55, 65, 75, 85, 95]
}
df = pd.DataFrame(data)

# Features and target variable
X = df[['study_hrs', 'attendance', 'prev_scores', 'sleep_hrs']]
y = df['final_score']

# create linear regression model
model = LinearRegression()
model.fit(X, y)

# b0, b1, b2, b3, b4
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# y^ = b0 + b1*study_hrs + b2*attendance + b3*prev_scores + b4*sleep_hrs

# Coefficients: [ 7.93650794e-02  3.96825397e-01  7.93650794e-01 -1.38777878e-17]
# Intercept: -16.587301587301624

# y^ = -16.587301587301624 + 0.07936507936507936*study_hrs + 0.3968253968253968*attendance + 0.7936507936507936*prev_scores - 1.3877787807814457e-17*sleep_hrs

# Predicting final score for a new student
# study_hrs, attendance, prev_scores, sleep_hrs
new_student = [[4, 90, 70, 8]]  
predicted_score = model.predict(new_student)
print("Predicted final score for the new student:", predicted_score[0])