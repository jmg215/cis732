import matplotlib.pyplot as plt
import numpy as np


def runme(fff):

    a1 = np.array([1,2,3,4,5])
    a2 = np.array([33,59,29,88,2])
    
    axarr = fff.subplots(1,1)
    axarr.set_title('plot this')
    axarr.set_xlim(-5,5)
    axarr.set_ylim(-5,5)
    axarr.set_xlabel('x axis is here')
    axarr.set_ylabel("CHARLIE MURPHY!")
    # axarr.legend(['im rick james bitch'])
    axarr.grid(True)
    axarr
    # axarr.plot(a1,a2)
    

    return axarr


   
eff = plt.figure(figsize = (11,8), dpi = 330)
   
f =  runme(fff = eff)
f.plot(1,4, marker = 'o')
f.legend(['im rick james bitch. enjoy yourself'])

