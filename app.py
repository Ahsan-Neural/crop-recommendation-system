import streamlit as st
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

st.set_page_config(
    page_title="Crop Recommendation System",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
    <style>
    [data-testid="stAppViewContainer"] {
        background-image: linear-gradient(rgba(10, 20, 10, 0.82), rgba(10, 20, 10, 0.82)),
        url("https://images.unsplash.com/photo-1500382017468-9049fed747ef?w=1600");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    [data-testid="stSidebar"] {
        background-color: rgba(15, 30, 15, 0.92);
        border-right: 1px solid #2d5a27;
    }
    .main-title { font-size: 2.2rem; font-weight: 800; color: #7ec850; letter-spacing: -0.5px; margin-bottom: 0; }
    .sub-title { font-size: 1rem; color: #a8c898; margin-top: 4px; margin-bottom: 28px; }
    .section-header { font-size: 1rem; font-weight: 600; color: #7ec850; margin-bottom: 12px;
        border-bottom: 1px solid #2d5a27; padding-bottom: 8px; }
    .result-card {
        background: linear-gradient(135deg, rgba(30, 70, 20, 0.9), rgba(15, 40, 10, 0.95));
        border: 1px solid #4a9e35;
        border-radius: 12px;
        padding: 32px;
        text-align: center;
        margin-top: 16px;
    }
    .result-label { font-size: 0.85rem; color: #a8c898; text-transform: uppercase; letter-spacing: 0.1em; }
    .result-crop { font-size: 2.8rem; font-weight: 800; color: #7ec850; margin: 8px 0; }
    .metric-card {
        background-color: rgba(20, 50, 15, 0.85);
        border: 1px solid #2d5a27;
        border-radius: 8px;
        padding: 14px 18px;
        margin-bottom: 8px;
    }
    .metric-label { font-size: 0.75rem; color: #a8c898; text-transform: uppercase; letter-spacing: 0.05em; }
    .metric-value { font-size: 1.4rem; font-weight: 700; color: #e6edf3; }
    .input-hint { font-size: 0.78rem; color: #6a9a5a; margin-top: -10px; margin-bottom: 8px; }
    .footer-link { color: #7ec850; text-decoration: none; font-size: 0.85rem; }
    div[data-baseweb="slider"] { padding-top: 4px; }
    label { color: #c8dcc0 !important; }
    </style>
""", unsafe_allow_html=True)

CROP_EMOJI = {
    "rice": "Rice", "maize": "Maize", "chickpea": "Chickpea",
    "kidneybeans": "Kidney Beans", "pigeonpeas": "Pigeon Peas",
    "mothbeans": "Moth Beans", "mungbean": "Mung Bean", "blackgram": "Black Gram",
    "lentil": "Lentil", "pomegranate": "Pomegranate", "banana": "Banana",
    "mango": "Mango", "grapes": "Grapes", "watermelon": "Watermelon",
    "muskmelon": "Muskmelon", "apple": "Apple", "orange": "Orange",
    "papaya": "Papaya", "coconut": "Coconut", "cotton": "Cotton",
    "jute": "Jute", "coffee": "Coffee"
}

@st.cache_resource
def train_model():
    url = "https://raw.githubusercontent.com/nileshely/Crop-Recommendation/main/Crop_Recommendation.csv"
    df = pd.read_csv(url)
    df.columns = df.columns.str.strip()
    X = df[["Nitrogen", "Phosphorus", "Potassium", "Temperature", "Humidity", "pH_Value", "Rainfall"]]
    y = df["Crop"]
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    clf = RandomForestClassifier(n_estimators=100, random_state=42)
    clf.fit(X_train, y_train)
    accuracy = clf.score(X_test, y_test)
    return clf, accuracy

with st.spinner("Loading model..."):
    model, accuracy = train_model()

with st.sidebar:
    st.markdown('<p class="section-header">Soil Parameters</p>', unsafe_allow_html=True)
    nitrogen   = st.slider("Nitrogen (N)", 0, 140, 50)
    phosphorus = st.slider("Phosphorus (P)", 5, 145, 50)
    potassium  = st.slider("Potassium (K)", 5, 205, 50)

    st.markdown('<p class="section-header" style="margin-top:20px;">Weather & Soil Conditions</p>', unsafe_allow_html=True)
    temperature = st.slider("Temperature (°C)", 8.0, 44.0, 25.0, step=0.1)
    humidity    = st.slider("Humidity (%)", 14.0, 100.0, 60.0, step=0.1)
    ph_value    = st.slider("pH Value", 3.5, 10.0, 6.5, step=0.1)
    rainfall    = st.slider("Rainfall (mm)", 20.0, 300.0, 100.0, step=0.5)

    st.markdown("---")
    st.markdown(
        '<p class="metric-label">Model Accuracy</p>'
        f'<p style="color:#7ec850;font-size:1.3rem;font-weight:700;">{accuracy*100:.1f}%</p>',
        unsafe_allow_html=True
    )
    st.markdown("---")
    st.markdown(
        '<p class="metric-label">Built by</p>'
        '<a class="footer-link" href="https://www.kaggle.com/ahsanneural" target="_blank">Ahsan Neural — Kaggle Profile</a>',
        unsafe_allow_html=True
    )

st.markdown('<p class="main-title">Crop Recommendation System</p>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Enter your soil and weather conditions to find the best crop for your land</p>', unsafe_allow_html=True)

col1, col2, col3, col4 = st.columns(4)
params = [
    ("Nitrogen", nitrogen, "mg/kg"),
    ("Phosphorus", phosphorus, "mg/kg"),
    ("Potassium", potassium, "mg/kg"),
    ("Temperature", temperature, "°C"),
]
for col, (label, val, unit) in zip([col1, col2, col3, col4], params):
    with col:
        st.markdown(f'<div class="metric-card"><p class="metric-label">{label}</p><p class="metric-value">{val} <span style="font-size:0.8rem;color:#6a9a5a;">{unit}</span></p></div>', unsafe_allow_html=True)

col5, col6, col7 = st.columns(3)
params2 = [
    ("Humidity", humidity, "%"),
    ("pH Value", ph_value, ""),
    ("Rainfall", rainfall, "mm"),
]
for col, (label, val, unit) in zip([col5, col6, col7], params2):
    with col:
        st.markdown(f'<div class="metric-card"><p class="metric-label">{label}</p><p class="metric-value">{val} <span style="font-size:0.8rem;color:#6a9a5a;">{unit}</span></p></div>', unsafe_allow_html=True)

st.markdown("---")

if st.button("Recommend Crop", use_container_width=True):
    input_data = np.array([[nitrogen, phosphorus, potassium, temperature, humidity, ph_value, rainfall]])
    prediction = model.predict(input_data)[0]
    proba = model.predict_proba(input_data).max() * 100
    display_name = CROP_EMOJI.get(prediction.lower(), prediction.capitalize())

    st.markdown(f"""
        <div class="result-card">
            <p class="result-label">Recommended Crop for Your Land</p>
            <p class="result-crop">{display_name}</p>
            <p style="color:#a8c898;font-size:0.95rem;">Model confidence: <strong style="color:#7ec850;">{proba:.1f}%</strong></p>
        </div>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <div style="border: 1px dashed #2d5a27; border-radius: 8px; padding: 48px; text-align:center; color:#6a9a5a;">
            Adjust the soil and weather parameters on the left, then click Recommend Crop.
        </div>
    """, unsafe_allow_html=True)
