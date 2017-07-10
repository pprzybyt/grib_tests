from scipy.interpolate import griddata
import numpy as np

grid = np.zeros((2,2))
grid[0][0] = 1
grid[0][1] = 2
grid[1][0] = 3
grid[1][1] = 4

x, y = np.mgrid[0:1:10j, 0:1:10j]

points = np.matrix('0 0; 0 1; 1 0; 1 1')
values = np.matrix('1 ;2; 3; 4')

z0 = griddata(points, values, (x,y), method="nearest")
z1 = griddata(points, values, (x,y), method="linear")
z2 = griddata(points, values, (x,y), method="cubic")

from matplotlib import pyplot as plt



plt.subplot(221)
plt.imshow(z0[:][:])
plt.subplot(222)
plt.imshow(z1.reshape((10,10)))
plt.subplot(223)
plt.imshow(z2.reshape((10,10)))
plt.savefig("scipy.png")