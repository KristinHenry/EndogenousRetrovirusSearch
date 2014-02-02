#

import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import numpy as np

class plot4() :
    
    def __init__ (self, rows, cols) :  
        
        h = 3
        w = cols * h
            
        
        maxnum = 13
        numfilled = 40
        x = np.random.randint(0, maxnum, size=numfilled)
        y = np.random.randint(0, maxnum, size=numfilled)
        z = x * y
        
        fig, ax = plt.subplots()
        
        for X,Y,Z in zip(x,y,z):
            ax.text(X+0.5,Y+0.5,str(Z), ha='center', va='center')
        
        ax.axis([0, maxnum, 0, maxnum])
        
        for axis in [ax.xaxis, ax.yaxis]:
            axis.set_minor_locator(MultipleLocator(1))
            axis.set_ticks(np.arange(maxnum) + 0.5)
            axis.set_ticklabels(range(maxnum))
        
        ax.grid(which='minor')
        ax.xaxis.set_ticks_position('top')
        
        plt.show()
        
       
        
           
    
   

   

     
     
        