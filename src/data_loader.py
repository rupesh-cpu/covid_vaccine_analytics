import pandas as pd
import os

def load_data(path="data/covid_vaccine_statewise.csv"):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Dataset not found at {path}.")
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()  # remove leading/trailing spaces

    # Rename to short, consistent names
    rename_map = {
        "First Dose Administered": "FirstDose",
        "Second Dose Administered": "SecondDose",
        "Male(Individuals Vaccinated)": "Male",
        "Female(Individuals Vaccinated)": "Female",
        "Total Individuals Vaccinated": "TotalVaccinated"
    }
    df.rename(columns=rename_map, inplace=True)
    return df
