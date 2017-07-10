from random import randint
from eccodes import *
from settings import *

x = []
y = []
v1 = []
v2 = []

for i in range(10):
    x.append(randint(0, 360))
    y.append(randint(0,180) - 90)

f = open(SOURCE + "temp_test_03_07.grib2")

gid1 = codes_grib_new_from_file(f)
gid2 = codes_grib_new_from_file(f)
gid3 = codes_grib_new_from_file(f)

for i in range(len(x)):
    v1.append(round(codes_grib_find_nearest(gid2, y[i], x[i])[0].value - 273.15, 2))
    v2.append(round(codes_grib_find_nearest(gid3, y[i], x[i])[0].value - 273.15, 2))

for i, (lat, lon) in enumerate(zip(x, y)):
    print "[", lat, ",", lon, "]   : ", (v1[i]+v2[i]) / 2.
