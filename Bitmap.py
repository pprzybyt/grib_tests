from eccodes import *
import numpy as np
import matplotlib.pyplot as plt
from settings import *

class Bitmap:

    def __init__(self, grib, path):
        self.Ni = codes_get(grib, 'Ni')
        self.Nj = codes_get(grib, 'Nj')
        self.name = codes_get(grib, "name")
        self.hour = int(codes_get(grib, "stepRange"))
        self.bitmap = np.zeros((self.Ni, self.Nj))
        self.grib = grib
        self.path = path
        self.missing_value = 0
        codes_set(self.grib, "missingValue", self.missing_value)
        self.im = 0
        self.fill_in()


    def fill_in(self):
        iter = codes_grib_iterator_new(self.grib, 0)
        for j in range(self.Nj):
            for i in range(self.Ni):
                result = codes_grib_iterator_next(iter)
                val = result[2]
                self.bitmap[i][j] = val
        self.bitmap = self.bitmap.transpose()
        codes_grib_iterator_delete(iter)

    def display(self):
        print sum(sum(self.bitmap))
        plt.figure().clear()
        time = int(self.hour % 24)
        plt.title(str(time) + ":00")
        plt.imshow(self.bitmap, interpolation='spline36')
        plt.colorbar()
        plt.savefig(IMAGES + self.path + ".png")
        plt.ion()
        plt.show()