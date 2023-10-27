#!/usr/bin/env python3
#1-4
import Bio.Seq
import re
import textwrap
import json
from Bio import SeqIO
from Bio.Seq import Seq
def gc_content(seq):
  G_count=seq.count('G')
  C_count=seq.count('C')
  gc_content=(G_count+C_count)
  return gc_content
nt_count_list=[]
total_seq=0
gc_content_list=[]
for seq_record in SeqIO.parse("/Users/pfb14/Downloads/Python_08.fasta","fasta"):
  print('ID', seq_record.id)
  print('Description',seq_record.description)
  print('Sequence', seq_record.seq)
  nt_count=len(seq_record.seq)
  nt_count_list.append(nt_count)
  seq_count=re.findall(r">",seq_record.id)      
  total_seq+=1
  total_nts=sum(nt_count_list)
  avg_len_seq=total_nts/total_seq
  shortest_seq_len=min(nt_count_list)
  longest_seq_len=max(nt_count_list)
  gc_content_seq=(gc_content(seq_record.seq))
  gc_content_list.append(gc_content_seq)
  avg_gc_content=sum(gc_content_list)/total_seq
  lowest_gc_content=min(gc_content_list)
  highest_gc_content=max(gc_content_list)
print(f"gc_content_list:{gc_content_list}")
print(f"average_gc_content:{avg_gc_content}")
print(f"lowest gc content is: {lowest_gc_content},highest gc content is:{highest_gc_content}")
print(f"shortest sequence length in the file:{shortest_seq_len}")
print(f"longest sequence length in the file:{longest_seq_len}")
print(f"average length of sequences:{avg_len_seq:.2}")
print(f"average length of sequences:{avg_len_seq}")
print(f"total no of nucleotides in the file:{total_nts}")
print(f"total number of sequence:{total_seq}")
print(nt_count_list)
print(f"counting bases in sequences{nt_count}")
gc_content_seq=(gc_content(seq_record.seq))
print(gc_content_seq)
#Parsing blast output
id_list=[]
desc_list=[]
total_SP=0
for seq_record_uniport in SeqIO.parse("/Users/pfb14/problemsets/biopython/uniprot_sprot.fasta","fasta"):
 # print('ID_uniport', seq_record_uniport.id)
  #print('Description',seq_record_uniport.description)
  id_list.append(seq_record_uniport.id)
  desc_list.append(seq_record_uniport.description)
  if re.search(r"OS=Salmonella", seq_record_uniport.description):
    total_SP+=1
#print(f"total no of SP:{total_SP}")
#print(id_list)
#print(desc_list)
#print(len(id_list))
#print(len(desc_list))
  with open("s_paratyphi.prot.txt","w") as file_write:
    if (re.search(r"OS=Salmonella paratyphi B", seq_record_uniport.description)):      
      SP_B={}
      SP_B_ID=(seq_record_uniport.id)
      SP_B_desc=(seq_record_uniport.description)
      SP_B_seq=(seq_record_uniport.seq)
      SP_B[SP_B_ID]={}
      SP_B[SP_B_ID][SP_B_desc]=SP_B_seq
      #print(SP_B)
      file_write.write(json.dumps(SP_B))
      print(file_write)
      #print(SP_B_ID)  
       #file_write.write(seq_record_uniport.id)
       #file_write.write(seq_record_uniport.description)
       #file_write.write(seq_record_uniport.seq)
       
