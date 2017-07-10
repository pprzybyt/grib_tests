from settings import *
from eccodes import *

INPUT = SOURCE + '1.grib2'

def example():
    f = open(INPUT)

    i = 0
    while 1:
        gid = codes_grib_new_from_file(f)
        if gid is None:
            break

        iterid = codes_keys_iterator_new(gid, 'ls')
        print i, ":"
        print "day", codes_get_string(iterid, "day")
        print "hour", codes_get_string(iterid, "hour")
        print "name", codes_get_string(iterid, "name")
        print "stepRange", codes_get_string(iterid, "endStep")
        print "forecast", codes_get_string(iterid, "dataTime")
        print "ni", codes_get_string(iterid, "Ni")
        print "nj", codes_get_string(iterid, "Nj")




        i+=1

        codes_keys_iterator_delete(iterid)
        codes_release(gid)

    f.close()


example()