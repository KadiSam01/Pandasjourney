import matplotlib.pyplot as plt
file_path = 'unit3/temperature_data.csv'
with open(file_path) as f:
    data = f.read().strip().split('\n')
    print(data)
    year = []
    anomaly = []
    lowess = [] 

for line in data[1:]:
    list_of_years, list_anomalies,list_lowesss=line.split(',')
    year+=[int(list_of_years)]
    anomaly+=[float(list_anomalies)]
    lowess+=[float(list_lowesss)]

plt.plot(year,anomaly)
plt.plot(year,lowess)
plt.show()