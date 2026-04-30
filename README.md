# 🌾 Crop Recommendation System

> A machine learning web application that recommends the best crop to grow based on soil nutrients and weather conditions.

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Streamlit-red?style=flat-square)](https://ahsan-crop-recommendation.streamlit.app/)
[![Python](https://img.shields.io/badge/Python-3.7+-blue?style=flat-square&logo=python)](https://www.python.org/)
[![Scikit-learn](https://img.shields.io/badge/Scikit--learn-Random%20Forest-orange?style=flat-square)](https://scikit-learn.org/)

## 📋 Overview

This application uses a **Random Forest Classifier** trained on **2,200 samples** across **22 crop types** to predict the most suitable crop for given soil and weather conditions. It provides data-driven recommendations to optimize agricultural productivity.

## 🎯 Features

- **Smart Predictions:** ML-powered crop recommendations based on 7 environmental parameters
- **Interactive UI:** User-friendly Streamlit interface
- **22 Crop Types:** Comprehensive coverage of diverse crops
- **Real-time Demo:** Try it live at the Streamlit app link above

## 📊 Input Parameters

| Parameter | Description | Unit |
|-----------|-------------|------|
| **Nitrogen** | Nitrogen content in soil | mg/kg |
| **Phosphorus** | Phosphorus content in soil | mg/kg |
| **Potassium** | Potassium content in soil | mg/kg |
| **Temperature** | Ambient temperature | °C |
| **Humidity** | Relative humidity | % |
| **pH Value** | Soil pH level | 0–14 |
| **Rainfall** | Annual rainfall | mm |

## 🌱 Supported Crops

Rice, Maize, Chickpea, Kidney Beans, Pigeon Peas, Moth Beans, Mung Bean, Black Gram, Lentil, Pomegranate, Banana, Mango, Grapes, Watermelon, Muskmelon, Apple, Orange, Papaya, Coconut, Cotton, Jute, Coffee

## 🛠️ Tech Stack

- **Language:** Python
- **ML Framework:** Scikit-learn (Random Forest Classifier)
- **Web Framework:** Streamlit
- **Data Processing:** Pandas, NumPy

## 🚀 Quick Start

### Prerequisites
- Python 3.7+
- pip

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Ahsan-Neural/crop-recommendation-system.git
   cd crop-recommendation-system
   ```

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**
   ```bash
   streamlit run app.py
   ```

4. **Access the app:**
   Open your browser and navigate to `http://localhost:8501`

## 📈 Dataset

- **Total Samples:** 2,200
- **Crop Classes:** 22
- **Features:** 7
- **Source:** [Crop Recommendation Dataset](https://raw.githubusercontent.com/nileshely/Crop-Recommendation/main/Crop_Recommendation.csv)

## 👤 Author

**Ahsan Neural** — ML Enthusiast & Data Scientist  
[![Kaggle](https://img.shields.io/badge/Kaggle-Profile-blue?style=flat-square&logo=kaggle)](https://www.kaggle.com/ahsanneural)

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repository and submit a pull request with your improvements.

---

**Try the live demo:** [Crop Recommendation System](https://ahsan-crop-recommendation.streamlit.app/)