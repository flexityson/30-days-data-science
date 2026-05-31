# What is a hyperparameter in your own words
so hyperparameter is something that chose before training the model, so it controls how the model learn, not the model peformance.
# What is GridSearchCV and what does it do
GridSearchCV specifically tries every combination in the grid and finds the best one automatically
# What is cross validation (cv=5) in your own words
it is something that split data into 5 chunks and test it one by one compare with train.
# Your results table — all 4 models and their accuracy
| Model | Accuracy |
|---|---|
| Logistic Regression | 79% |
| Decision Tree | 77% |
| Random Forest (default) | 78% |
| Random Forest (tuned) | 83.5% |
# Why limiting max_depth helped accuracy
think about max_depth just as the same idea of the concept overfitting the depth is max, it means your tree can grow as much as they can, and the same idea apply in training model it means the training has memoried the whole dataset, so it will fail when testing with different datasets.
# Self-review questions — at least 3
When do I have to use hyperparameter?
What is the best setting for my dataset to get more accuracy?
How to avoid the training being overfitting?