# Crop Recommendation System

A machine learning web application that recommends the best crop to grow 
based on soil nutrients and weather conditions.

**Live Demo:** https://ahsan-crop-recommendation.streamlit.app/

## Overview

This app uses a Random Forest classifier trained on 2200 samples across 
22 crop types to predict the most suitable crop for given soil and 
weather conditions.

## Input Parameters

| Parameter | Description | Unit |
|---|---|---|
| Nitrogen | Nitrogen content in soil | mg/kg |
| Phosphorus | Phosphorus content in soil | mg/kg |
| Potassium | Potassium content in soil | mg/kg |
| Temperature | Ambient temperature | °C |
| Humidity | Relative humidity | % |
| pH Value | Soil pH level | 0–14 |
| Rainfall | Annual rainfall | mm |

## Crops Predicted

Rice, Maize, Chickpea, Kidney Beans, Pigeon Peas, Moth Beans, 
Mung Bean, Black Gram, Lentil, Pomegranate, Banana, Mango, 
Grapes, Watermelon, Muskmelon, Apple, Orange, Papaya, 
Coconut, Cotton, Jute, Coffee

## Tech Stack

- Python
- Scikit-learn (Random Forest Classifier)
- Streamlit
- Pandas, NumPy

## How to Run Locally

1. Install dependencies:
   pip install -r requirements.txt

2. Run the app:
   streamlit run app.py


## Dataset

Public crop recommendation dataset — 2200 samples, 22 crop classes, 7 features.  
Source: [Crop Recommendation Dataset](https://raw.githubusercontent.com/nileshely/Crop-Recommendation/main/Crop_Recommendation.csv)
## Author

**Ahsan Neural** — [Kaggle Profile](https://www.kaggle.com/ahsanneural)
