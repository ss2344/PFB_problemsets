#!/usr/bin/env python3
import sys
#from Bio.Blast import NCBIXM
BL50200_dict={}
with open (sys.argv[1],'r') as BL50200:
  for line in BL50200:
    line=line.rstrip()
    if not line.startswith('#'):
      line.split('\t')
      #print(line.split('\t'))
      BL50200_dict=dict(zip(['qseqid', 'sseqid', 'percid', 'alen', 'mismat', 'gaps', 'q_start', 'q_end', 's_start', 's_end', 'evalue', 'bits'],line.split('\t')))
      print(BL50200_dict)

BL62200_dict={}
with open (sys.argv[1],'r') as BL62200:
  for line in BL62200:
    line=line.rstrip()
    if not line.startswith('#'):
      line.split('\t')
      BL62200_dict=dict(zip(['qseqid', 'sseqid', 'percid', 'alen', 'mismat', 'gaps', 'q_start', 'q_end', 's_start', 's_end', 'evalue', 'bits'],line.split('\t')))
      print(BL62200_dict)



VT10200_dict={}
with open (sys.argv[1],'r') as VT10200:
  for line in VT10200:
    line=line.rstrip()
    if not line.startswith('#'):
      line.split('\t')
      VT10200_dict=dict(zip(['qseqid', 'sseqid', 'percid', 'alen', 'mismat', 'gaps', 'q_start', 'q_end', 's_start', 's_end', 'evalue', 'bits'],line.split('\t')))
      print(VT10200_dict)
VT160200_dict={}
with open (sys.argv[1],'r') as VT160200:
  for line in VT160200:
    line=line.rstrip()
    if not line.startswith('#'):
      line.split('\t')
    VT160200_dict=dict(zip(['qseqid', 'sseqid', 'percid', 'alen', 'mismat', 'gaps', 'q_start', 'q_end', 's_start', 's_end', 'evalue', 'bits'],line.split('\t')))
    print(VT160200_dict)

