
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
data=[
    [100,10,1],
    [200,20,1],
    [300,30,1],
    [400,40,1],
    [500,50,0],
    [600,60,1],
    [700,70,0],
    [800,80,1],
    [900,90,0],
]
df=pd.DataFrame(data,columns=['stock_price','quantity','buyable'])

X=df[['stock_price','quantity']]
y=df['buyable']
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)

model=DecisionTreeClassifier()
model.fit(X_train,y_train)
accuracy=model.score(X_test,y_test)
print(f'Accuracy: {accuracy:.2f}')
