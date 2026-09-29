# Heart_Disease_Prediction


A Machine Learning-based web application that predicts the possibility of heart disease using patient health information. The application provides a simple interface where users can enter medical parameters and get a prediction with probability.

## 🔗 Project Links

**🌐 Live Demo:** YOUR_DEPLOYMENT_LINK

**💼 LinkedIn:** YOUR_LINKEDIN_PROFILE_LINK

**📂 GitHub:** YOUR_GITHUB_REPOSITORY_LINK

---

## 📌 About the Project

Heart Disease Prediction is a Machine Learning project developed using **Python and Flask**. The model analyzes different health-related features and predicts whether the input data belongs to the positive or negative heart disease class.

The trained Machine Learning model is saved using **Pickle** and integrated into a Flask web application.

## 🎯 Objectives

* Build a Machine Learning model for heart disease prediction.
* Process and analyze patient health data.
* Create a simple web interface using HTML and CSS.
* Connect the ML model with a Flask backend.
* Display prediction results and probability to the user.

## 📊 Dataset

The project uses the **UCI Heart Disease Dataset**.

* **Records:** 303
* **Input Features:** 13
* **Target:** Heart disease classification

**Dataset Source:**
https://uci-ics-mlr-prod.aws.uci.edu/dataset/45/heart%2Bdisease

### Main Features

`age`, `sex`, `cp`, `trestbps`, `chol`, `fbs`, `restecg`, `thalach`, `exang`, `oldpeak`, `slope`, `ca`, `thal`

## 🤖 Machine Learning Model

**Algorithm:** Logistic Regression

### Preprocessing

* Train/Test Split – 80/20
* StandardScaler for feature scaling
* Stratified data splitting

### Model Performance

**Accuracy: 80.33%**

The trained model is stored as:

```text
heart_disease_model.pkl
```

## 🛠️ Technologies Used

| Technology   | Purpose              |
| ------------ | -------------------- |
| Python       | Programming          |
| Pandas       | Data processing      |
| NumPy        | Numerical operations |
| Scikit-learn | Machine Learning     |
| Flask        | Web application      |
| HTML         | Frontend             |
| CSS          | Styling              |
| Pickle       | Model saving/loading |

## 📂 Project Structure

```text
Heart_Disease_Prediction/
│
├── app.py
├── model.py
├── heart.csv
├── heart_disease_model.pkl
├── requirements.txt
├── README.md
│
└── templates/
    └── index.html
```

## 🔄 Project Workflow

```text
Heart Disease Dataset
        ↓
Data Preprocessing
        ↓
Train Machine Learning Model
        ↓
Save Model (.pkl)
        ↓
Flask Web Application
        ↓
User Enters Details
        ↓
Prediction + Probability
```

## ▶️ How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
cd Heart_Disease_Prediction
```

### 2. Install required packages

```bash
pip install -r requirements.txt
```

### 3. Train the model

```bash
python model.py
```

This creates:

```text
heart_disease_model.pkl
```

### 4. Run the Flask application

```bash
python app.py
```

Open the application in your browser:

```text
http://127.0.0.1:5000
```

## ✨ Key Features

* User-friendly web interface
* Machine Learning-based prediction
* Prediction probability
* Flask backend
* Saved and reusable ML model
* Easy to run locally

## 🚀 Future Improvements

* Try advanced ML algorithms such as Random Forest and XGBoost.
* Improve model accuracy using hyperparameter tuning.
* Add charts and data visualization.
* Deploy the application online.
* Add a database for storing prediction history.

## 👩‍💻 Author

**Vyshnavi Maddikera**

B.Tech Graduate | Java Full Stack & Data Analytics Enthusiast

**LinkedIn:** YOUR_LINKEDIN_PROFILE_LINK

## ⚠️ Disclaimer

This project is created for **educational purposes only**. The prediction should not be considered a medical diagnosis. Always consult a qualified healthcare professional for medical advice.

---

⭐ **If you find this project useful, please consider giving the repository a star!**
