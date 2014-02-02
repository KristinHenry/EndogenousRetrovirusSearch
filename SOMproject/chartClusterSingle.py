#



class chartClusterSingle() :
    
    def __init__ (self, row, col, mapcolors, clusterid, seqdata, ids) :  
        import numpy as np
        import matplotlib.mathtext as mathtext
        import matplotlib.pyplot as plt
        import matplotlib
        
        self.mapcolors = mapcolors
        self.clusterid = clusterid
        self.seqdata = seqdata
        self.seqids = ids
        
        matplotlib.rc('image', origin='upper')
        
        parser = mathtext.MathTextParser("Bitmap")
        
        filename = "sequences" + `row` + `col` + ".png"
        print filename
       
        #filename = 'sequences.png' # "sequences" + num +".png"    #'sequences.png' #'sequences',  str(k), '.png'
        #parser.to_png(filename, r'$\left[\left\lfloor\frac{5}{\frac{\left(3\right)}{4}} y\right)\right]$', color='green', fontsize=14, dpi=100)
        print len(self.seqdata)
        h = 10#.15 * len(self.seqdata) #3
        w = 20 
                
                
                
        fig = plt.figure(figsize=(w,h), facecolor='w')
        #fig.savefig(filename)
                
        i = 0   
        line = 0
        for seq in self.seqdata:
            if clusterid[i][0] == row and clusterid[i][1]== col:
                
                print self.seqids[i]
                str = self.seqids[i] + ' '
                        
                for elem in seq:
                    #if elem == "-": elem = " "
                    if elem != "-":
                        str = str + elem
                #print str
                #print i, self.clusterid[i], " ", self.clusterid[i][0], " ", self.clusterid[i][1]
                c = self.getColor(self.clusterid[i][0], self.clusterid[i][1])
                #print "row ", self.clusterid[i][0]
                #print "col", self.clusterid[i][1]
                fsize = 2
                rgba1, depth1 = parser.to_rgba(str, color=c, fontsize=fsize, dpi=300)
                #fig.figimage(rgba1.astype(float)/255., 10, 300 - (10*i))
                x = 10
                y = 10 + (10*line) #1100 - (5*i)
                fig.figimage(rgba1.astype(float)/255., x, y)
                line += 1
                        
            i += 1
        
        if line > 0:
            print "save file"
            plt.savefig(filename, dpi=100)
        
        #plt.show()
        
        
      
   
    
    def getColor(self, row, col):
        for c in self.mapcolors:
            #print c
            if c[0]== row and c[1]== col:
                return c[2]
                
           
            
   
     
     
        