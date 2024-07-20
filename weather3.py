import pandas as pd 


#weather_data = "unit3/us-weather-history/KCLT.csv"
weather_data = "unit3/us-weather-history/KPHL.csv"
df = pd.read_csv(weather_data)
"""
t = 0
for temp in df["actual_max_temp"]:
    if temp > 90:
        t+=1
print(t)
"""

#print(df["actual_max_temp"].sum())
print(df["actual_max_temp"].mean())
print(df["actual_min_temp"].mean())
print(df["actual_max_temp"].max())
print(df["actual_min_temp"].min())
print(len(df[df['record_max_temp']<df['actual_max_temp']]))
print(len(df[df['actual_min_temp']>df['record_min_temp']]))
print(len(df[df['actual_precipitation']>0]))
print(df['actual_precipitation'].sum())