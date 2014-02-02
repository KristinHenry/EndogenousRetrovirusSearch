#

class mapcolors() :
    
    def __init__ (self) :  
        
        self.colors1 = ['#FF3300', '#FF6600', '#FF9900', '#FFCC00',
                     '#FFFF00', '#CCFF00', '#99FF00', '#66FF00',
                     '#33FF00', '#00FF00', '#00FF33', '#00FF66']
        
        
        self.colors2 = ['#8B0A50','#473C8B', '#8A2BE2', '#483D8B', '#1874CD', '#53868B',
                      '#70DB93', '#20B2AA', '#7FFF00', '#FFF68F', '#FF7F00', '#FF4500']
        
        self.colors3 = ['#FF1199', '#FF0066', '#FF1133', '#FF0000',
                     '#FF3300', '#FF6600', '#FF9900', '#FFCC00',
                     '#FFFF00', '#CCFF00', '#99FF00', '#66FF00',
                     '#33FF00', '#00FF00', '#00FF33', '#00FF66',
                     '#00FF99', '#00FFCC', '#00FFFF', '#00CCFF',
                     '#0099FF', '#0066FF', '#0033FF', '#0000FF',
                     '#3300FF', '#6600FF', '#9900FF', '#FF00FF']
        
        
        
    def getColorMap(self, rows, cols):
        
        myColors = self.colors3
        numColors = len(myColors)
        
        numUnits = rows*cols
        
        gap = numColors/numUnits
        
        self.colormap = []
        colorid = 0
        
        for i in range(0,rows):
            #print "row ", i
            for j in range(0, cols):
                #print "col ", j
                #print "row", i, " col", j
                #print i, ",", j, " ", myColors[colorid]
                self.colormap.append([i, j, myColors[colorid]])           
                colorid += gap
        
        return self.colormap
    
    
    def getColor(self, row, col):
        for c in self.colormap:
            #print c
            if c[0]== row and c[1]== col:
                return c[2]
       
        
           
    
   

   

     
     
        