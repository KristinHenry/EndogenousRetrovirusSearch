#import seqData
import Bio
import Bio.AlignIO
from Bio import SeqIO
from Bio.Seq import Seq

import Bio.Cluster 
import numpy


if __name__ == '__main__' :
    
    dataPath = "env_complete_seqs.fasta"

    alignment = Bio.AlignIO.read( "env_complete_seqs.aln", "clustal" )
    
    print alignment
    
    
    sequences = [list(str(seq_record.seq)) for seq_record in alignment]
    seqEncoded = []


#    sequences = ['aaaaaaaaaaaaaaaa',
#                 'aaaaaaabbbbbbbbb',
#                 'jkuuuulrefkwmcko',
#                 'aaaaaaaaailjshdu',
#                 'abasdfchjuodheui',
#                 'jkasdflmnopsfrwt',
#                 'jkqqqqlrefkpuito',
#                 'huqqqqdshilhdtwe',
#                 'xxyzxyzxyzpsfert']
    
    # convert chars to integers
    for seq in sequences:
        tmp = []
        for elem in seq:
            tmp.append(ord(elem))
        seqEncoded.append(tmp)
    
   
    
    data = seqEncoded
    numIter = 1
    rows = 2
    cols = 2
    
    
    #tree = Bio.Cluster.treecluster(data=sequences, mask=None, weight=None, transpose=0, method='m', dist='e', distancematrix=None)
    clusterid, celldata = Bio.Cluster.somcluster(data, mask=None, weight=None, transpose=0, nxgrid=cols, nygrid=rows, inittau=0.02, niter=numIter, dist='e')
    
    print clusterid
    #print celldata
    
    print clusterid[0]
    
   
    
    