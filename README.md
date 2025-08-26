# Global Temperature Anomalies Dashboard

This project provides an interactive dashboard to explore global temperature anomaly data from GISTEMP and GCAG datasets. The dashboard is built with Streamlit, featuring a full-screen color gradient background and a stylish glass (glassmorphism) effect around the charts.

## Features

- View combined annual and monthly global temperature anomalies.
- Interactive sliders for filtering data by year and date ranges.
- Beautiful dark gradient background with frosted glass effect on charts.
- Easy to run locally and deployable to cloud platforms.

## Data Sources

- [GISTEMP Global Land-Ocean Temperature Index](http://data.giss.nasa.gov/gistemp)
- [Global component of Climate at a Glance (GCAG)](http://www.ncdc.noaa.gov/cag/time-series/global)

## Dependencies

The project uses the following Python libraries:

- streamlit
- pandas
- matplotlib
- requests (used in data preprocessing script)

## Setup & Installation

1. Clone the repository or download the project files.

2. (Recommended) Create and activate a Python virtual environment:

python -m venv venv

Activate venv on Windows
.\venv\Scripts\activate

On macOS/Linux
source venv/bin/activate

text

3. Install required packages:

pip install streamlit pandas matplotlib requests

text

4. Run the preprocessing script to generate CSV data files:

python scripts/process.py

text

This script downloads, processes, and merges the GISTEMP and GCAG data into `data/annual.csv` and `data/monthly.csv`.

## Running the Dashboard

Once the data files are prepared, run the Streamlit app:

streamlit run app.py

text

Open your browser and go to [http://localhost:8501](http://localhost:8501) to interact with the dashboard.

## Deployment

You can deploy this app easily on:

- **Streamlit Cloud:** Connect your GitHub repo and deploy in minutes.
- **Heroku or other PaaS:** Use a `Procfile` and `requirements.txt`.

---

## Project Structure

global-temp/
│
├── data/
│ ├── annual.csv # Combined annual temperature data
│ └── monthly.csv # Combined monthly temperature data
│
├── scripts/
│ ├── process.py # Data preprocessing script
│ └── requirements.txt # Dependencies for preprocessing
│
├── app.py # Streamlit dashboard app script
├── requirements.txt # App dependencies
├── README.md # This file
└── ...

text

## License

This project is licensed under the Open Data Commons Public Domain Dedication and License (PDDL) 1.0.

---

## Acknowledgements

- Data provided by NASA GISS and Met Office Hadley Centre.
- Built with [Streamlit](https://streamlit.io/).

---

Feel free to open issues or contribute enhancements!
