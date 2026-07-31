import pandas as pd 
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, precision_score, recall_score, f1_score


df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

print(df.isnull().sum())

#clean the data
df['Age'] = df['Age'].fillna(df['Age'].median())

df = df.drop(columns=["Cabin"])
df = df.dropna(subset=["Embarked"])

df["FamilySize"] = df["Parch"] + df["SibSp"] + 1
 #feature and target

features = ['Pclass', 'Age', 'SibSp', 'Parch', 'Fare', 'FamilySize']
X = df[features]
y = df['Survived']
#split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 42)

#Train and predict

model = RandomForestClassifier(n_estimators=100, random_state= 42)
model.fit(X_train, y_train)
y_pred = model.predict(X_test)

acc = accuracy_score(y_test, y_pred)
print(acc)

cm = confusion_matrix(y_test, y_pred )
print(cm)

print(precision_score(y_test, y_pred))
print(recall_score(y_test, y_pred))

