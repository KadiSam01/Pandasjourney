import pandas as pd 
honey_list = "unit3/honey.csv"


def convert_value(val):
    val = val.strip().replace(",", "")
    if val == "(D)":
        return 0
    return int(val)
df = pd.read_csv(honey_list)

df = df[["Year", "State","County","Value"]]

df["Value"] = df["Value"].apply(convert_value)

df = df[df["Value"]>0]
print(len(df))
print(df)

most_product_year = df["Year"].max()
print(df.groupby("Year")["Value","State"].max())


for hone in state 