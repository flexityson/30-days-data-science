import streamlit as st 
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.title("Titanic Survival Predictor")
st.write("Enter passenger details to predict survival.")
# Load and prepare data
df = pd.read_csv("https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv")
df["Age"]=df["Age"].fillna(df["Age"].median())

df=df.drop(columns=["Cabin"])
df=df.dropna(subset=["Embarked"])

X = df[["Age", "Sex", "Pclass", "SibSp", "Parch", "Fare"]].copy()
y = df["Survived"]

X["Sex"] = X["Sex"].map({'male': 0, 'female':1})

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

age = st.slider("Age", 1, 80, 25)
sex = st.selectbox("Sex", ["male", "female"])
pclass = st.selectbox("Pclass", ["1", "2", "3"])
sibsp = st.slider("Sibsp", 0, 8, 0)
parch = st.slider("Parch", 0, 6, 0)
fare = st.slider("Fare", 0, 500, 50)

if st.button("Predict"):
    sex_encoded = 1 if sex == "female" else 0
    input_data = pd.DataFrame([[age, sex_encoded, int(pclass), sibsp, parch, fare]], columns=['Age', 'Sex', 'Pclass', 'SibSp', 'Parch', 'Fare'])
    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.success("This passenger would have survived")
    else:
        st.error("This passanger would have died")