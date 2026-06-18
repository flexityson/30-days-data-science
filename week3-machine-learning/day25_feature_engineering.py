import pandas as pd

df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")

print(df.isnull().sum())

#clean the data
df['Age'] = df['Age'].fillna(df['Age'].median())

df = df.drop(columns=["Cabin"])
df = df.dropna(subset=["Embarked"])

df["FamilySize"] = df["Parch"] + df["SibSp"] + 1

print(df.groupby('FamilySize')['Survived'].mean())

df['Title'] = df['Name'].str.extract(r' ([A-Za-z]+)\.')

print(df['Title'].value_counts())