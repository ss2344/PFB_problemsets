#!/usr/bin/env python3

''':w
nt_comp={}
dna='GAACTCCAAAAATGAAAACATAGTAGCAATCAAAGCATCCCACTATTTTTTGTCTCTCGTTTCATTAGCGTTGTAAATTACTGATACCCTACTATACCTCTACAAGGCCTTTGTCATCTTTTTACTCAAGTGTGAAATCATCACTTATTGTATGAAGGATGAGCTTTCCGTTCGCTAGTTTGCTGAAAAGGCCTTCTGCAATAAGCTCTCTATTATCTTTAAAAAAACCTGGTTCCTGGTCTTCCATTCTGCTAAAAGCTGTAGGGGTTTTATCACGAGATTCCCGTTGGCATTCTGACTTATTAAAAATGCTTACAGAAGAAATGGATTCTTTAAATGGTCAAATTAATACGTGGACAGATAATAATCCTTTATTAGATGAAATTACGAAGCCATACAGAAAATCTTCAACTCGTTTTTTTCATCCGCTTCTTGTACTTCTAATGTCTAGAGCATCAGTAAATGGGGATCCACCGAGTCAGCAACTATTTCAAAGGTACAAACAACTTGCCCGTGTAACAGAATTGATTCATGCTGCCAATATAATTCATATTAATATTGGAGAAGAACAAAGCAACGAACAGATTAAACTTGCAACGTTGGTTGGAGATTATTTACTCGGAAAGGCGTCTGTTGATTTAGCACATTTAGAAAACAACGCTATTACAGAAATTATGGCTTCTGTTATTGCAAACTTAGTTGAAGGGCACTTCGGAAGCCGACAAAATGGCTCTGTTGGTTTGTCAAACGAACGAACCATCCTTCTGCAATCAGCCTTTATGCCAGCAAAGGCATGTTTATGCGCAAGCATATTGAATAACTCATCACAATACATTAATGATGCGTGTTTCAATTATGGAAAATTTCTAGGCTTATCGCTGCAACTGGCCCATAAGCCTGTATCTCCTGACGCCCAAGTTTTGCAAAAGAATAATGACATTTTGAAAACATATGTTGAGAATGCCAAGAGCTCATTGTCTGTTTTCCCCGATATAGAGGCTAAGCAAGCTCTCATGGAAATCGCTAATAGTGTTTCGAAGTAATCGACAGGTATTGTATCCTGGATTAATATTAGGGTGGCTCATGCATGCTCGTGCAATCGTAACAAATATGTCTTTCTTTTACGAATTTTAACGCTTCAATATAAATCATATTTTTCCTCA'
composition= set(dna)
print ('composition of nt:' ,  composition)
for nt in composition:
 nt_count=dna.count(nt)
 nt_comp[nt]=nt_count
 print(f'{nt} count: { nt_count}')
'''
#5
with open("python_06.txt", "r") as file_read,open("python_06_write.txt", "w") as file_write:
 for line in file_read:
  line = line.rstrip()
  print(line)
  line=line.upper()  
  print(line)
  file_write.write(f"{line}\n")
  print("wrote python_06_write.txt")



#7
Python_06seq_dict={}
with open("Python_06.seq.txt","r") as file_seq_read:
 for line in file_seq_read:
  line=line.rstrip()
  seqName,sequence=line.split('\t')
  Python_06seq_dict[seqName]= sequence
  print(Python_06seq_dict)
for seqName in Python_06seq_dict:
  sequence_comp=Python_06seq_dict[seqName].replace('A','t').replace('T','a').replace('C','g').replace('G','c')
  seq_comp_rev=sequence_comp[::-1]
  sequence_revcomp_upper=seq_comp_rev.upper()
  Python_06seq_dict[seqName]=sequence_revcomp_upper
with open ("Python_06.seq_write.txt", "w") as file_seq_write:
 for seqName in Python_06seq_dict:  
  print('>'+seqName)
  print(Python_06seq_dict[seqName])
  file_seq_write.write(f">{seqName}\n{Python_06seq_dict[seqName]}\n")
#8
count=0
with open ("Python06.fastq","r") as file_fastq_read, open("Python06_wrie.fastq", "w") as file_fastq_write:
 for line in file_fastq_read:
  count+=1
print(count)
count=0
with open ("Python06.fastq","r") as file_fastq_read, open("Python06_wrie.fastq", "w") as file_fastq_write:
 for line in file_fastq_read:
  count=len(line)
  count += 1
print(count)

count_len=[]
with open ("Python06.fastq","r") as file_fastq_read, open("Python06_wrie.fastq", "w") as file_fastq_write:
 for line in file_fastq_read:
  count=len(line)
  count_len.append(count)
print(count_len)
average=sum(count_len)/len(count_len)
print(f"average of the fastq file is:{average}")

#9
new_fasta_file= open ("my_fasta_file","w") 
new_fasta_file.write("seq1 ATGCTGATAG\n")
new_fasta_file.write("seq2 GTACTGACTG\n")
new_fasta_file.write("seq3 ATCGACGTAG\n")
new_fasta_file.write("seq4 GTACGTGCAG\n")
new_fasta_file.close()
print(new_fasta_file)
my_fasta_dict={}
with open("my_fasta_file", "r") as file_read:
 for line in file_read:
  line=line.rstrip()
  seqname,sequence=line.split(' ')
  my_fasta_dict[seqname]=sequence
 print(my_fasta_dict) 

#10
alpaca_all_list=[]
alpaca_stemcellprolif_list=[]
alpaca_pigmentation_list=[]
with open ("alpaca_all_genes.tsv", "r") as all_genes:
 for line in all_genes:
  line=line.rstrip()
  alpaca_all_list.append(line)
 print(alpaca_all_list)
with open ("alpaca_stemcellproliferation_genes.tsv", "r") as all_stemcellprolif:
 for line in all_stemcellprolif:
  line=line.rstrip()
  alpaca_stemcellprolif_list.append(line)
print(alpaca_stemcellprolif_list)
with open("alpaca_pigmentation_genes.tsv", "r") as all_pigmentation:
 for line in all_pigmentation:
  line=line.rstrip()
  alpaca_pigmentation_list.append(line)
print(alpaca_pigmentation_list)
alpaca_all_set=set(alpaca_all_list)
print(alpaca_all_set)
alpaca_stemcellprolif_set= set(alpaca_stemcellprolif_list)
alpaca_pigmentation_set= set(alpaca_pigmentation_list)
print(alpaca_all_set - alpaca_stemcellprolif_set)
print(alpaca_stemcellprolif_set & alpaca_pigmentation_set)
