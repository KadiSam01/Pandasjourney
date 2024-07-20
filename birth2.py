import pandas as pd

birth_data = "unit3/Birthdata.csv"

df = pd.read_csv(birth_data)

"""
print(df.groupby("date_of_month")["births"].sum().sort_values(ascending=False))
print(df.groupby(["year","month","date_of_month"])["births"].sum().max())
print(df.groupby(["year","month","date_of_month"])["births"].sum().min())
"""
print(df.groupby['month','date_of_month'])['births'].mean().sort_values().head(20))
print(df.groupby['month','date_of_month']))
