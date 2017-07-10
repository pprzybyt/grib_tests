from eccodes.high_level.gribfile import *
from eccodes import  *
from ForecastError import ForecastError
from Bitmap import Bitmap
from TimeInterpolator import TimeInterpolator
import numpy as np
from settings import *
from matplotlib import pyplot as plt

idx1_file = "my1.idx"
idx2_file = "my2.idx"
idx3_file = "my3.idx"

index_keys = ["shortName", "level"]
iid1 = codes_index_new_from_file(SOURCE + 'ocnf2017070506.01.2017070500.grb2', index_keys)
codes_index_write(iid1,SOURCE + idx1_file)
iid2 = codes_index_new_from_file(SOURCE + 'ocnf2017070512.01.2017070500.grb2', index_keys)
codes_index_write(iid1,SOURCE + idx2_file)
iid3 = codes_index_new_from_file(SOURCE + 'ocnf2017070518.01.2017070500.grb2', index_keys)
codes_index_write(iid1,SOURCE + idx3_file)

codes_index_select(iid1, "shortName", "ucurr")
codes_index_select(iid1, "level", "5")
codes_index_select(iid2, "shortName", "ucurr")
codes_index_select(iid2, "level", "5")
codes_index_select(iid3, "shortName", "ucurr")
codes_index_select(iid3, "level", "5")


gid1 = codes_new_from_index(iid1)
gid2 = codes_new_from_index(iid2)
gid3 = codes_new_from_index(iid3)


b = Bitmap(gid2, "ocnf_inte_t_test_f6")
ti = TimeInterpolator(gid1, gid3, 0.5,"ocnf_inte_t_test_f6a")
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
print "Ilosc pomiarow z bledem do   0.1 K: ", points - err_over_01_mps, 100. * (points -err_over_01_mps)/points, "%"
print "Ilosc pomiarow z bledem pow. 0.1 K: ", err_over_01_mps, 100. * err_over_01_mps/points, "%"
print "Ilosc pomiarow z bledem pow. 0.2 K: ", err_over_02_mps, 100. * err_over_02_mps/points, "%"
print "Ilosc pomiarow z bledem pow. 0.5 K: ", err_over_05_mps, 100. * err_over_05_mps/points, "%"
print "Ilosc pomiarow z bledem pow. 1.0 K: ", err_over_1_mps, 100. * err_over_1_mps/points, "%"
print "Ilosc pomiarow z bledem pow. 2.0 K: ", err_over_2_mps, 100. * err_over_2_mps/points, "%"
print "Ilosc pomiarow z bledem pow. 5.0 K: ", err_over_5_mps, 100. * err_over_5_mps/points, "%"

print codes_get(gid1, "name")
codes_release(gid1)
codes_release(gid2)
codes_release(gid3)
