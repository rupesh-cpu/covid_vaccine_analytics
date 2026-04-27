# 💉 COVID-19 Vaccine Analytics (India)

An interactive **Streamlit dashboard** that visualizes COVID-19 vaccination progress across Indian states using real-world data.  
👉 **Live Demo:** [rupesh-cpu-covid-vaccine-analytics-app](https://rupesh-cpu-covid-vaccine-analytics-app-ygkpau.streamlit.app/)

---

## 📊 Features

- **Dataset Overview**
  - Cleaned and normalized vaccination dataset
  - Quick inspection of raw data and column names

- **State-wise Analytics**
  - Bar charts for **First Dose Administered**
  - Bar charts for **Second Dose Administered**

- **Gender-wise Analytics**
  - Pie chart showing **Male vs Female vaccination distribution**

- **Interactive Visualizations**
  - Built with **Plotly** for modern, responsive charts
  - Streamlit UI for easy navigation and filtering

---

## 🗂 Dataset

Source: [COVID-19 in India (Kaggle)](https://www.kaggle.com/datasets/sudalairajkumar/covid19-in-india)

Key columns used:
- `State`
- `First Dose Administered`
- `Second Dose Administered`
- `Male(Individuals Vaccinated)`
- `Female(Individuals Vaccinated)`
- `Total Individuals Vaccinated`

Additional columns available for future extensions:
- Age groups (`18-44`, `45-60`, `60+`)
- Vaccine types (`Covaxin`, `Covishield`, `Sputnik V`)
- Transgender vaccination counts
- Adverse Events Following Immunization (AEFI)

---

## ⚙️ Tech Stack

- **Python** – Core programming language
- **Pandas** – Data wrangling and aggregation
- **Plotly** – Interactive charts
- **Streamlit** – Web app framework
- **Modular Project Structure**
  - `src/data_loader.py` → loads and cleans dataset
  - `src/analytics.py` → analytics functions
  - `app.py` → Streamlit dashboard

s
