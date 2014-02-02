#!/usr/bin/env python2

import Bio.AlignIO
import operator

def _clustal_process( inputFile ):
    star_info = inputFile._star_info
    record_one = str( inputFile._records[0].seq )
    middle_entry_index = ( len( inputFile._records ) / 2 )

    common_sequence = []
    for x, character in enumerate( star_info ):
        if character == '*':
            common_sequence.append( inputFile._records[middle_entry_index].seq[x] )
        elif character == ' ': continue #Nothing matching properly
        elif ( character == '.' ) or ( character == ':' ):
            char_count = {}
            for record in ( inputFile._records ):
                if record.seq[x] in char_count:
                    char_count[record.seq[x]] = char_count[record.seq[x]] + 1 #Increment count
                else:
                    char_count[record.seq[x]] = 1 #Initialize count
            key = max( char_count.iteritems(), key = operator.itemgetter( 1 ) )[0] #Hackery to get the highest value key from list
            common_sequence.append( key ) #None are going to agree, default to record_two

        else:
            print( "Unknown character at point " + str( x ) + " in sequence." )
            print( "Character ASCII representation: " + str( ord( character ) ) )

    print ( "Final common sequence: " )
    str_common_sequence = ''.join( common_sequence )
    print( str_common_sequence )
    print( "Sequence Length: " + str( len( str_common_sequence ) ) )

    return str_common_sequence


clustal_align_pol = Bio.AlignIO.read( "../clustalw/withoutMoloney/pol_complete_woMoloney_seqs.aln", "clustal" )
clustal_align_env = Bio.AlignIO.read( "../clustalw/withoutMoloney/env_complete_woMoloney_seqs.aln", "clustal" )
clustal_align_gag = Bio.AlignIO.read( "../clustalw/withoutMoloney/gag_complete_woMoloney_seqs.aln", "clustal" )



outData = _clustal_process( clustal_align_pol )
f = open( "common_protein_seq_POL.fasta", 'w' )
f.write( outData )
f.close()

outData = _clustal_process( clustal_align_gag )
f = open( "common_protein_seq_GAG.fasta", 'w' )
f.write( outData )
f.close()

outData = _clustal_process( clustal_align_env )
f = open( "common_protein_seq_ENV.fasta", 'w' )
f.write( outData )
f.close()
