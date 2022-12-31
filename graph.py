import numpy as np
import matplotlib.pyplot as plt
import matplotlib.dates
import time
from datetime import datetime

array = np.array([0.1,0.15,0.2])
time_m = np.array([2100,2130,2200])
while(True) :
    import putcallratio as pcr
    print(pcr.putcallratio())
    array = np.append(array,pcr.putcallratio())
    if (int(datetime.now().minute/10) == 0):
        time_m = np.append(time_m, int(str(datetime.now().hour) + "0" +str(datetime.now().minute)))
    else:
        time_m = np.append(time_m,int(str(datetime.now().hour) + str(datetime.now().minute)))
    plt.plot(time_m,array)
    plt.axhline(y=0, color='r', linestyle='-')
    plt.show()
    time.sleep(250)


