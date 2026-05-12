Day17 note
1. What is a Decision Tree?

A decision tree is just like asking series question yes and no question until it reach the last data. and it will split into two groups

2. Overfitting 

Overfitting here: it mean like you take exam as an example, if we only reviewed same questions over and over again that appear in the last examination, what if you take another different examination you will get fail becuase you only know the same questions you once look at.

3. Confusion matrix 

it tells us about 4 things: (True, False) of positive and negative

Example: My titanic Dataset

True Negative which mean people died and it actually diedd
True Positive which mean people alive and it actually alive
False Negative which mean people died and it actually alive
False Positive which mean people alive and it actually died

4. Bugs I made today 

model.fit(X_train, y_test)

modelfit is actually using train not test

5. Why median over mean

we use median to find exact middle value while mean is just average which mean it cant give use exact value

6. Self-review questions

What is the 7 steps of machine learning?
Which method you use to clean the data?
What is overfitting and how does it affect Decision Trees?