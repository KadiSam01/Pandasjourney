import matplotlib.pyplot as plt


fig, axes = plt.subplots(1,4)
axes[0][0].plot(range(10))
axes[0][1].plot([x**2 for x in range(10)])
axes[1].plot([x**3 for x in range(10)])
axes[1].plot([x**4 for x in range(10)])


plt.show()