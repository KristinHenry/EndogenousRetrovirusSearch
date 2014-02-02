#

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

class plot2() :
    
    def __init__ (self, rows, cols) :      
        
        X = 10*np.random.rand(rows,cols)

        fig = plt.figure()
        ax = fig.add_subplot(111)
        ax.imshow(X, cmap=cm.jet, interpolation='nearest')
        
        numrows, numcols = X.shape
        def format_coord(x, y):
            col = int(x+0.5)
            row = int(y+0.5)
            if col>=0 and col<numcols and row>=0 and row<numrows:
                z = X[row,col]
                return 'x=%1.4f, y=%1.4f, z=%1.4f'%(x, y, z)
            else:
                return 'x=%1.4f, y=%1.4f'%(x, y)
        
        ax.format_coord = format_coord
        plt.show()
           
    
   

   

     
     
        