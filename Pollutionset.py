import pandas as pd
import matplotlib.pyplot as plt

pollution_set2 = "unit3/plastic-waste-generation-total.csv"
df = pd.read_csv(pollution_set2)
df=df.drop('Code',axis=1)


print("total amount of plastic in  the world")
print(df['Plastic waste generation (tonnes, total)'].sum())
highest_plastic_waste = df[["Plastic waste generation (tonnes, total)","Entity"]].sort_values(by="Plastic waste generation (tonnes, total)",ascending=False)

#it will find the 10 country with the highest amount of 
find_the_highest_ten = highest_plastic_waste[:10]
print(find_the_highest_ten)


least_plastic_waste = df[["Plastic waste generation (tonnes, total)","Entity"]].sort_values(by="Plastic waste generation (tonnes, total)",ascending=True)
find_the_lowest_ten = least_plastic_waste[:10]
print(find_the_lowest_ten)

find_the_highest_ten["Plastic waste generation (tonnes, total)"].plot(kind='bar')
plt.xlabel("Country")
plt.ylabel("Amount of plastic waste")
plt.title("Top 10 country with the most plastic waste")
plt.show()

find_the_lowest_ten["Plastic waste generation (tonnes, total)"].plot(kind='bar')
plt.xlabel("Country")
plt.ylabel("Amount of plastic waste")
plt.title("Top 10 country with the least plastic waste")
plt.show()
