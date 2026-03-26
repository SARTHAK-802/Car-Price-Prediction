# Car Price Prediction

## Overview

This project is an end-to-end Machine Learning application that predicts the selling price of a used car based on various features such as year, present price, kilometers driven, fuel type, seller type, transmission, and ownership.

The model is deployed as an interactive web application using **Streamlit**, allowing users to input car details and get real-time price predictions.

---

## Live Demo

🔗 [Click here to use the app](https://your-app.streamlit.app)

---

## 🛠️ Tech Stack

* **Programming Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-learn
* **Model:** Random Forest Regressor
* **Deployment:** Streamlit Cloud

---

## Features

* Predict car selling price instantly
* User-friendly web interface
* Handles categorical variables using encoding
* Real-time interaction with trained ML model

---

## Machine Learning Workflow

1. Data Collection
2. Data Cleaning & Preprocessing
3. Feature Engineering
4. Model Training (Random Forest Regressor)
5. Model Evaluation
6. Model Serialization (`model.pkl`)
7. Deployment using Streamlit

---

## Project Structure

```
Car-Price-Prediction/
│
├── app.py               # Streamlit web application
├── model.pkl            # Trained ML model
├── columns.pkl          # Feature columns
├── code.py              # Model training notebook
├── requirements.txt     # Dependencies
└── README.md            # Project documentation
```

---

## Installation & Setup

### 1️. Clone the repository

```
git clone https://github.com/your-username/Car-Price-Prediction.git
cd Car-Price-Prediction
```

### 2️. Install dependencies

```
pip install -r requirements.txt
```

### 3️. Run the application

```
streamlit run app.py
```

---

## Input Features

* Year of Purchase
* Present Price (in lakhs)
* Kilometers Driven
* Fuel Type (Petrol/Diesel)
* Seller Type (Dealer/Individual)
* Transmission (Manual/Automatic)
* Number of Owners

---

## Output

* Predicted selling price of the car (in lakhs ₹)

---

## Screenshots

(Add your app screenshot here)

---

## Future Improvements

* Add more advanced models (XGBoost, LightGBM)
* Improve UI/UX design
* Deploy using FastAPI + React for production

---

## Author

**Sarthak Maity**
🔗 GitHub: [SARTHAK-802.github.io](https://sarthak-802.github.io/)


---
