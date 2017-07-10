from eccodes import *
from Bitmap import Bitmap
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from settings import *
from TimeInterpolator import TimeInterpolator

f = open(SOURCE + "temperature.grib2")

N = 8
n = 3 # beetween forecasts
b = []

gid1 = codes_grib_new_from_file(f)
gid2 = codes_grib_new_from_file(f)

for i in range(N):
    b.append(Bitmap(gid1, "lala").bitmap)
    for j in range(1, n):
        b.append((TimeInterpolator(gid1, gid2, j/3., "lala").bitmap))
    gid1 = gid2
    gid2 = codes_grib_new_from_file(f)


ims = []
fig = plt.figure()

print "len(b): ", len(b)
for i in range(len(b)):
    im = plt.imshow(b[i], animated=True, interpolation="spline36")
    plt.title(str(i))
    cb = plt.colorbar()
    plt.savefig(IMAGES + "ani_inter" + str(i) + ".png")
    cb.remove()
    ims.append([im])
    print i
plt.title("TEMPERATURE")
ani = animation.ArtistAnimation(fig, ims,interval=100, blit=True,repeat_delay=0)

ani.save(SOURCE + "x_inter.mp4")

f.close()
