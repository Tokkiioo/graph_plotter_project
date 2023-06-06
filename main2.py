import matplotlib.pyplot as plt

x1 = [2, 4, 5, 6]
y1 = [2, 3, 6, 7]

plt.plot(x1, y1, color='green', linestyle='dashed', linewidth=3, marker='o', markerfacecolor='blue', markersize=12)

plt.xlim(1,8)
plt.ylim(1,8)

plt.xlabel('X Axis')

plt.ylabel('Y Axis')

plt.title('Demo Graph - Customization')

plt.legend()

plt.show()