# 30 Days of Data Science

![Python](https://img.shields.io/badge/Python-3.x-blue)
![SQL](https://img.shields.io/badge/SQL-Database-orange)
![Scikit--learn](https://img.shields.io/badge/Scikit--learn-ML-red)
![Status](https://img.shields.io/badge/Day-In%20Progress-brightgreen)
![Author](https://img.shields.io/badge/Author-Mony-purple)

**Author:** Iung Seangchanmony (Mony)  
**Program:** Year 1 Data Science & AI Engineering  
**Started:** May 2026  
**Goal:** Build real, employable data science skills in 30 days

---

## 🚀 Live Demo
[Titanic Survival Predictor](https://30-days-data-science.streamlit.app/)

## Why I'm Doing This

This is a structured 30-day self-learning challenge —
one concept per day, one commit per day, no excuses.

Every line of code written by me.
Every concept understood before moving forward.
No copy-paste. No shortcuts.

---

## Progress Tracker

| Week | Topic | Status |
|------|-------|--------|
| Week 1 | Python & Pandas |  Complete |
| Week 2 | SQL & Databases |  Complete |
| Week 3 | Machine Learning |  In Progress |
| Week 4 | Real Project + Deployment |  Coming Soon |

---

## Weekly Breakdown

### Week 1 — Python & Pandas
**Folder:** `week1-python-pandas`

**What I learned:**
- Data exploration and EDA from scratch
- Data cleaning — duplicates, missing values, wrong types
- Data visualization — bar, line, scatter charts
- Real project: Movie industry analysis

**Key insight from Week 1:**
> Does spending more money make a better film?
> No. The Godfather had a $6M budget and a 9.2 rating.

**Skills gained:**
```python
import pandas as pd
import matplotlib.pyplot as plt

# Load, clean, analyze, visualize
df = pd.read_csv('data.csv')
df.dropna(inplace=True)
df.groupby('category')['sales'].sum().plot(kind='bar')
```

---

### Week 2 — SQL & Databases
**Folder:** `week2-sql`

**What I learned:**
- SELECT, WHERE, ORDER BY, LIMIT
- Aggregate functions — COUNT, SUM, AVG, GROUP BY
- JOINs — INNER JOIN, LEFT JOIN
- Subqueries and CASE WHEN
- Real project: 5 business questions answered with SQL

**Sample query I wrote:**
```sql
SELECT category, 
       SUM(revenue) as total_revenue,
       AVG(rating) as avg_rating
FROM products
GROUP BY category
ORDER BY total_revenue DESC
LIMIT 5;
```

---

### Week 3 — Machine Learning Complete
**Folder:** `week3-machine-learning`
**What I learned:**
- Logistic Regression, Decision Tree, Random Forest
- Model comparison and evaluation
- Hyperparameter tuning with GridSearchCV
- Built a Titanic Survival Predictor web app with Streamlit

**To run the Streamlit app:**
```bash
streamlit run week3-machine-learning/day21_app.py
```

---

### Week 4 — Real Project + Deployment (Coming Soon)
**Folder:** 
**What I'm learning**
- Cambodia economic data analysis
- Build Streamlit dashboard
- Deploy live online
- End-to-end data science project

---

## Full Tech Stack

| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| Pandas | Data manipulation |
| Matplotlib | Visualization |
| SQL (SQLite) | Database queries |
| Scikit-learn | Machine learning |
| Jupyter Notebook | Development environment |
| Git + GitHub | Version control |
| Streamlit | Dashboard deployment (Week 4) |

---

## How to Run

```bash
# Clone this repository
git clone https://github.com/flexityson/30-days-data-science

# Install dependencies
pip install pandas matplotlib scikit-learn jupyter

# Launch Jupyter
jupyter notebook

# Navigate to any week folder
# Open .ipynb file and run all cells
```

---

## What's Next After 30 Days
Month 2 → Cambodia economic data project
Month 3 → Streamlit dashboard deployed live
Month 4 → First ML freelance project on Upwork
Month 6 → Full data science portfolio complete

---

## Contact

Available for data analysis and entry-level 
data science freelance projects.

- Email: [chanmony@gmail.com]
- GitHub: github.com/flexityson

---

## Support

If this challenge inspires you to start your own —
give it a star and start building.

*"Don't wait until you're ready.
Start now and get ready along the way."*
