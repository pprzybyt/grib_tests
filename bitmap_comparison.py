from eccodes.high_level.gribfile import *
from eccodes import  *
from ForecastError import ForecastError
from Bitmap import Bitmap
from TimeInterpolator import TimeInterpolator
import numpy as np
from settings import *
from matplotlib import pyplot as plt

f1 = open(SOURCE + "multi_1.ak_10m.t00z.f000.grib2")
f2 = open(SOURCE + "multi_1.ak_10m.t00z.f003.grib2")
f3 = open(SOURCE + "multi_1.ak_10m.t00z.f006.grib2")

gid1 = codes_grib_new_from_file(f1)
gid2 = codes_grib_new_from_file(f2)
gid3 = codes_grib_new_from_file(f3)
b = []
b.append(Bitmap(gid1, "TI_0").bitmap)
#b[-1].display()
for i in range(1, 3):
    b.append(TimeInterpolator(gid1, gid2, i/3., str(i)).bitmap)

b.append(Bitmap(gid2, "TI_3").bitmap)
#b[-1].display()

for i in range(1, 3):
    b.append(TimeInterpolator(gid2, gid3, i/3., str(i + 3)).bitmap)

b.append(Bitmap(gid3, "TI_6").bitmap)
#b[-1].display()

fig, ax = plt.subplots(3, sharex = True)
i = 0
for axes in ax:
    axes.set_title(str(i))
    im = axes.imshow(b[i])
    i += 1

fig.subplots_adjust(right = .8)
cb_ax = fig.add_axes([.85, .15, .05, .7])
fig.colorbar(im, cax = cb_ax)
plt.savefig(IMAGES + "ak_comparison_1.png")

fig, ax = plt.subplots(3, sharex = True)
for axes in ax:
    axes.set_title(str(i))
    im = axes.imshow(b[i])
    i += 1

fig.subplots_adjust(right = .8)
cb_ax = fig.add_axes([.85, .15, .05, .7])
fig.colorbar(im, cax = cb_ax)
plt.savefig(IMAGES + "ak_comparison_2.png")

"""
b = Bitmap(gid3)
b.display()
print "mean error: ", sum(sum(abs(np.subtract(ti.bitmap, b.bitmap)))) / ti.valid_points

for j in range(ti.Nj/4):
    for i in range(ti.Ni/4):
        anal = b.bitmap[j][i]
        inter = ti.bitmap[j][i]
        if anal!=0. or inter!=0.:
            print "analiza: ", anal, "interpolacja: ", inter, "error: ", abs(anal - inter), "error [%]", (inter - anal)/anal * 100.
"""

codes_release(gid1)
f1.close()
codes_release(gid2)
f2.close()
#codes_release(gid3)
#f3.close()
