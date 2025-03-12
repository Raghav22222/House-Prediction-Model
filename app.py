from fastapi import FastAPI
import joblib
import numpy as np
from pydantic import BaseModel

# Load the trained model
model = joblib.load('tuned_random_forest_model.pkl')

# Initialize FastAPI app
app = FastAPI()

# Define the input data structure (ONLY 6 FEATURES)
class HouseFeatures(BaseModel):
    price: float
    availability_365: int
    number_of_reviews: int
    calculated_host_listings_count: int
    beds: int
    baths: float

# Define the prediction endpoint
@app.post("/predict")
def predict_price(features: HouseFeatures):
    try:
        # Convert input data into NumPy array (matching model's 6 features)
        data = np.array([[features.price, features.availability_365, features.number_of_reviews,
                          features.calculated_host_listings_count, features.beds, features.baths]])

        # Get prediction from the model
        prediction = model.predict(data)

        # Return the predicted price
        return {"predicted_price": float(prediction[0])}
    except Exception as e:
        return {"error": str(e)}
