

# Logistic Regression Example
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, roc_auc_score, roc_curve

# Load the dataset - students ( in-memory ) - study_hours,lab_score,internal_marks,final_result(pass/fail)
data = {
    'study_hours': [2, 3, 5, 1, 4, 6, 7, 8, 9, 10],
    'lab_score': [50, 60, 80, 40, 70, 90, 95, 85, 100, 110],
    'internal_marks': [30, 40, 60, 20, 50, 70, 80, 75, 90, 95],
    'final_result': [0, 0, 1, 0, 1, 1, 1, 1, 1, 1]  # 0 = fail, 1 = pass
}

# Feature matrix and target variable
X = pd.DataFrame(data, columns=['study_hours', 'lab_score', 'internal_marks'])
y = pd.Series(data['final_result'])

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)   

# Create and fit the logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train) 

# print the coefficients of the model
print("Coefficients:", model.coef_)
print("Intercept:", model.intercept_)

# Predict the probabilities of passing
y_prob = model.predict_proba(X_test)[:, 1]  # Probability of passing
print("Predicted probabilities of passing:", y_prob)


# Predict the results on the test set
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy * 100:.2f}%")

# Confusion matrix
conf_matrix = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:\n", conf_matrix)

# Classification report
class_report = classification_report(y_test, y_pred)
print("Classification Report:\n", class_report)

# ROC AUC score
roc_auc = roc_auc_score(y_test, y_prob)
print(f"ROC AUC Score: {roc_auc:.2f}")

# ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_prob)
print("ROC Curve:\nFPR:", fpr, "\nTPR:", tpr, "\nThresholds:", thresholds)
