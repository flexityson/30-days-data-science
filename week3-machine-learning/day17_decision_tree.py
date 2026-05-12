import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
#collect data
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

print(df.isnull().sum())
#clean data
df['Age']=df['Age'].fillna(df['Age'].median())

df = df.drop(columns= ["Cabin"])
df = df.dropna(subset=["Embarked"])
#select fetures and target
X=df[['Age', 'Sex', 'Pclass', 'SibSp', 'Parch', 'Fare']].copy()
y=df['Survived']

X['Sex']=X['Sex'].map({'male': 0, 'female': 1})
#split into train and test
X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=42)
#Create and train DecisionTree
model = DecisionTreeClassifier()
model.fit(X_train, y_train)
#make predictions
prediction = model.predict(X_test)
#Evaluation
accuracy = accuracy_score(y_test, prediction)

print(accuracy)

from sklearn.linear_model import LogisticRegression

lr_model = LogisticRegression()
lr_model.fit(X_train, y_train)
lr_predictions = lr_model.predict(X_test)

from sklearn.metrics import accuracy_score
lr_accuracy = accuracy_score(y_test, lr_predictions)
print("Logistic Regression:", lr_accuracy)
print("Decision Tree:", accuracy)

from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, prediction)
print(cm)