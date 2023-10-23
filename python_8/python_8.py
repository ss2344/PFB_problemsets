#!/usr/bin/env python3
import re
seq_dict={}
header=[]
sequence=[]
with open ("Python_08.fasta", "r") as file_obj:
  for line in file_obj:
    line=line.rstrip()
    if line.startswith('>'):
       header=line.split()
       sequence=[]       
    elif not line.startswith('>'):
       sequence.append(line)
       seq_dict[header[0]]=''.join(sequence)
print(seq_dict)        
nts_in_seqdict={}
for key in seq_dict:
  nts_in_seqdict[key]={}
  nts_in_seqdict[key]['A']=seq_dict[key].count('A')
  nts_in_seqdict[key]['T']=seq_dict[key].count('T')
  nts_in_seqdict[key]['G']=seq_dict[key].count('G')
  nts_in_seqdict[key]['C']=seq_dict[key].count('C')
print(nts_in_seqdict)

#2

with open ("Python_08.fasta", "r") as file_obj:
  for sequence in seq_dict:
    codon = re.findall(r"(.{3})",seq_dict[sequence])
    print(codon)
  #codons= re.search(r"(.{3})",sequence)
  #print(codons)

translation_table = {
    'GCT':'A', 'GCC':'A', 'GCA':'A', 'GCG':'A',
    'CGT':'R', 'CGC':'R', 'CGA':'R', 'CGG':'R', 'AGA':'R', 'AGG':'R',
    'AAT':'N', 'AAC':'N',
    'GAT':'D', 'GAC':'D',
    'TGT':'C', 'TGC':'C',
    'CAA':'Q', 'CAG':'Q',
    'GAA':'E', 'GAG':'E',
    'GGT':'G', 'GGC':'G', 'GGA':'G', 'GGG':'G',
    'CAT':'H', 'CAC':'H',
    'ATT':'I', 'ATC':'I', 'ATA':'I',
    'TTA':'L', 'TTG':'L', 'CTT':'L', 'CTC':'L', 'CTA':'L', 'CTG':'L',
    'AAA':'K', 'AAG':'K',
    'ATG':'M',
    'TTT':'F', 'TTC':'F',
    'CCT':'P', 'CCC':'P', 'CCA':'P', 'CCG':'P',
    'TCT':'S', 'TCC':'S', 'TCA':'S', 'TCG':'S', 'AGT':'S', 'AGC':'S',
    'ACT':'T', 'ACC':'T', 'ACA':'T', 'ACG':'T',
    'TGG':'W',
    'TAT':'Y', 'TAC':'Y',
    'GTT':'V', 'GTC':'V', 'GTA':'V', 'GTG':'V',
    'TAA':'*', 'TGA':'*', 'TAG':'*'
}
for triplets in codon:
   codon=translation_table[triplets]
   print(codon)
