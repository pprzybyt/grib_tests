from eccodes.high_level.gribfile import *
from eccodes import  *
from ForecastError import ForecastError
from Bitmap import Bitmap
from TimeInterpolator import TimeInterpolator
import numpy as np
from matplotlib import pyplot as plt
from random import randint
from settings import *

f1 = open(SOURCE + "tmpsfc_1.grib2")
f2 = open(SOURCE + "tmpsfc_2.grib2")
f3 = open(SOURCE + "tmpsfc_3.grib2")
f4 = open(SOURCE + "tmpsfc_4.grib2")


gid1 = codes_grib_new_from_file(f1)
gid2 = codes_grib_new_from_file(f2)
gid3 = codes_grib_new_from_file(f3)
gid4 = codes_grib_new_from_file(f4)

b1 = Bitmap(gid1, "temp_inter_test1")
b2 = Bitmap(gid2, "temp_inter_test2")
b3 = Bitmap(gid3, "temp_inter_test3")
b4 = Bitmap(gid4, "temp_inter_test4")

fig, ((ax1), (ax2)) = plt.subplots(2,2, sharex = True, sharey=True)
ax1[0].set_title("m1")
ax1[1].set_title("m2")
ax2[0].set_title("m3")
ax2[1].set_title("m4")

im = ax1[0].imshow(b1.bitmap - 273.15)
im = ax1[1].imshow(b2.bitmap - 273.15)
im = ax2[0].imshow(b3.bitmap - 273.15)
im = ax2[1].imshow(b4.bitmap - 273.15)

fig.subplots_adjust(right = .8)
cb_ax = fig.add_axes([.85, .15, .05, .7])
fig.colorbar(im, cax = cb_ax)
plt.savefig(IMAGES + "comparison.png")

x = []
y = []

for i in range(10):
    x.append(randint(0, 360))
    y.append(randint(0,180) - 90)

print "TEST: "
for i in range(len(x)):
    print (round(codes_grib_find_nearest(gid1, y[i], x[i])[0].value - 273.15, 2),
           round(codes_grib_find_nearest(gid2, y[i], x[i])[0].value - 273.15, 2),
           round(codes_grib_find_nearest(gid3, y[i], x[i])[0].value - 273.15, 2),
           round(codes_grib_find_nearest(gid4, y[i], x[i])[0].value - 273.15, 2))

codes_release(gid1)
codes_release(gid2)
codes_release(gid3)
codes_release(gid4)

f1.close()
f2.close()
f3.close()
f4.close()


