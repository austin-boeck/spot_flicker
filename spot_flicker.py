import numpy as np
import matplotlib.pyplot as plt
#

'''
Need to read lc in with np including time, flux, error each in separate arrays

'''
file = '4171937.lc'

time, flux, err = np.loadtxt(file, usecols=(1,2,3), unpack = True)

#plot of time vs flux

plt.figure()
plt.plot(time, flux, 'g')
#plt.ylabel('Equivalent Duration (ergs maybe?)')
#plt.xlabel('Flare Duration (Minutes)')
plt.show()


