import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

# Load the CSV data with caching for performance
@st.cache_data
def load_data():
    annual_df = pd.read_csv('data/annual.csv')
    monthly_df = pd.read_csv('data/monthly.csv')
    # Convert monthly 'Year' column to datetime
    monthly_df['Date'] = pd.to_datetime(monthly_df['Year'], errors='coerce')
    return annual_df, monthly_df

annual_df, monthly_df = load_data()

st.title("Global Temperature Anomalies Dashboard")

st.header("Annual Global Temperature Anomalies")
st.write("Data source: GISTEMP & GCAG combined annual anomalies")

# Year filter slider
min_year = int(annual_df['Year'].min())
max_year = int(annual_df['Year'].max())
year_range = st.slider("Select Year Range", min_year, max_year, (min_year, max_year))

filtered_annual = annual_df[(annual_df['Year'] >= year_range[0]) & (annual_df['Year'] <= year_range[1])]

# Plotting annual temperature anomalies by source
fig, ax = plt.subplots()
for source in filtered_annual['Source'].unique():
    source_data = filtered_annual[filtered_annual['Source'] == source]
    ax.plot(source_data['Year'], source_data['Mean'], label=source)
ax.set_xlabel('Year')
ax.set_ylabel('Temperature Anomaly (°C)')
ax.legend()
ax.grid(True)
st.pyplot(fig)

st.header("Monthly Global Temperature Anomalies")
st.write("Data source: GISTEMP & GCAG combined monthly anomalies")

# Convert min and max dates to Python date for Streamlit slider compatibility
min_date = monthly_df['Date'].min().date()
max_date = monthly_df['Date'].max().date()

selected_dates = st.slider(
    "Select Date Range",
    min_date,
    max_date,
    (min_date, max_date)
)

# Filter the data using datetime converted back from date to Timestamp
filtered_monthly = monthly_df[
    (monthly_df['Date'] >= pd.to_datetime(selected_dates[0])) & 
    (monthly_df['Date'] <= pd.to_datetime(selected_dates[1]))
]

# Plot monthly temperature anomalies by source
fig2, ax2 = plt.subplots(figsize=(10, 4))
for source in filtered_monthly['Source'].unique():
    source_data = filtered_monthly[filtered_monthly['Source'] == source]
    ax2.plot(source_data['Date'], source_data['Mean'], label=source)
ax2.set_xlabel('Date')
ax2.set_ylabel('Temperature Anomaly (°C)')
ax2.legend()
ax2.grid(True)
st.pyplot(fig2)
