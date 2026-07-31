# Day 26 — Model Evaluation

## 1. Confusion matrix
A matrix with rows and columns that tells you the actual thing that happened — did my model get it right or wrong? 4 cells: correct-died, false-survived, missed-survived, correct-survived.

## 2. Precision
Trust the YES. When the model says "survived", can I trust it?
My numbers: said survived 70 times, only 40 right → 57%.
It's only about the "yes" calls, not about the "died" calls.

## 3. Recall
Catch the YES that actually is. Out of all who actually survived (69), how many did the model catch (40) → 58%.

## 4. F1
Combines precision + recall (not accuracy). One score to balance "don't cry wolf" and "don't miss the real one."

## 5. Why accuracy alone is not enough
Accuracy 0.67 sounds fine, but the matrix shows 29 survivors were told they'd die. Accuracy hides that. Precision and recall reveal where it fails.

## 6. Why split train/test
711 train, 178 test. If you train on all, you already know the exam → fake 100%. What's the point of training if you know the outcome? Test = honest exam.

## 7. Trading translation
Win rate = accuracy. Good setups I take = precision. If win rate is 80% but I overtrade randomly, that's luck, not edge.

## 8. My numbers
0.67 = accuracy (how close to truth)
0.57 = precision (trust the yes)
0.58 = recall (catch the real survivors)

## Day 27 preview
Why only 0.67? Missing the best feature — Sex. Men vs women predicted survival more than anything. Feature engineering is next.