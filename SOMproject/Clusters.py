#

class Clusters() :
    
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

        
        
    def getClusterSeqIds(self, row, col):
        
        if row == 0 and col  == 0:
            return self.cluster00
        if row == 0 and col  == 1:
            return self.cluster01
        if row == 0 and col  == 2:
            return self.cluster02
        if row == 0 and col  == 3:
            return self.cluster03
        if row == 0 and col  == 4:
            return self.cluster04
        if row == 1 and col  == 0:
            return self.cluster10
        if row == 1 and col  == 1:
            return self.cluster11
        if row == 1 and col  == 2:
            return self.cluster12
        if row == 1 and col  == 3:
            return self.cluster13
        if row == 1 and col  == 4:
            return self.cluster14
        if row == 2 and col  == 0:
            return self.cluster20
        if row == 2 and col  == 1:
            return self.cluster21
        if row == 2 and col  == 2:
            return self.cluster22
        if row == 2 and col  == 3:
            return self.cluster23
        if row == 2 and col  == 4:
            return self.cluster24
        if row == 3 and col  == 0:
            return self.cluster30
        if row == 3 and col  == 1:
            return self.cluster31
        if row == 3 and col  == 2:
            return self.cluster32
        if row == 3 and col  == 3:
            return self.cluster33
        if row == 3 and col  == 4:
            return self.cluster34
        if row == 4 and col  == 0:
            return self.cluster40
        if row == 4 and col  == 1:
            return self.cluster41
        if row == 4 and col  == 2:
            return self.cluster42
        if row == 4 and col  == 3:
            return self.cluster43
        if row == 4 and col  == 4:
            return self.cluster44

   

     
     
        