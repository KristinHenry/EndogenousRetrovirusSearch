#

from matplotlib import pyplot, mpl

class plot3() :
    
    def __init__ (self, rows, cols, mapcolors) :  
        
        h = 10 #3
        w = 10 #cols * h
        
        self.mapcolors = mapcolors
            
        #self.dataColors = []
        
        # Make a figure and axes with dimensions input
        fig = pyplot.figure(figsize=(w,h), facecolor='w')
        
        yStart = .05
        xStart = .05
        dy = h/rows * .09 
        dx = w/cols * .09 
        
        rowlist = []
        i = rows
        while i > 0:
            rowlist.append(i-1)
            i -=1
        
        collist = []
        i = cols
        while i > 0:
            collist.append(i-1)
            i -=1
            
        numUnits = rows * cols
        #print numUnits   
        
        #numColors = len(mapcolors)
        #gap = numColors/numUnits
        
        
        # draw blocks
        colorid = 0
        for col in collist:
            for row in rowlist:
            
                rowNum = row
                colNum = col
                x = xStart + (colNum*dx)
                y = (rowNum*dy) + yStart 
                
                rect = [x, y, dx, dy]
                
                # get color for this grid from mapcolors
                color = self.getColor(row, col, rows, cols)
                #print color
                
                ax1 = fig.add_axes(rect, axisbg=color, xticklabels='', yticklabels='')                
                
                #colorid +=gap
        
        
        fig.savefig("colormap.png", dpi=300)
        pyplot.show()
      
      
        
    def colorPlot(self):
        
        return self.dataColors
    
    def getColor(self, row, col, rows, cols):
        for c in self.mapcolors:
            #print c
            if c[0]== row and c[1]== col:
                return c[2]
                
           
      
        