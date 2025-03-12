# 🏠 House Price Prediction API

## 📌 Project Overview  
This project is a **Machine Learning API** built using **FastAPI**.  
It predicts house prices based on various features such as **price per bedroom, availability, number of reviews, number of beds, and baths**.  

The model is trained on **real estate data** to help users estimate housing prices efficiently.  
By providing relevant features, users can obtain **an accurate price prediction** for a house listing.

---

## 🔬 Machine Learning Approach  
This project follows a **structured ML pipeline**:  

1. **Data Preprocessing**  
   - Handled **missing values** and performed **feature engineering**  
   - Removed **outliers** using the **Interquartile Range (IQR) method**  
   - Scaled numerical features and **one-hot encoded categorical variables**  

2. **Model Selection**  
   - Trained and compared **three models**:  
     - 📉 **Linear Regression** → Basic but interpretable model  
     - 🌳 **Decision Tree** → Captures non-linearity but prone to overfitting  
     - 🌲 **Random Forest** → Ensemble model providing high accuracy  

3. **Hyperparameter Tuning**  
   - Optimized the **Random Forest model** using **GridSearchCV**  
   - Achieved a **94% R² score** after fine-tuning  

4. **Deployment with FastAPI**  
   - Built a **REST API** to serve predictions  
   - Hosted on **Render** for real-time predictions  

---

## 🚀 Features
- **ML Model:** Fine-Tuned **RandomForestRegressor**
- **API Framework:** **FastAPI**
- **Deployment:** Hosted on **Render**
- **Tested using:** Swagger UI (`/docs`) & CURL  

---

## 📡 Live API Endpoint
### 🌍 **Test the API in Browser (Swagger UI)**  
👉 [**House Price Prediction API Docs**](https://house-prediction-model-tabr.onrender.com/docs)

---

## 📌 How to Use the API

### **1️⃣ Test the API using Swagger UI**
1. Go to 👉 [API Docs](https://house-prediction-model-tabr.onrender.com/docs)
2. Click **"POST /predict"**
3. Click **"Try it out"**, enter sample data, and **Execute**
4. You will get a predicted house price in the response

---

📌 How to Use the API
1️⃣ Test the API using CURL (Command Prompt)
Run this command in CMD (Windows Terminal):

```bash
curl -X POST "https://house-prediction-model-tabr.onrender.com/predict" \
     -H "accept: application/json" \
     -H "Content-Type: application/json" \
     -d "{\"price\": 150.0, \"availability_365\": 200, \"number_of_reviews\": 50, \"calculated_host_listings_count\": 3, \"beds\": 2, \"baths\": 1.5}"
```
✅ Expected Response:
```
{
  "predicted_price": 20306.28
}
```
---
🔧 How to Run the API Locally

1️⃣ Clone the Repository
```bash
git clone <your-github-repo-link>
cd <your-repo-name>
```
2️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```
3️⃣ Run FastAPI
```bash
uvicorn app:app --reload
```
4️⃣ Open API Docs in Browser
```bash
http://127.0.0.1:8000/docs
```
---
## 📂 Project Structure
```plaintext
📁 House-Prediction-Model/
│── 📄 app.py                     # FastAPI script for serving predictions
│── 📄 tuned_random_forest_model.pkl  # Trained machine learning model
│── 📄 requirements.txt            # Dependencies for running the API
│── 📄 house_price_prediction.ipynb  # Jupyter Notebook with model training code
│── 📄 README.md                   # Project documentation
```
---
## 🎯 How the Model Works
- **Preprocessed the dataset** (handled missing values, feature engineering, encoding)
- **Trained multiple models** (Linear Regression, Decision Tree, Random Forest)
- **Selected the best model** (Fine-Tuned RandomForestRegressor)
- **Optimized using Hyperparameter Tuning** (GridSearchCV)
- **Deployed API using FastAPI & Render)

---
## 📝 Author
- 👤 **Raghav Tripathi**  
- 📧 **Email:** `tripathiraghav43@gmailcom`  
- 🔗 **GitHub:** [Your GitHub Profile](https://github.com/Raghav22222)




