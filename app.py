import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# --- CUSTOM CSS FOR FULL BG GRADIENT + GLASS EFFECT ---
st.markdown(
    """
    <style>
    html, body {
        height: 100% !important;
        width: 100% !important;
    }
    body {
        background: linear-gradient(135deg, #000428 0%, #004E92 100%) !important;
        background-attachment: fixed !important;
        background-repeat: no-repeat !important;
        min-height: 100vh !important;
        min-width: 100vw !important;
        overflow-x: hidden !important;
    }
    .stApp, .block-container, .main, .css-18e3th9, .css-1d391kg {
        background: transparent !important;
    }
    /* Glassmorphism effect for plot containers */
    .glass-box {
        background: rgba(255, 255, 255, 0.19);
        border-radius: 30px;
        box-shadow: 0 8px 32px 0 rgba(31, 38, 135, 0.23);
        backdrop-filter: blur(18px);
        -webkit-backdrop-filter: blur(18px);
        border: 1.5px solid rgba(255, 255, 255, 0.19);
        margin: 2rem auto 2rem auto;
        padding: 2rem 1.5rem 2rem 1.5rem;
        max-width: 900px;
    }
    /* Make scrollbar blend in */
    ::-webkit-scrollbar {
        width: 8px;
        background: transparent;
    }
    ::-webkit-scrollbar-thumb {
        background: #003a6d;
        border-radius: 4px;
    }
    /* Optional: make headers white for contrast */
    h1, h2, h3, h4, h5, h6, label, .stMarkdown, .stSlider, .st-bd {
        color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --- DATA LOAD ---
@st.cache_data
def load_data():
    annual_df = pd.read_csv('data/annual.csv')
    monthly_df = pd.read_csv('data/monthly.csv')
    monthly_df['Date'] = pd.to_datetime(monthly_df['Year'], errors='coerce')
    return annual_df, monthly_df

annual_df, monthly_df = load_data()

st.title("Global Temperature Anomalies Dashboard")

st.header("Annual Global Temperature Anomalies")
st.write("Data source: GISTEMP & GCAG combined annual anomalies")

# --- YEAR SLIDER FILTER ---
min_year = int(annual_df['Year'].min())
max_year = int(annual_df['Year'].max())
year_range = st.slider("Select Year Range", min_year, max_year, (min_year, max_year))

filtered_annual = annual_df[(annual_df['Year'] >= year_range[0]) & (annual_df['Year'] <= year_range[1])]

# --- ANNUAL PLOT (WITH GLASS EFFECT) ---
fig, ax = plt.subplots()
for source in filtered_annual['Source'].unique():
    source_data = filtered_annual[filtered_annual['Source'] == source]
    ax.plot(source_data['Year'], source_data['Mean'], label=source)
ax.set_xlabel('Year', color='white')
ax.set_ylabel('Temperature Anomaly (°C)', color='white')
ax.legend()
ax.grid(True, color='gray')
ax.tick_params(colors='white')

st.markdown('<div class="glass-box">', unsafe_allow_html=True)
st.pyplot(fig)
st.markdown('</div>', unsafe_allow_html=True)

# --- MONTHLY PLOT (WITH GLASS EFFECT) ---
st.header("Monthly Global Temperature Anomalies")
st.write("Data source: GISTEMP & GCAG combined monthly anomalies")

min_date = monthly_df['Date'].min().date()
max_date = monthly_df['Date'].max().date()

selected_dates = st.slider(
    "Select Date Range",
    min_date,
    max_date,
    (min_date, max_date)
)

filtered_monthly = monthly_df[
    (monthly_df['Date'] >= pd.to_datetime(selected_dates[0])) &
    (monthly_df['Date'] <= pd.to_datetime(selected_dates[1]))
]

fig2, ax2 = plt.subplots(figsize=(10, 4))
for source in filtered_monthly['Source'].unique():
    source_data = filtered_monthly[filtered_monthly['Source'] == source]
    ax2.plot(source_data['Date'], source_data['Mean'], label=source)
ax2.set_xlabel('Date', color='white')
ax2.set_ylabel('Temperature Anomaly (°C)', color='white')
ax2.legend()
ax2.grid(True, color='gray')
ax2.tick_params(colors='white')

st.markdown('<div class="glass-box">', unsafe_allow_html=True)
st.pyplot(fig2)
st.markdown('</div>', unsafe_allow_html=True)
