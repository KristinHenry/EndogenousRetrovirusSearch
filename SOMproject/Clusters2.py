#

class Clusters2() :
    
    def __init__ (self) :
        
        self.cluster00 = []
        self.cluster01 = []
        self.cluster02 = []
        self.cluster03 = []
        self.cluster04 = []
        self.cluster10 = []
        self.cluster11 = []
        self.cluster12 = []
        self.cluster13 = []
        self.cluster14 = []
        self.cluster20 = []
        self.cluster21 = []
        self.cluster22 = []
        self.cluster23 = []
        self.cluster24 = []
        self.cluster30 = []
        self.cluster31 = []
        self.cluster32 = []
        self.cluster33 = []
        self.cluster34 = []
        self.cluster40 = []
        self.cluster41 = []
        self.cluster42 = []
        self.cluster43 = []
        self.cluster44 = []
            
        
        
    def addToCluster(self, row, col, id):
        
        if row == 0 and col  == 0:
            self.cluster00.append(id)
        if row == 0 and col  == 1:
            self.cluster01.append(id)
        if row == 0 and col  == 2:
            self.cluster02.append(id)
        if row == 0 and col  == 3:
            self.cluster03.append(id)
        if row == 0 and col  == 4:
            self.cluster04.append(id)
        if row == 1 and col  == 0:
            self.cluster10.append(id)
        if row == 1 and col  == 1:
            self.cluster11.append(id)
        if row == 1 and col  == 2:
            self.cluster12.append(id)
        if row == 1 and col  == 3:
            self.cluster13.append(id)
        if row == 1 and col  == 4:
            self.cluster14.append(id)
        if row == 2 and col  == 0:
            self.cluster20.append(id)
        if row == 2 and col  == 1:
            self.cluster21.append(id)
        if row == 2 and col  == 2:
            self.cluster22.append(id)
        if row == 2 and col  == 3:
            self.cluster23.append(id)
        if row == 2 and col  == 4:
            self.cluster24.append(id)
        if row == 3 and col  == 0:
            self.cluster30.append(id)
        if row == 3 and col  == 1:
            self.cluster31.append(id)
        if row == 3 and col  == 2:
            self.cluster32.append(id)
        if row == 3 and col  == 3:
            self.cluster33.append(id)
        if row == 3 and col  == 4:
            self.cluster34.append(id)
        if row == 4 and col  == 0:
            self.cluster40.append(id)
        if row == 4 and col  == 1:
            self.cluster41.append(id)
        if row == 4 and col  == 2:
            self.cluster42.append(id)
        if row == 4 and col  == 3:
            self.cluster43.append(id)
        if row == 4 and col  == 4:
            self.cluster44.append(id)

        
    def allClusters(self):       
    
        self.Clusters = []
        
        self.Clusters.append(self.cluster00)
        self.Clusters.append(self.cluster01)
        self.Clusters.append(self.cluster02)
        self.Clusters.append(self.cluster03)
        self.Clusters.append(self.cluster04)
        self.Clusters.append(self.cluster10)
        self.Clusters.append(self.cluster11)
        self.Clusters.append(self.cluster12)
        self.Clusters.append(self.cluster13)
        self.Clusters.append(self.cluster14)
        self.Clusters.append(self.cluster20)
        self.Clusters.append(self.cluster21)
        self.Clusters.append(self.cluster22)
        self.Clusters.append(self.cluster23)
        self.Clusters.append(self.cluster24)
        self.Clusters.append(self.cluster30)
        self.Clusters.append(self.cluster31)
        self.Clusters.append(self.cluster32)
        self.Clusters.append(self.cluster33)
        self.Clusters.append(self.cluster34)
        self.Clusters.append(self.cluster40)
        self.Clusters.append(self.cluster41)
        self.Clusters.append(self.cluster42)
        self.Clusters.append(self.cluster43)
        self.Clusters.append(self.cluster44)
        
        return self.Clusters
            
   

     
     
        