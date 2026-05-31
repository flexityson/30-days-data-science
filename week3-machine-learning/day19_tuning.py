import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split, GridSearchCV
from sklearn.metrics import accuracy_score

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

print(df.isnull().sum())

#clean data
df["Age"]=df["Age"].fillna(df["Age"].median())

df=df.drop(columns=["Cabin"])
df=df.dropna(subset=["Embarked"])
#select feature and target
X=df[['Age', 'Sex', 'Pclass', 'SibSp', 'Parch', 'Fare']].copy()
y=df['Survived']

X['Sex']=X['Sex'].map({'male': 0, 'female':1})

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.2, random_state=42)

param_grid={
    'n_estimators': [100, 200, 300],
    'max_depth': [10, 5, 10]}

grid_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=5)
grid_search.fit(X_train, y_train)

print("Best parameters:", grid_search.best_params_)
print("Best accuracy:", grid_search.best_score_)