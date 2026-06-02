# What I actually built today
today I have done one mini project by compare 3 models training I have learnd, not which one give the most accuracy but which one give the most accurate also come with realible and honest results
# Why 100% accuracy made us suspicious and it is actually okay this time 
beacuse 100% accuracy on big data could be the training is overfitting, and it was actually okay this time because this time we just learned and used the dataset that is easy to give us for most accuracy to test out, the real world data is messy and abtract.
# why GridSearchCV gave 95.8% instead of 100% 
because it used cross validation- 5 different splits averaged together. One lucky split gave 100%, but average across 5 splits the ture performance is 95.8%. That's why it's more trustworthy.
# Final Results of All 3 models and tuned
Accuracy of LogisticRegression: 100%
Accuracy of DecisionTree: 100%
Accuracy of Random Forest: 100%
Random Forest(tuned): 95.8%
# Self-review questions-at least 3
why from model to model give different accuracy?
why we have to consider the right one for different dataset?
Could we just randomly just any models to train the data base our own assumption that think it is the best?