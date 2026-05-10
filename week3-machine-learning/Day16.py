import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error

data = { 
    'size_sqft': [800, 1200, 1500, 900, 1800, 2000, 1100, 1600, 700, 2200],
    'bedrooms': [2, 3, 3, 2, 4, 4, 2, 3, 1, 5],
    'age_years': [10, 5, 8, 15, 3, 1, 12, 6, 20, 2],
    'price': [150000, 220000, 280000, 160000, 350000, 400000, 190000, 300000, 120000, 450000]
}

df = pd.DataFrame(data)

X=df[['size_sqft', 'bedrooms', 'age_years']]
y=df['price']

print(df.head())

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Actual:", y_test.values)

mae=mean_absolute_error(y_test, predictions)

print("Mean absolute error:", mae)