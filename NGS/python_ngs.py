#!/usr/bin/env python3
#import sys
#file_name=sys.argv[1]
#base_quality_threshold=int(sys.argv[2])
sequence_list=[]
with open("SRR21901339.fastq", "r") as file_obj:
  for line in file_obj:
    line=line.rstrip()
    sequence=line.split()
    sequence_list.append(sequence)
  seq_rev=sequence_list[::-1]
  phred=  
 for seq in seq_rev:
    if phred 
      
