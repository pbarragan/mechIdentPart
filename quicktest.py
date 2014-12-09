import numpy as np
from matplotlib import pyplot

thf = np.arange(-np.pi,np.pi,.1)
thi = np.pi/2
Kx = 10
Ky = 10
r = 0.56
ax = 0.06
ay = 0.06

dEdth = r*(Kx*(r*np.cos(thi)+ax)*np.sin(thf)-Ky*(r*np.sin(thi)+ay)*np.cos(thf))+r*r*((Ky-Kx)*np.sin(thf)*np.cos(thf))

pyplot.plot(thf,dEdth)
pyplot.show()
