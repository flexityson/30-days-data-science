import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

print(df.isnull().sum())
#clean the data
df["Age"]=df["Age"].fillna(df["Age"].median())

df = df.drop(columns=["Cabin"])
df = df.dropna(subset=["Embarked"])

X=df[["Age", "Sex", "SibSp", "Parch", "Pclass", "Fare"]].copy()
y=df["Survived"]

X["Sex"]=X["Sex"].map({'male':0, 'female':1})

X_train, X_test, y_train, y_test=train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

prediction = model.predict(X_test)

accuracy = accuracy_score(y_test, prediction)

print(accuracy)
import pandas as pd
feature_importance = pd.Series(model.feature_importances_, index=X.columns)
print(feature_importance.sort_values(ascending=False))