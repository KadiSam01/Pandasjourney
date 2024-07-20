import matplotlib.pyplot as plt
birth_data = "unit3/Birthdata.csv"
with open(birth_data) as f:
    data = f.read().split('\n')
    birth_per_year= {}
    for year in range(2000,2015):
        birth_per_year[year] = 0
    birth_per_day = {}
    for week in range(1,8):
        birth_per_day[week] = 0
    for line in data[1:]:
        info = line.split(',')
        birth_per_year[int(info[0])]+=int(info[-1]) 
        birth_per_day[int(info[3])]+=int(info[-1])
fig, axes = plt.subplots(1,2)
axes[0].set_xlabel("Year")
axes[1].set_ylabel("birts per year")

axes[0].set_xlabel("Week per day")
axes[1].set_ylabel("births per year")


#amount_of_birth_per_year = birth_per_year.keys(),birth_per_year.values()
#amount_of_birth_per_day = birth_per_day.keys(),birth_per_day.values()
axes[0].bar(birth_per_year.keys(),birth_per_year.values())
axes[1].bar(birth_per_day.keys(),birth_per_day.values())
plt.show()
