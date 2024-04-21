import numpy as np
import matplotlib.pyplot as plt

x = list(range(1,101))
v = [i**2 for i in x]
plt.plot(x, v, color='green', marker='o', markersize=7)
plt.xlabel("Число")
plt.ylabel("Число в квадрате")
plt.title('Первый график')
plt.grid(True)
plt.show()
