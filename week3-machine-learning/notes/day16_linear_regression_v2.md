# Day 16 — Linear Regression
**Author:** Iung Seangchanmony (Tyson)
**Date:** 2026-04-07

---

## What I Learned Today

So yesterday I learned Logistic Regression which predicts yes or no stuff like pass or fail.
Today is Linear Regression which predicts actual numbers like house prices.

Same idea, different output. That's really the only difference at this level.

---

## Logistic vs Linear — Keep It Simple

```
Logistic Regression → yes or no     → pass/fail, spam/not spam
Linear Regression   → actual number → house price, salary, temperature
```

If someone asks you to predict a category — use Logistic.
If someone asks you to predict a number — use Linear.

---

## What I Built Today

A model that predicts house prices based on 3 things:
- How big the house is (size_sqft)
- How many bedrooms
- How old the house is (age_years)

The model looks at past houses and their prices, learns the pattern, then guesses the price of houses it's never seen before.

---

## The Code

```python
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

X = df[['size_sqft', 'bedrooms', 'age_years']]
y = df['price']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

predictions = model.predict(X_test)

print("Predictions:", predictions)
print("Actual:     ", y_test.values)

mae = mean_absolute_error(y_test, predictions)
print("Mean Absolute Error:", mae)
```

Output I got:
```
Predictions: [ 96027.38  239861.27]
Actual:      [120000 220000]
MAE: 21916.94
```

---

## The Mistake I Made Today

I wrote this at first:
```python
X = [['size_sqft', 'bedrooms', 'age_years']]  # WRONG
y = ['price']                                  # WRONG
```

That's just a list of column names as strings. No actual data inside.
The correct way is to select from the DataFrame:

```python
X = df[['size_sqft', 'bedrooms', 'age_years']]  # CORRECT
y = df['price']                                  # CORRECT
```

Always select from df. Don't create a new list for X and y.
I'll remember this one because it caused a confusing error.

---

## MAE — What It Actually Means

For yes/no predictions I use accuracy_score — how many did I get right.
For number predictions I use MAE — how far off was I on average.

My model predicted:
```
House 1 → predicted 96027  → actual 120000 → off by 23973
House 2 → predicted 239861 → actual 220000 → off by 19861

Average error = (23973 + 19861) / 2 = 21917
```

MAE of 21917 means on average I was wrong by $21,917 per house.
Lower MAE = better model. More data = lower MAE usually.

---

## The 7 Steps — Same Every Time

This is the ML workflow I need to memorize because it never changes:

```
1. Collect and clean data
2. Define X (features) and y (target)
3. Split into train and test
4. Choose the right model
5. Train → model.fit(X_train, y_train)
6. Predict → model.predict(X_test)
7. Measure → accuracy_score or MAE
```

Only step 4 and 7 change depending on whether I'm predicting a category or a number.
Everything else is identical.

---

## Quick Reference

| Task | Logistic Regression | Linear Regression |
|---|---|---|
| Predicts | Category (0/1) | Number |
| When to use | Yes/no problems | Number problems |
| Accuracy metric | accuracy_score | mean_absolute_error |
| Output example | [0, 1] | [96027, 239861] |

---

## Questions to Test Myself Later

1. When do I use Linear vs Logistic Regression?
2. What does MAE mean in plain English?
3. What is the bug I made today and why did it break?
4. Write the 7 ML steps from memory without looking
5. If MAE is 500 for salary prediction — is that good or bad?
6. What metric do I use for yes/no predictions vs number predictions?
