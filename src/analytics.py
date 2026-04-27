def statewise_first_dose(df):
    return df.groupby("State")["FirstDose"].sum().reset_index()

def statewise_second_dose(df):
    return df.groupby("State")["SecondDose"].sum().reset_index()

def total_males_vaccinated(df):
    return df["Male"].sum()

def total_females_vaccinated(df):
    return df["Female"].sum()
