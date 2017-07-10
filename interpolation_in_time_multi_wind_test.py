from eccodes.high_level.gribfile import *
from eccodes import  *
from ForecastError import ForecastError
from Bitmap import Bitmap
from TimeInterpolator import TimeInterpolator
import numpy as np
from settings import *
from matplotlib import pyplot as plt

f1 = open(SOURCE + "multi_1.glo_30m.t00z.f000.grib2")
f2 = open(SOURCE + "multi_1.glo_30m.t00z.f003.grib2")
f3 = open(SOURCE + "multi_1.glo_30m.t00z.f006.grib2")
for i in range(2):
    gid1 = codes_grib_new_from_file(f1)
    gid2 = codes_grib_new_from_file(f2)
    gid3 = codes_grib_new_from_file(f3)
    print codes_get(gid1, "name")


b = Bitmap(gid2, "glo_inte_t_test_f003")
ti = TimeInterpolator(gid1, gid3, 0.5,"glo_inte_t_test_f003a")
print "mean error: ", sum(sum(abs(np.subtract(ti.bitmap, b.bitmap)))) / ti.valid_points
print ti.Nj
err_over_1_proc = 0
err_over_2_proc = 0
err_over_5_proc = 0
err_over_10_proc = 0
err_over_30_proc = 0
err_over_50_proc = 0
err_over_01_mps = 0
err_over_02_mps = 0
err_over_05_mps = 0
err_over_1_mps = 0
err_over_2_mps = 0
err_over_5_mps = 0
points = 0
for j in range(ti.Nj):
    for i in range(ti.Ni):
        anal = b.bitmap[j][i]
        inter = ti.bitmap[j][i]
        if anal!=0. or inter!=0.:
            #print "analiza: ", anal, "interpolacja: ", inter, "error: ", abs(anal - inter), "error [%]", (inter - anal)/anal * 100.
            if abs((inter - anal) / anal) * 100. > 1:
                err_over_1_proc += 1
                if abs((inter - anal) / anal) * 100.0 > 2:
                    err_over_2_proc += 1
                    if abs((inter - anal) / anal) * 100. > 5:
                        err_over_5_proc += 1
                        if abs((inter - anal) / anal) * 100. > 10:
                            err_over_10_proc += 1
                            if abs((inter - anal) / anal) * 100. > 30:
                                err_over_30_proc += 1
                                if abs((inter - anal) / anal) * 100. > 50:
                                    err_over_50_proc += 1

            if abs(inter - anal) > .1:
                err_over_01_mps += 1
                if abs(inter - anal) > .2:
                    err_over_02_mps += 1
                    if abs(inter - anal) > .5:
                        err_over_05_mps += 1
                        if abs(inter - anal) > 1.:
                            err_over_1_mps += 1
                            if abs(inter - anal) > 2.:
                                err_over_2_mps += 1
                                if abs(inter - anal) > 5.:
                                    err_over_5_mps += 1
            points += 1



print "Ilosc pomiarow: ", points
print "Ilosc pomiarow z bledem do   1%: ", points - err_over_1_proc, 100. * (points -err_over_1_proc)/points, "%"
print "Ilosc pomiarow z bledem pow. 1%: ", err_over_1_proc, 100. * err_over_1_proc/points, "%"
print "Ilosc pomiarow z bledem pow. 2%: ", err_over_2_proc, 100. * err_over_2_proc/points, "%"
print "Ilosc pomiarow z bledem pow. 5%: ", err_over_5_proc, 100. * err_over_5_proc/points, "%"
print "Ilosc pomiarow z bledem pow. 10%: ", err_over_10_proc, 100. * err_over_10_proc/points, "%"
print "Ilosc pomiarow z bledem pow. 30%: ", err_over_30_proc, 100. * err_over_30_proc/points, "%"
print "Ilosc pomiarow z bledem pow. 50%: ", err_over_50_proc, 100. * err_over_50_proc/points, "%"
print "Ilosc pomiarow z bledem do   0.1 m/s: ", points - err_over_01_mps, 100. * (points -err_over_01_mps)/points, "%"
print "Ilosc pomiarow z bledem pow. 0.1 m/s: ", err_over_01_mps, 100. * err_over_01_mps/points, "%"
print "Ilosc pomiarow z bledem pow. 0.2 m/s: ", err_over_02_mps, 100. * err_over_02_mps/points, "%"
print "Ilosc pomiarow z bledem pow. 0.5 m/s: ", err_over_05_mps, 100. * err_over_05_mps/points, "%"
print "Ilosc pomiarow z bledem pow. 1.0 m/s: ", err_over_1_mps, 100. * err_over_1_mps/points, "%"
print "Ilosc pomiarow z bledem pow. 2.0 m/s: ", err_over_2_mps, 100. * err_over_2_mps/points, "%"
print "Ilosc pomiarow z bledem pow. 5.0 m/s: ", err_over_5_mps, 100. * err_over_5_mps/points, "%"


codes_release(gid1)
f1.close()
codes_release(gid2)
f2.close()
codes_release(gid3)
f3.close()
""" 
           if abs((inter - anal) / anal) * 100. > 1:
                err_over_1_proc += 1
                if abs((inter - anal) / anal)* 100.0 > 2:
                    err_over_2_proc += 1
                    if abs((inter - anal) / anal)* 100. > 5:
                        err_over_5_proc += 1
                        if abs((inter - anal) / anal)* 100. > 10:
                            err_over_10_proc += 1
                            if abs((inter - anal) / anal)* 100. > 30:
                                err_over_30_proc += 1
                                if abs((inter - anal) / anal) * 100. > 50:
                                    err_over_50_proc += 1
            """