import matplotlib.pyplot as plt

import pandas as pd

weather_data = "unit3/us-weather-history/KIND.csv"

df = pd.read_csv(weather_data)
plt.plot(df["average_max_temp"])
plt.plot(df["actual_max_temp"])
plt.plot(df["record_max_temp"])
plt.show()
