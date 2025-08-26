import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Inject CSS for gradient background
st.markdown(
    """
    <style>
    /* Apply gradient background to full viewport */
    html, body, #root, .main, .block-container {
        background: linear-gradient(135deg, #000428, #004E92) !important;
        color: white;
        height: 100%;
        min-height: 100vh;
        margin: 0;
        padding: 0;
    }
    /* Override container backgrounds */
    .css-18e3th9, .css-145kmo2, .css-1d391kg {
        background: transparent !important;
    }
    /* Set heading and label text colors */
    h1, h2, h3, h4, h5, h6, label, .stMarkdown {
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


# Load the CSV data with caching
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

min_year = int(annual_df['Year'].min())
max_year = int(annual_df['Year'].max())
year_range = st.slider("Select Year Range", min_year, max_year, (min_year, max_year))

filtered_annual = annual_df[(annual_df['Year'] >= year_range[0]) & (annual_df['Year'] <= year_range[1])]

fig, ax = plt.subplots()
for source in filtered_annual['Source'].unique():
    source_data = filtered_annual[filtered_annual['Source'] == source]
    ax.plot(source_data['Year'], source_data['Mean'], label=source)
ax.set_xlabel('Year', color='white')
ax.set_ylabel('Temperature Anomaly (°C)', color='white')
ax.legend()
ax.grid(True, color='gray')
ax.tick_params(colors='white')
st.pyplot(fig)

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
st.pyplot(fig2)
