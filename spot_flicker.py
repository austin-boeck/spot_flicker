import numpy as np
import matplotlib
from matplotlib.patches import Polygon
import matplotlib.pyplot as plt

#

'''
Need to read lc in with np including time, flux, error each in separate arrays

'''
file = '4171937.lc'

time, flux, err = np.loadtxt(file, usecols=(1,2,3), unpack = True)



#plot of time vs flux of an interesting light curve segment

plt.figure()
plt.plot(time, flux, 'g')
plt.xlim(774, 786)
plt.ylim(13750,14000)
plt.ylabel('Equivalent Duration (ergs maybe?)')
plt.xlabel('Time (Days)')
plt.show()
plt.savefig('CandidateTime' )

#Here I attempt to do the same as above, but with flare durations highlighted

file2 = '4171937.dat.fbeye'
 
flaretimes = np.loadtxt(file2, usecols=(5,6))

#plt.figure()
#plt.plot(time, flux, 'g')
#plt.Polygon(flaretimes, closed=False , c = 'y')
#plt.xlim(774, 786)
#plt.ylim(13750,14000)
#plt.ylabel('Equivalent Duration (ergs maybe?)')
#plt.xlabel('Time (Days)')
#plt.show()
#plt.savefig('CT_W_flares' )

