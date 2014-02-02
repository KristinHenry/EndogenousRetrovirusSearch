#import seqData
#import Bio
#import Bio.AlignIO
#from Bio import SeqIO
#from Bio.Seq import Seq


import plot3
import mapcolors


if __name__ == '__main__' :
    
#    
    rows = 4
    cols = 3
    mc = mapcolors.mapcolors()
    colors = mc.colors3
   
    plot3.plot3(rows,cols, colors) 
   
    
    

    
   
    
    