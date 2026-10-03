\# 🎓 Student Performance Prediction System



A machine learning web application that predicts a student's final academic performance based on academic, personal, family, and lifestyle-related factors.



\## 📌 Project Overview



The Student Performance Prediction System uses machine learning to predict a student's final grade (G3) on a scale of 0–20.



The project includes:



\- Exploratory Data Analysis (EDA)

\- Data preprocessing

\- Feature encoding

\- Regression model training

\- Random Forest model

\- Model evaluation

\- Feature importance analysis

\- Interactive Streamlit web application

\- Performance classification

\- Personalized study recommendations



\## 🎯 Objective



The main objective of this project is to build a practical machine learning application that can estimate a student's final performance using their previous academic performance and other relevant student attributes.



\## 📊 Dataset



The project uses the \*\*UCI Student Performance Dataset\*\*.



The dataset contains information related to:



\- Student demographics

\- Family and education

\- Study habits

\- Previous academic performance

\- School support

\- Social activities

\- Lifestyle

\- Absences



The target variable is:



\*\*G3 — Final Grade\*\*



The grade ranges from \*\*0 to 20\*\*.



\## 🔍 Exploratory Data Analysis



Several relationships were analyzed during EDA, including:



\- Study time vs final grade

\- Previous failures vs final grade

\- Absences vs final grade

\- G1, G2 and G3 correlations

\- Distribution of final grades

\- Categorical variables and their relationship with performance



\## 🤖 Machine Learning



Two regression approaches were explored:



\### Linear Regression



A baseline Linear Regression model was developed to predict G3.



\### Random Forest Regressor



A Random Forest Regressor was then trained using the processed dataset.



The Random Forest model achieved:



\- \*\*MAE:\*\* 1.19

\- \*\*RMSE:\*\* 2.00

\- \*\*R²:\*\* 0.806



These results are based on the project's test split.



> Note: These metrics represent the performance of the model on the test data and should not be interpreted as prediction accuracy.



\## 📈 Feature Importance



The Random Forest model was also used to examine feature importance.



The most influential features in this model included:



\- G2 — Second period grade

\- Absences

\- Reason for choosing school

\- Age

\- G1 — First period grade



Feature importance indicates how useful features were to the trained model; it does not establish causation.



\## 🌐 Streamlit Application



The project includes an interactive Streamlit web application.



Users can enter student information such as:



\- Personal information

\- Family and education details

\- Academic information

\- Activities and internet access

\- Social and health information

\- Previous grades



The application provides:



1\. Predicted final score

2\. Performance level

3\. Personalized recommendations



\## 🛠️ Technologies Used



\- Python

\- Pandas

\- NumPy

\- Matplotlib

\- Seaborn

\- Scikit-learn

\- Joblib

\- Streamlit

\- Jupyter Notebook



\## 📁 Project Structure



```text

Student-Performance-Prediction/

│

├── app.py

├── student performance prediction dataset analysis.ipynb

├── student\_performance\_model.pkl

├── student\_preprocessor.pkl

└── README.md

🚀 How to Run

1\. Install the required libraries

pip install streamlit pandas numpy matplotlib seaborn scikit-learn joblib

2\. Open the project folder

cd Student-Performance-Prediction

3\. Run the Streamlit application

python -m streamlit run app.py



The application will open in your browser.



💡 Key Learning Outcomes



Through this project, I practiced:



Data cleaning and exploration

Feature selection

Categorical feature encoding

Train-test splitting

Regression modeling

Model evaluation using MAE, RMSE and R²

Random Forest

Feature importance analysis

Model serialization using Joblib

Building an interactive ML application with Streamlit

👩‍💻 Author



Charu Hasini Chennamallu



Aspiring Software Developer | Data Science Enthusiast





