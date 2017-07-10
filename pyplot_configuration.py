import matplotlib.rcsetup as rcsetup
import matplotlib.pyplot as plt
import matplotlib

print rcsetup.all_backends

plt.switch_backend("Qt5Agg")



print matplotlib.get_backend()

plt.figure()
plt.show()