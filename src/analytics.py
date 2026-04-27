def statewise_first_dose(df):
    return df.groupby("State")["First Dose Administered"].sum().reset_index()

def statewise_second_dose(df):
    return df.groupby("State")["Second Dose Administered"].sum().reset_index()

def total_males_vaccinated(df):
    return df["Male(Individuals Vaccinated)"].sum()

def total_females_vaccinated(df):
    return df["Female(Individuals Vaccinated)"].sum()
