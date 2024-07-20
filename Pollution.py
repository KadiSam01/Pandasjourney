import pandas as pd
import matplotlib.pyplot as plt

pollution = "unit3/global-plastics-production.csv"
df = pd.read_csv(pollution)
df=df.drop('Code',axis=1)


print("amount of polution")
polution = df.groupby(["Year"])['Plastic_pollution'].sum().sort_values()
print(polution)

print("the average polution")
print(df["Plastic_pollution"].mean())

least_polution = df.groupby("Entity")['Plastic_pollution'].min().sort_values()
print("The amount of  less polution in the world",least_polution)
max_polution = df.groupby("Entity")['Plastic_pollution'].max().sort_values()
print("The amount of more polution in world",max_polution)
#least_polution = df['Plastic_pollution'].min()
#print(df[df['Plastic_pollution']==least_polution])

plt.plot(polution)
plt.title("Amount of polution over the year")
plt.xlabel("Years")
plt.ylabel("growth of polution")
plt.show()
