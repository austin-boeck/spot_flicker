import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import pandas as pd

np.set_printoptions(threshold=np.nan)
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
plt.savefig('CandidateTime.png', dpi=300 )
#plt.show()




#Here I attempt to do the same as above, but with flare durations highlighted

file2 = '4171937.dat.fbeye'
 
peaktime, starttime, stoptime = np.loadtxt(file2, usecols=(3,4,5), unpack=True)

plt.figure()
plt.plot(time, flux, 'b') # plot the original data in blue
plt.ylabel('Equivalent Duration (ergs maybe?)')
plt.xlabel('Time (Days)')
plt.xlim(774, 786)
plt.ylim(13750,14000)
# now lets loop over every flare, find the data that falls within the start/stop times

for k in range(0, len(starttime)):
    # this finds WHERE the logic statements are true for the k'th given flare
    x = np.where((time >= starttime[k]) & (time <= stoptime[k]))

    # now let's plot that flare
    plt.plot(time[x], flux[x], c='red')
   
   #Here I attempt to use similar syntax as above to try to highlight peak times
for xc in peaktime:
    plt.axvline(x=xc, alpha = .15, c='orange')

plt.savefig('CT_W_flares.png', dpi=300 )
#plt.show()

'''
This following section attmepts to create arrays exactly like the arrays above for flux 
time, and error. However these arrays will not have any data that coincides with flares.
It then also plots that resulting data
'''

#This section creates exact copies of the arrays
time_sans = np.copy(time, order='K')
flux_sans = np.copy(flux, order = 'K')
err_sans =  np.copy(err, order='K')

#tThis section loops over each flare, and replaces the flare-data with nan
for i in range(0, len(starttime)):
   y = np.where((time >= starttime[i]) & (time <= stoptime[i]))
   
   time_sans[y] = [None]
   flux_sans[y] = [None]
   err_sans[y] = [None]
   
#Here the data is plotted  
plt.figure()
plt.ylabel('Equivalent Duration (ergs maybe?)')
plt.xlabel('Time (Days)')
plt.xlim(774, 786)
plt.ylim(13750,14000)

plt.plot(time_sans, flux_sans)
plt.savefig('CT_sans_flares.png', dpi=300)
#plt.show()
plt.close()
   
   
'''
This next section of code will attempt to smooth the curve
via a rolling median window (Here we go...)
'''

kernel = 15

data_mean = pd.rolling_mean(flux_sans, kernel, center=True)


   
#here the median data is plotted      
plt.figure()
plt.plot(time, flux, 'b') # plot the original data in blue
plt.ylabel('Equivalent Duration (ergs maybe?)')
plt.xlabel('Time (Days)')
plt.xlim(774, 786)
plt.ylim(13750,14000)


for k in range(0, len(starttime)):
    
    x = np.where((time >= starttime[k]) & (time <= stoptime[k]))
    plt.plot(time[x], flux[x], c='red')

plt.plot(time_sans, data_mean)
plt.savefig('CT_W_flares_K15.png', dpi=300 )
plt.show()

'''
In this next section, I will attempt to relate Error and flux against time. This part is still very much a work in progress.
'''

modulus = (flux_sans - data_mean) / err_sans 

plt.figure()
plt.ylabel('Relative Flux/Error')
plt.xlabel('Time (Days)')
plt.plot(time, modulus)
plt.savefig('Err-analysis.png', dpi=300)
plt.show()
















