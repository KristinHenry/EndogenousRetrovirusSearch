#
import numpy as np
import matplotlib.mathtext as mathtext
import matplotlib.pyplot as plt
import matplotlib


class drawCluster() :
    
    def __init__ (self, row, col, mycolor, seqStrings=None) :  
        
        print "draw cluster", row, col, mycolor
        print seqStrings
        
        filename = "sequences" + `row` + `col` + ".png"
        matplotlib.rc('image', origin='upper')
        parser = mathtext.MathTextParser("Bitmap")
        
        h = 10#.15 * len(self.seqdata) #3
        w = 20        
        fig = plt.figure(figsize=(w,h), facecolor='w')
        #fig.savefig(filename)
        
        mydpi = 200
        
        line = 0
        for seq in seqStrings:
            print seq
            
            fsize = 8
            rgba1, depth1 = parser.to_rgba(seq, color=mycolor, fontsize=fsize, dpi=mydpi)
            
            x = 10
            y = 10 + (22*line) #1100 - (5*i)
            fig.figimage(rgba1.astype(float)/255., x, y)
            
            line += 1
            
        plt.savefig(filename, dpi=mydpi)
        
        
      
   
  
                
           
            
   
     
     
        