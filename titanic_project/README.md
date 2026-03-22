# Titanic Survival Prediction 🚢

## Problem Statement
Predict whether a passenger survived the Titanic disaster using Machine Learning.

## Dataset
Titanic dataset containing passenger details such as:
- Age
- Fare
- Sex
- Pclass
- SibSp
- Parch
- Embarked

## Steps Performed

### Data Preprocessing
- Dropped constant / useless columns
- Handled missing values (Mode imputation for Embarked)
- Feature Engineering:
  - Created FamilySize
  - Created IsAlone
- Outlier Handling:
  - Log transformation on Fare
- Feature Scaling using StandardScaler

### Model Used
- Logistic Regression

### Accuracy Achieved
~78%

## Tech Stack
- Python
- Pandas
- NumPy
- Scikit-Learn
- Seaborn
- Matplotlib

## How to Run

```bash
pip install -r requirements.txt
