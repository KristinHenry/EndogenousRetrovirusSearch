#import seqData
#import Bio
#import Bio.AlignIO
#from Bio import SeqIO
#from Bio.Seq import Seq


import Bio.Cluster 
#import numpy


import seqData
import plot3
import mapcolors
import Clusters
import clusterData
import drawCluster


#import chartClusters
import chartClusterSingle
import Report



if __name__ == '__main__' :
    
#    docPath = "env_complete_seqs.aln"
#    docPath = "gag_complete_seqs.aln"
#    docPath = "pol_complete_seqs.aln"
#    docPath = "psiBlast_clustal_source.aln"
#    docPath="psiBlast_POL_against_Mouse.aln"
#    docPath="psiBlast_GAG_against_Mouse.aln"
    docPath="psiBlast_ENV_against_Mouse.aln"
    
    
    seqdata = seqData.seqData(docPath)
    encoded = seqdata.encode()
    #print encoded
            
    
    data = encoded
    numIter = 1
    rows = 5
    cols = 5
    
    
    #tree = Bio.Cluster.treecluster(data=sequences, mask=None, weight=None, transpose=0, method='m', dist='e', distancematrix=None)
    clusterid, celldata = Bio.Cluster.somcluster(data, mask=None, weight=None, transpose=0, nxgrid=cols, nygrid=rows, inittau=0.02, niter=numIter, dist='e')


    cl = Clusters.Clusters()


    id = 0
    for cluster in clusterid:
        cl.addToCluster(cluster[0], cluster[1], id)
        print cluster
        id += 1
    
    
    mc = mapcolors.mapcolors()
    colors = mc.colors3
    myColorMap = mc.getColorMap(rows, cols)
    print myColorMap
    

    seqStrings = seqdata.getStrings()
    print seqStrings
    
    
    for i in range(0,rows):
        for j in range(0,cols):
            
            #print i, j
            ids = cl.getClusterSeqIds(i, j)
            #print ids
            color = mc.getColor(i, j)
            #print color
            
            cdata = clusterData.clusterData(ids, color, seqStrings)
            print "cluster count: ", len(cdata.clustSeqs)
            if len(cdata.clustSeqs) > 0:
                print "print"
                drawCluster.drawCluster(i, j, color, cdata.clustSeqs)
    
   
    # draw color chart
    myplot = plot3.plot3(rows,cols, myColorMap) 
    
    report = Report.Report()
    report.saveToFile(docPath, numIter, rows, cols, clusterid, myColorMap)
    




    
    
    
    
    

    
   
    
    