#
# Takes in a DNA sequence and ...
#
#import Bio
import Bio.AlignIO
#from Bio import SeqIO
#from Bio.Seq import Seq

class seqData() :
    
    def __init__ (self, infile=None) :      
        
        if infile :
            
            #alignment = Bio.AlignIO.read( "env_complete_seqs.aln", "clustal" )
            alignment = Bio.AlignIO.read(infile, "clustal")
            
            print alignment
            
            self.ids = [seq_record.id for seq_record in alignment]
            print self.ids
            
            self.seqs = [list(str(seq_record.seq)) for seq_record in alignment]
   
    
    def encode(self):
        self.encoded = []
 
        # convert chars to integers
        for seq in self.seqs:
            tmp = []
            for elem in seq:
                n = ord(elem)
                if n == 45: n = 0 # set empty "-" to be zero, to reduce it's effect in map
                tmp.append(n)
            self.encoded.append(tmp)
            
        return self.encoded
    
    def getStrings(self):
        
        tmp =[]
        
        i = 0
        for id in self.ids:
            st = id
            st = st + " "
            for char in self.seqs[i]:
                if char is not "-":
                    st = st + char 
                
            
            tmp.append(st)
            i +=1
            
        return tmp
            
            
        
             


   

     
     
        