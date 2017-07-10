from eccodes import *
import numpy as np
from HyperPanel import HyperPanel
from Vect3D import Vect3D
from matplotlib import pyplot as plt
from settings import *
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
from matplotlib.ticker import LinearLocator, FormatStrFormatter



radius = 1
middle_point = (-15, 110)

def generate_square(midPoint, radius):
    points = list()

    x = midPoint[0]
    y = midPoint[1]
    points.append((x - radius, y - radius))
    points.append((x + radius, y - radius))
    points.append((x + radius, y + radius))
    points.append((x - radius, y + radius))

    return points

def gen_vect3d_square(points, values):
    square = list()
    i = 0
    for x, y in points:
        square.append(Vect3D(x, y, values[i]))
        i += 1

    return square

#f = open(SOURCE + "xt6_f0.grib2")
#gid = codes_grib_new_from_file(f)

idx_file = "my.idx"
index_keys = ["shortName", "level"]
iid = codes_index_new_from_file(SOURCE + 'ocnf2017070418.01.2017070412.grib2', index_keys)
codes_index_write(iid,SOURCE + idx_file)

index_vals = []

for key in index_keys:
    print key, codes_index_get_size(iid, key)

for key in index_keys:
    key_vals = codes_index_get(iid,key)
    index_vals.append(key_vals)
print index_vals[1]


codes_index_select(iid, "shortName", "t")
codes_index_select(iid, "level", "0")
gid = codes_new_from_index(iid)

x = middle_point[0]
y = middle_point[1]

mid_value = codes_grib_find_nearest(gid,x, y)[0].value

points =  generate_square(middle_point, radius)
values = []
for lat, lon in points:
    values.append(codes_grib_find_nearest(gid, lat, lon)[0].value)
    print lat, lon, values[-1] - 273.15

v = gen_vect3d_square(points, values)

# TEST
w = 10
h = 10

w = 2 * w + 1
h = 2 * h + 1

test = np.zeros((w,h))

x = np.zeros((w,h))
y = np.zeros((w,h))
z = np.zeros((w,h))

hp = HyperPanel(v[0], v[1], v[2], v[3])
for i in range(w):
    for j in range(h):
        x[i][j] = hp.get_panel_point_uv(-1 + j/((w - 1) /2.), -1 + i/((h-1)/2.)).x
        y[i][j] = hp.get_panel_point_uv(-1 + j/((w - 1) /2.), -1 + i/((h-1)/2.)).y
        z[i][j] = hp.get_panel_point_uv(-1 + j/((w - 1) /2.), -1 + i/((h-1)/2.)).z

plt.imshow(z)#, interpolation='spline36')
plt.title("interpolation test")
plt.colorbar()
plt.show()
plt.savefig(IMAGES + "interpolation_in_cords.png")

fig = plt.figure()
ax = fig.add_subplot(111, projection=  "3d")
ax.plot_wireframe(x, y, z, rstride = 100, cstride= 100)
plt.savefig(IMAGES + "plot3d_test.png")

fig = plt.figure()
ax = fig.gca(projection = '3d')
x = x[1]
y  = np.arange(-.5,0.501,0.05)
x, y = np.meshgrid(x, y)

surf = ax.plot_surface(x,y,z, cmap= cm.coolwarm)
plt.savefig(IMAGES + "plot3d_test2.png")

print hp.get_panel_point_uv(0,0).z - 273.15

codes_release(gid)
#f.close()