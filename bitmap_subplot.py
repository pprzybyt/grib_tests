from eccodes.high_level.gribfile import *
from eccodes import  *
from ForecastError import ForecastError
from Bitmap import Bitmap
from TimeInterpolator import TimeInterpolator
import numpy as np
from matplotlib import pyplot as plt
from settings import *

f = open(SOURCE + "tmpsfc_00.grib2")

gid1 = codes_grib_new_from_file(f)
gid2 = codes_grib_new_from_file(f)
gid3 = codes_grib_new_from_file(f)

b1 = Bitmap(gid1, "temp_inter_test1")
b2 = Bitmap(gid2, "temp_inter_test2")
b3 = Bitmap(gid3, "temp_inter_test3")
fig, ax = plt.subplots(3, sharex = True)
ax[0].set_title("6:00")
ax[1].set_title("12:00")
ax[2].set_title("18:00")
im = ax[0].imshow(b1.bitmap - 273.15)
im = ax[1].imshow(b2.bitmap - 273.15)
im = ax[2].imshow(b3.bitmap - 273.15)

fig.subplots_adjust(right = .8)
cb_ax = fig.add_axes([.85, .15, .05, .7])
fig.colorbar(im, cax = cb_ax)
plt.savefig(IMAGES + "comparison.png")

b1.display()
codes_release(gid1)
codes_release(gid2)
codes_release(gid3)
f.close()

