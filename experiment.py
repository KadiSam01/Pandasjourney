import matplotlib.pyplot as plt
with open('unit3/311_data.csv') as f:
    data = f.read().split('\n')
    print(data)
    times = []
    temp_1 = []
    temp_2 = []
    for line in data[1:]:
        time, temp1, temp2 = line.split(",")
        times += [int(time)]
        temp_1 += [float(temp1)]
        temp_2 += [float(temp2)]

plt.plot(times, temp_1)
plt.plot(times, temp_2)

plt.show()