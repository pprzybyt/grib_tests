from eccodes import *
import numpy as np
from matplotlib import pyplot as plt
from settings import *

class TimeInterpolator:

    def __init__(self, grib1, grib2, offset, path):
        self.path = path
        self.Ni = codes_get(grib1, 'Ni')
        self.Nj = codes_get(grib1, 'Nj')
        self.lat_0 = codes_get(grib1, 'latitudeOfFirstGridPointInDegrees')
        self.lon_0 = codes_get(grib1, 'longitudeOfFirstGridPointInDegrees')
        self.lat_n = codes_get(grib1, 'latitudeOfLastGridPointInDegrees')
        self.lon_n = codes_get(grib1, 'longitudeOfLastGridPointInDegrees')
        self.duration = abs(int(codes_get(grib1, "stepRange")) - int(codes_get(grib2, "stepRange")))
        self.offset = offset
        self.forecast_grib = grib2
        self.analisys_grib = grib1
        print self.duration
        self.missing_value = 1e+20
        self.bitmap = np.zeros((self.Ni, self.Nj))
        self.valid_points = 0

        codes_set(self.forecast_grib, "missingValue", self.missing_value)
        codes_set(self.analisys_grib, "missingValue", self.missing_value)
        self.interpolate()

    def interpolate(self):
        f_iter = codes_grib_iterator_new(self.forecast_grib, 0)
        a_iter = codes_grib_iterator_new(self.analisys_grib, 0)
        a = 1
        for j in range(self.Nj):
            for i in range(self.Ni):
                result1 = codes_grib_iterator_next(a_iter)[2]
                result2 = codes_grib_iterator_next(f_iter)[2]
                val = 0
                if result1 != self.missing_value and result1 != self.missing_value:
                    val = result1 + (result2 - result1)*self.offset
                    self.valid_points +=1

                self.bitmap[i][j] = val
                if i == 0:
                    print result1, val, result2

        codes_grib_iterator_delete(f_iter)
        codes_grib_iterator_delete(a_iter)
        self.bitmap = self.bitmap.transpose()
        self.display()

    def display(self):
        print sum(sum(self.bitmap))
        plt.figure().clear()
        plt.imshow(self.bitmap, interpolation='spline36')
        plt.colorbar()
        plt.show()
        plt.savefig(IMAGES + "TI_" + self.path + ".png")
       #cb.remove()
