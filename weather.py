import matplotlib.pyplot as plt

with open("unit3/us-weather-history/KIND.csv") as f:
    data=f.read().strip().split('\n')
    actual_max_KCLT=[]
    average_max_KCLT=[]
    actual_min_KCLT=[]
    average_min_KCLT=[]
    actual_precip_KCLT=[]
    average_precip_KCLT=[]
    for line in data[1:]:
        info = line.split(',')
        actual_max_KCLT += [int(info[3])]
        average_max_KCLT += [int(info[5])]
        average_min_KCLT += [int(info[4])]
        actual_min_KCLT += [int(info[2])]
        actual_precip_KCLT += [float(info[10])]
        average_precip_KCLT += [float(info[11])]

with open("unit3/us-weather-history/KJAX.csv") as f:
    data=f.read().strip().split('\n')
    actual_max_KCQT=[]
    average_max_KCQT=[]
    actual_min_KCQT=[]
    average_min_KCQT=[]
    actual_precip_KCQT=[]
    average_precip_KCQT=[]
    for line in data[1:]:
        info = line.split(',')
        actual_max_KCQT += [int(info[3])]
        average_max_KCQT += [int(info[5])]
        average_min_KCQT += [int(info[4])]
        actual_min_KCQT += [int(info[2])]
        actual_precip_KCQT += [float(info[10])]
        average_precip_KCQT += [float(info[11])]


with open("unit3/us-weather-history/KPHL.csv") as f:
    data=f.read().strip().split('\n')
    actual_max_KHOU=[]
    average_max_KHOU=[]
    actual_min_KHOU=[]
    average_min_KHOU=[]
    actual_precip_KHOU=[]
    average_precip_KHOU=[]
    for line in data[1:]:
        info = line.split(',')
        actual_max_KHOU += [int(info[3])]
        average_max_KHOU += [int(info[5])]
        average_min_KHOU += [int(info[4])]
        actual_min_KHOU += [int(info[2])]
        actual_precip_KHOU += [float(info[10])]
        average_precip_KHOU += [float(info[11])]


fig, axes=plt.subplots(3,3)

axes[0,0].plot(actual_max_KCLT)
axes[0,0].plot(average_max_KCLT)
axes[0,1].plot(actual_min_KCLT)
axes[0,1].plot(average_min_KCLT)
axes[0,2].plot(actual_precip_KCLT)
axes[0,2].plot(average_precip_KCLT)

axes[1,0].plot(actual_max_KCQT)
axes[1,0].plot(average_max_KCQT)
axes[1,1].plot(actual_min_KCQT)
axes[1,1].plot(average_min_KCQT)
axes[1,2].plot(actual_precip_KCQT)
axes[1,2].plot(average_precip_KCQT)


axes[2,0].plot(actual_max_KHOU)
axes[2,0].plot(average_max_KHOU)
axes[2,1].plot(actual_min_KHOU)
axes[2,1].plot(average_min_KHOU)
axes[2,2].plot(actual_precip_KHOU)
axes[2,2].plot(average_precip_KHOU)

for row in axes:
    for axes in row[:2]:
        axes.set_ylim(0,110) 
plt.show()

