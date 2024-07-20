import matplotlib.pyplot as plt
import pandas as pd

temp_data = "unit3/temperature_data.csv"
df = pd.read_csv(temp_data)

plt.plot(df["Year"], df["Anomaly"])
plt.plot(df["Year"], df["LOWESS"])
plt.show()