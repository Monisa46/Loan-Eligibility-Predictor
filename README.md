Loan Approval Prediction

This project uses machine learning to predict whether a loan application will be approved or not based on applicant information. The solution is built using Logistic Regression and Random Forest models, with performance evaluation and final prediction output.

Features

- Loads and preprocesses training and test datasets  
- Encodes categorical variables and handles missing values  
- Applies Logistic Regression and Random Forest classifiers  
- Evaluates models using Accuracy, Precision, Recall, F1-score, AUC  
- Visualizes ROC curves for both models  
- Generates loan approval predictions on test data

Dataset

Source: https://www.kaggle.com/datasets/altruistdelhite04/loan-prediction-problem-dataset  
Files used:
- train_u6lujuX_CVtuZ9i.csv  
- test_Y3wMUE5_7gLdaTN.csv

Preprocessing:
- Drop `Loan_ID`  
- Fill missing values with mode (for categorical) and median (for numeric)  
- Label encode categorical columns  
- Map Loan_Status: Y → 1, N → 0 (for training)

Built With

Python 3.10+  
Pandas, NumPy  
Scikit-learn  
Matplotlib, Seaborn

Model Performance Comparison

Logistic Regression

- Accuracy: 76%  
- Precision: 75% (class 0), 77% (class 1)  
- Recall: 49% (class 0), 91% (class 1)  
- AUC Score: 0.75

Random Forest

- Accuracy: 77%  
- Precision: 86% (class 0), 75% (class 1)  
- Recall: 42% (class 0), 96% (class 1)  
- AUC Score: 0.75

Conclusion

- Logistic Regression performs better in balanced prediction but struggles with false positives  
- Random Forest performs better in detecting approvals but has lower recall for denials  
- Final predictions are generated using Random Forest and saved to a CSV file

Demo link :
License

This project is licensed under the MIT License — free to use, adapt, and share with attribution.

About the Creator

Created by Monisa R, a B.Tech CSBS student exploring machine learning applications in real-world decision systems.

LinkedIn: https://www.linkedin.com/in/monisa-r-17a41228b/  
Email: monisa4606@gmail.com

