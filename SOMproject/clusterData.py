#
# Takes in a DNA sequence and ...
#

class clusterData() :
    
    def __init__ (self, ids, color, seqstrings) :      
        
        self.ids = ids
        #print "cluster data: ", self.ids
        self.clustSeqs = self.getStrings(seqstrings)
            
            
    def getStrings(self, seqstrings):
        
        clustSeqs = []
        
        for id in self.ids:
            #print "id", id
            #print seqstrings[id]
            clustSeqs.append(seqstrings[id])
         
          
        return clustSeqs
            

   

     
     
        