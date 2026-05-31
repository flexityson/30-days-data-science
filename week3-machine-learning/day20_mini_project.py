import pandas as pd
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species']=iris.target

pd.set_option('display.max_columns', None)

print(df.isnull().sum())
print(df.head())
#select feature and target
X=df[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)']]
y=df['species']
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state=42)
#Logistic Regression
from sklearn.linear_model import LogisticRegression
model = LogisticRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(y_test, predictions)

print("Accuracy of LogisticRegression:", accuracy)

from sklearn.tree import DecisionTreeClassifier

dtc_model = DecisionTreeClassifier()
dtc_model.fit(X_train, y_train)

dtc_predictions = dtc_model.predict(X_test)

dtc_acc = accuracy_score(y_test, dtc_predictions)

print("Accuracy of DecisionTree:", dtc_acc)

from sklearn.ensemble import RandomForestClassifier
rfc_model = RandomForestClassifier()
rfc_model.fit(X_train, y_train)

rfc_predictions = rfc_model.predict(X_test)

rfc_acc = accuracy_score(y_test, rfc_predictions)

print("Accuracy of Random Forest:", rfc_acc)
from sklearn.model_selection import GridSearchCV
param_grid={
    'n_estimators': [100, 200, 300],
    'max_depth': [None, 5, 10]}
grid_search = GridSearchCV(RandomForestClassifier(), param_grid, cv=5)
grid_search.fit(X_train, y_train)

print("Best parameters:", grid_search.best_params_)
print("Best accuracy:", grid_search.best_score_)