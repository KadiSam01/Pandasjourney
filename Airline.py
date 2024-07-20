import pandas as pd
import matplotlib.pyplot as plt
airline_data = "unit3/airline-safety.csv"
df = pd.read_csv(airline_data)
#df[colum_name] --> selecting a colon
#df[conditional statement] --> filters rows by conditio
#print(df[df["avail_seat_km_per_weak"]==df["avail_seat_km_per_week"].max()])
#print(df[df[df["actual_max_temp"]>df["record_max_temp"]]])
#print(df[df["fatalities_85_99"]==0])
#print(df[df["fatalities_85_99"]==0])
max_miles = df["avail_seat_km_per_week"].max()
min_miles = df["avail_seat_km_per_week"].min()
#print(df[df["avail_seat_km_per_week"]==min_miles])
#print(df[df["avail_seat_km_per_week"]==max_miles])
#accident = df["fatal_accidents_00_14"].min()
#print(df[df["fatal_accidents_00_14"]==accident])
df["fatalities"] = df["fatalities_85_99"] + df["fatalities_00_14"]
print(df[["airline","fatalities"]])
print(df)
#f["fatalities_per_incident"] = df["fatalities"]/df["fatal_incidents"]
#print(df[["airline","fatalities_per_incident"]])
#print("airline","fatalities")


