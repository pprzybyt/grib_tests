from eccodes import *

class ForecastError:

    def __init__(self, grib1, grib2):
        self.Ni = codes_get(grib1, 'Ni')
        self.Nj = codes_get(grib1, 'Nj')
        self.lat_0 = codes_get(grib1, 'latitudeOfFirstGridPointInDegrees')
        self.lon_0 = codes_get(grib1, 'longitudeOfFirstGridPointInDegrees')
        self.lat_n = codes_get(grib1, 'latitudeOfLastGridPointInDegrees')
        self.lon_n = codes_get(grib1, 'longitudeOfLastGridPointInDegrees')

        self.forecast_grib = grib1
        self.analisys_grib = grib2

        self.missing_value = 1e+20

        codes_set(self.forecast_grib, "missingValue", self.missing_value)
        codes_set(self.analisys_grib, "missingValue", self.missing_value)

    def analyse_error(self):
        error = 0

        f_iter = codes_grib_iterator_new(self.forecast_grib, 0)
        a_iter = codes_grib_iterator_new(self.analisys_grib, 0)
        i = 1
        while 1:
            result1 = codes_grib_iterator_next(f_iter)
            result2 = codes_grib_iterator_next(a_iter)

            if not result1 or not result2:
                break
            val1 = result1[2]
            val2 = result2[2]
            if val1 != self.missing_value and val2 != self.missing_value:
                error += abs(val1 - val2)
                i += 1

            if (i) % 1000 == 0:
                print i, error, error/(i-1), val1, val2

        codes_grib_iterator_delete(f_iter)
        codes_grib_iterator_delete(a_iter)
        return error/ (i-1)
