import streamlit as st
import pandas as pd
import plotly.express as px
from src.data_loader import load_data
from src.analytics import (
    statewise_first_dose,
    statewise_second_dose,
    total_males_vaccinated,
    total_females_vaccinated
)

# App Title
st.set_page_config(page_title="COVID Vaccine Analytics India", layout="wide")
st.title("🇮🇳 COVID-19 Vaccine Analytics (India)")
st.markdown("Dataset Source: [Kaggle](https://www.kaggle.com/sudalairajkumar/covid19-in-india?select=covid_vaccine_statewise.csv)")

# Load dataset
df = load_data()

# Dataset Overview
st.header("📑 Dataset Overview")
st.write("Shape:", df.shape)
st.write("Columns:", df.columns.tolist())
st.dataframe(df.head())

# Statewise First Dose
st.header("💉 State-wise First Dose Vaccinations")
first_dose = statewise_first_dose(df)
fig1 = px.bar(first_dose, x="State", y="First Dose Administered", title="First Dose by State", color="First Dose Administered")
st.plotly_chart(fig1, use_container_width=True)

# Statewise Second Dose
st.header("💉 State-wise Second Dose Vaccinations")
second_dose = statewise_second_dose(df)
fig2 = px.bar(second_dose, x="State", y="Second Dose Administered", title="Second Dose by State", color="Second Dose Administered")
st.plotly_chart(fig2, use_container_width=True)

# Gender-wise Vaccination
st.header("👥 Gender-wise Vaccination")
males = total_males_vaccinated(df)
females = total_females_vaccinated(df)

gender_data = pd.DataFrame({
    "Gender": ["Male", "Female"],
    "Count": [males, females]
})

fig3 = px.pie(gender_data, names="Gender", values="Count", title="Male vs Female Vaccinations")
st.plotly_chart(fig3, use_container_width=True)
