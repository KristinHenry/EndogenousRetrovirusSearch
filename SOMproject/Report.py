#

class Report() :
    
    def __init__ (self) :  
        print "report"
    
    def saveToFile(self, docPath, iters, rows, cols, clusterid, myColorMap):   
        f = open('resultsOut.txt', 'wb')
        
        f.write(`docPath` + "\r\n") 
        f.write("SOM iterations: " + `iters` + "\r\n")
        f.write("rows: " + `rows` + "  cols: " + `cols` + "\r\n")
        
        f.write("Cluster IDs: \r\n")
        for id in clusterid:
            f.write(`id` + "\r\n")
        
        f.write("Color Map: \r\n")
        for color in myColorMap:
            f.write(`color` + "\r\n")
        
        f.close()
        
   
        
      
   
  
                
           
            
   
     
     
        