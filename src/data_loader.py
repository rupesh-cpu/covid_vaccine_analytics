import pandas as pd
import kagglehub
import os

def load_data():
    # Download dataset from Kaggle
    path = kagglehub.dataset_download("sudalairajkumar/covid19-in-india")
    
    # The dataset folder contains multiple files, we need covid_vaccine_statewise.csv
    file_path = os.path.join(path, "covid_vaccine_statewise.csv")
    
    if not os.path.exists(file_path):
        raise FileNotFoundError(
            f"Dataset not found at {file_path}. Please check Kaggle dataset structure."
        )
    
    return pd.read_csv(file_path)
