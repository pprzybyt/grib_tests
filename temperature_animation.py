from eccodes import *
from Bitmap import Bitmap
from matplotlib import pyplot as plt
import matplotlib.animation as animation
from settings import *

f = open(SOURCE + "temperature.grib2")

N = 8
b = []
ims = []
fig = plt.figure()


for i in range(N):
    gid = codes_grib_new_from_file(f)
    bit = Bitmap(gid, str(i))
    im = plt.imshow(bit.bitmap, animated=True, interpolation="spline36")
    plt.title(str(i))
    cb = plt.colorbar()
    plt.savefig(IMAGES + "temp" + str(i) + ".png")
    cb.remove()
    ims.append([im])
    codes_release(gid)
    print i
plt.title("TEMPERATURE")

ani = animation.ArtistAnimation(fig, ims,interval=300, blit=True,repeat_delay=0)

ani.save(SOURCE + "x.mp4")

f.close()
