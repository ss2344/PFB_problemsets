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
#print(seq_dict)        
nts_in_seqdict={}
for key in seq_dict:
  nts_in_seqdict[key]={}
  nts_in_seqdict[key]['A']=seq_dict[key].count('A')
  nts_in_seqdict[key]['T']=seq_dict[key].count('T')
  nts_in_seqdict[key]['G']=seq_dict[key].count('G')
  nts_in_seqdict[key]['C']=seq_dict[key].count('C')
#print(nts_in_seqdict)

#2

with open ("Python_08.fasta", "r") as file_obj:
  for sequence in seq_dict:
    codon = re.findall(r"(.{3})",seq_dict[sequence])
   # print(codon)
#3
seq_dict_2={}
with open ("Python_08.fasta", "r") as file_obj:
  for sequence in seq_dict:
    sub_seq_2=seq_dict[sequence][1:]
    seq_dict_2[sequence]=sub_seq_2
   # print(seq_dict_2)
  for sequence in seq_dict_2:
    codon_2=re.findall(r"(.{3})",seq_dict_2[sequence])
    #print(codon_2)
seq_dict_3={}
with open ("Python_08.fasta", "r") as file_obj:
  for sequence in seq_dict:
    sub_seq_3=seq_dict[sequence][2:]
    seq_dict_3[sequence]=sub_seq_3
    #print(seq_dict_3)
for sequence_1 in seq_dict:
    codon_3=re.findall(r"(.{3})",seq_dict_3[sequence])
    #print(codon_3)
#4
seq_dict_rev_1={}
for sequence_1 in seq_dict:
  sequence_comp_1=seq_dict[sequence_1].replace('A','t'). replace('T', 'a').replace('C','g').replace('G','c')
  sequence_revcomp_1=sequence_comp_1[::-1]
  sequence_revcomp_upper_1= sequence_revcomp_1.upper() 
  seq_dict_rev_1[sequence_1]=sequence_revcomp_upper_1
  #print(seq_dict_rev_1)
  
seq_dict_rev_2={}
for sequence_2 in seq_dict_2:
  sequence_comp_2=seq_dict_2[sequence_2].replace('A','t'). replace('T', 'a').replace('C','g').replace('G','c')
  sequence_revcomp_2=sequence_comp_2[::-1] 
  sequence_revcomp_upper_2= sequence_revcomp_2.upper()
  seq_dict_rev_2[sequence_2]=sequence_revcomp_upper_2
  #print(seq_dict_rev_2)

seq_dict_rev_3={}
for sequence_3 in seq_dict_3:
  sequence_comp_3=seq_dict_3[sequence_3].replace('A','t'). replace('T', 'a').replace('C','g').replace('G','c')
  sequence_revcomp_3=sequence_comp_3[::-1]
  sequence_revcomp_upper_3= sequence_revcomp_3.upper()
  seq_dict_rev_3[sequence_3]=sequence_revcomp_upper_3
  #print(seq_dict_rev_3)
# 4 printing all the frames in one file

with open("Python_08.codons-6frames.nt","w") as file_write:
  for gene_name in seq_dict:
    file_write.write(f"{gene_name}\n{seq_dict[gene_name]}\n")
  print(file_write)

# seq_dict_2[sequence]=sub_seq




#pirint(seq_dict_2)
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

aa_seq = []
AA_dict={}
with open ("Python_08.codons1frames.nt", "w") as file_write:
  for triplet in translation_table:   
    AA=translation_table[triplet]
    aa_seq.append(AA)
  for triplet in codon:
    if triplet in translation_table:     
     AA_dict[triplet]=aa_seq
     print(AA_dict[triplet]) 
   # for gene_name in seq_dict:
   #     seq_dict[gene_name]=aa_seq
   # print(seq_dict[gene_name])
# ''' file_write.write(f"{gene_name}\n{aa_seq_join}\n")
 # print(file_write)'''
#''' for gene_name (in seq_dict:
 #     seq_dict[gene_name]=codon   
  #    file_write.write(f"{gene_name}\n{codon}\n" )
#print(file_write)'''

#for sequence in seq_dict:

 # sequence_dict_2[sequence_2]=

# print(sequence_2)
#sequence_dict_2[uience_frame_2]= 
