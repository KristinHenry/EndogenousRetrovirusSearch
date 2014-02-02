#!/usr/bin/env python2
"""
@author: Ty Davis
@date: 03.12.2011

Filter and reduce the BLAST results for ClustalW
"""

from Bio.Blast import NCBIXML
import logging

def filter_results( records ):
    filtered_blast_alignments = []
    for index in records.alignments:
        actionStr = index.hit_def.lower()
        if "predicted" in actionStr: logging.debug( "Filtering item: " + actionStr )
        elif "unnamed" in actionStr: logging.debug( "Filtering item: " + actionStr )
        #elif "unknown" in actionStr:logging.debug( "Filtering item: " + actionStr )
        elif "novel" in actionStr: logging.debug( "Filtering item: " + actionStr )
        else: filtered_blast_alignments.append( index )
    logging.info( "Blast records remaining: " + str( len( filtered_blast_alignments ) ) )
    return filtered_blast_alignments

def parse_alignments( outfile, records ):
    i = 0
    for item in records:
        logging.info( "Sequence " + str( i ) + " is: " )
        logging.info( item ) #Give them their alignments.
        shortened_title = item.hit_def[:29]
        print >> outfile, ( ">" + item.hit_id + shortened_title + str( i ) ) #Need to make Unique entries for clustalw
        matchSequence = item.hsps[0]
        print >> outfile, matchSequence.sbjct[:]
        i = i + 1
    return

logging.basicConfig( filename = "process_blast_results.log", filemode = 'w', level = logging.DEBUG, format = '%(asctime)s %(levelname)-8s %(message)s', datefmt = '%Y-%m-%d %H:%M:%S', )

xmlHandle = open( "../blastp_results/ENV_against_Mouse_DXMPZXG801N-Alignment.xml" )
blast_records = NCBIXML.read( xmlHandle )
logging.info( "BLAST data read." )

local_alignments = filter_results( blast_records )
clustalW_dump = open( "psiBlast_ENV_against_Mouse.fasta", 'w' ) #Where we're dumping the input for clustalw
parse_alignments( clustalW_dump, local_alignments )
clustalW_dump.close()

xmlHandle = open( "../blastp_results/GAG_against_Mouse_DXN1H0HK01S-Alignment.xml" )
blast_records = NCBIXML.read( xmlHandle )
logging.info( "BLAST data read." )

local_alignments = filter_results( blast_records )
clustalW_dump = open( "psiBlast_GAG_against_Mouse.fasta", 'w' ) #Where we're dumping the input for clustalw
parse_alignments( clustalW_dump, local_alignments )
clustalW_dump.close()

xmlHandle = open( "../blastp_results/POL_against_Mouse_DXNAPD5101N-Alignment.xml" )
blast_records = NCBIXML.read( xmlHandle )
logging.info( "BLAST data read." )

local_alignments = filter_results( blast_records )
clustalW_dump = open( "psiBlast_POL_against_Mouse.fasta", 'w' ) #Where we're dumping the input for clustalw
parse_alignments( clustalW_dump, local_alignments )
clustalW_dump.close()
