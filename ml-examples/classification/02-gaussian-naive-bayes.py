import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

from sklearn.metrics import accuracy_score, classification_report, confusion_matrix


data = {
    "study_hours": [1, 2, 3, 4, 5, 6, 7, 8, 1.5, 2.5, 3.5, 4.5],
    "attendance": [40, 50, 55, 65, 75, 85, 90, 95, 45, 52, 60, 70],
    "previous_marks": [25, 35, 45, 55, 65, 75, 85, 90, 30, 38, 48, 58],
    "result": ["Fail", "Fail", "Fail", "Pass", "Pass", "Pass",
               "Pass", "Pass", "Fail", "Fail", "Fail", "Pass"]
}

df = pd.DataFrame(data)

X = df[["study_hours", "attendance", "previous_marks"]]
y = df["result"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

model = GaussianNB()

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

print("Actual:", list(y_test))
print("Predicted:", list(y_pred))

print("Accuracy:", accuracy_score(y_test, y_pred))

print("Confusion Matrix:")
print(confusion_matrix(y_test, y_pred))

print("Classification Report:")
print(classification_report(y_test, y_pred))