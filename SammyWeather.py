import matplotlib.pyplot as plt
weather_data = "unit3/us-weather-history/KCLT.csv"
with open(weather_data) as f:
    data = f.read().split('\n')
    actual_max_temp = []
    average_max_temp = []
    actual_min_temp = []
    average_min_temp = []
    actual_precip = []
    average_precip = []
    #record_max_temp = []
    for line in data[1:]:
        info = line.split(" , ")
        #actual_max_temp.append(int(info[3]))
        actual_max_temp +=[int(info[3])]
        actual_min_temp.append(int(info[2]))
        average_min_temp.append(int(info[4]))
        average_max_temp.append(int(info[5]))
        actual_precip.append(int(info[10]))
        average_precip.append(float(info[11]))
        #max_temps += [int(info[3])]
        #avg_max  += [int(info[5])]
        #precip += [float(info[11])]
        #ag_precip = [float(info[11])]

weather_data_KSEA = "unit3/us-weather-history/KSEA.csv"
with open(weather_data_KSEA) as f:
    actual_mean_temp_KSEA = []
    actual_max_temp_KSEA = []
    average_min_temp_KSEA = []
    average_max_temp_KSEA = []
    actual_precip_KSEA = []
    average_precip_KSEA = []
    actual_max_temp_KSE +=[int(info[3])]
    actual_min_temp_KSEA += [int(info[2])]
    average_min_temp_KSEA += [int(info[4])]
    average_max_temp_KSEA += [int(info[5])]
    actual_precip_KSEA += [int(info[10])]
    average_precip_KSEA += [int(info[11])]
fig, axes = plt.subplots(2,3)
axes[0][0].plot(actual_mean_temp)
axes[0][0].plot(aveage_min_temp)
axes[0][1].plot(actual_max_temp)
axes[0][2].plot(actual_precip)
axes[0][2].plot(average_precip)

axes[1][0].plot(actual_mean_temp_KSEA)
axes[1][0].plot(aveage_min_temp_KSEA)
axes[1][1].plot(actual_max_temp_KSEA)
axes[1][2].plot(actual_precip_KSEA)
axes[1][2].plot(average_precip_KSEA)

for row in axes:
    for data in axes:
        data.set_ylim(0,100)
#axes[0].plot()
#xes[0].plot(max_temps)
#axes[0].plot(avg_max)
#axes[1].plot(precip)
#plt.set_title("Test")
#plt.plot(max_temps)
plt.show()