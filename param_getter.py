import traceback
from eccodes import *
from settings import *
import matplotlib
from matplotlib import pyplot as plt
from Bitmap import Bitmap

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
print index_vals[0]


codes_index_select(iid, "shortName", "t")
codes_index_select(iid, "level", "0")
gid = codes_new_from_index(iid)
b1 = Bitmap(gid, "ocnf_1deg_temp_test")

for i in range(b1.Ni):
    for j in range(b1.Nj):
        if b1.bitmap[j][i] != 0:
            b1.bitmap[j][i] -= 273

b1.display()

print codes_get(gid, "name")



