#!/usr/bin/env python3
import re
'''import sys'''

with open ("Python_07_nobody.txt", "r") as file_obj:
  for line in file_obj: 
    found= re.search(r"Nobody",line)
    if found:
      start,end=found.span()
      print(start,end)


#2
with open ("Python_07_nobody.txt", "r") as file_obj, open ("Python_07_Michael.txt","w") as file_write:
  for line in file_obj:
    found= re.search(r"Nobody",line)
    found_sub=re.sub(r"Nobody" , "Michael",line)
    file_write.write(f"{found_sub}")

#3

with open("Python_07.fasta", "r") as file_obj:
  for line in file_obj:
    found=re.search(r"^>\S+\s", line)
    if found:   
      print(found)

#4
with open("Python_07.fasta", "r") as file_obj:
  for line in file_obj:
    found=re.search(r"(^>\S+\s)([\w\W]*\n)", line)
    if found:
      print(f"id:{found.group(1)},{found.group(2)}", sep=" ")


#6
with open("Python_07_Apol.fasta","r") as file_obj:
  for line in file_obj:
    found=re.search(r"([AG]AATT[CT])", line)
    if found:
      print(f"Apo1 site found: {found}")

#7
'''
seq1='GAATTCAAGTTCTTGTGCGCACACAAATCCAATAAAAACTATTGTGCACACAGACGCGACTTCGCGGTCTCGCTTGTTCTTGTTGTATTCGTATTTTCATTTCTCGTTCTGTTTCTACTTCAATGTGGTGATAATATAAAAAATAAAGCAATTCAAAAGTGTATGACTTAATTAATGAGCGATTTTTTTTTTGAAATCAAATTTTTGGAACATTTTTTTTAAATTCAAATTTTGGCGAAAATTCAATATCGGTTCTACTATCCATAATATATTCATCAGGAATACATCTTCAAAGCCAAACGGTGACAACAAAATTCAGGCAATTCAGGCAAATACCGAATGACCAGCTTGGTTATCAATTCTAGAATTTGTTTTTTGGTTTTTATTTATCATTGTAAATAAGACAAACATTTGTTCCTAGTAAAGAATGTAACACCAGAAGTCACGTAAAATGGTGTCCCCATTGTTTAAACGGTTGTTGGGACCAATGGAGTTCGTGGTAACAGTACATCTTTCCCCTTGAATTTGCCATTCAAAATTTGCGGTGGAATACCTAACAAATCCAGTGAATT'''

'''seq1=Str('GAATTCAAGTTCTTGTGCGCACACAAATCCAATAAAAACTATTGTGCACACAGACGCGAC
TTCGCGGTCTCGCTTGTTCTTGTTGTATTCGTATTTTCATTTCTCGTTCTGTTTCTACTT
AACAATGTGGTGATAATATAAAAAATAAAGCAATTCAAAAGTGTATGACTTAATTAATGA
GCGATTTTTTTTTTGAAATCAAATTTTTGGAACATTTTTTTTAAATTCAAATTTTGGCGA
AAATTCAATATCGGTTCTACTATCCATAATATAATTCATCAGGAATACATCTTCAAAGGC
AAACGGTGACAACAAAATTCAGGCAATTCAGGCAAATACCGAATGACCAGCTTGGTTATC
AATTCTAGAATTTGTTTTTTGGTTTTTATTTATCATTGTAAATAAGACAAACATTTGTTC
CTAGTAAAGAATGTAACACCAGAAGTCACGTAAAATGGTGTCCCCATTGTTTAAACGGTT
GTTGGGACCAATGGAGTTCGTGGTAACAGTACATCTTTCCCCTTGAATTTGCCATTCAAA
ATTTGCGGTGGAATACCTAACAAATCCAGTGAATTTAAGAATTGCGATGGGTAATTGACA
TGAATTCCAAGGTCAAATGCTAAGAGATAGTTTAATTTATGTTTGAGACAATCAATTCCC
CAATTTTTCTAAGACTTCAATCAATCTCTTAGAATCCGCCTCTGGAGGTGCACTCAGCCG
CACGTCGGGCTCACCAAATATGTTGGGGTTGTCGGTGAACTCGAATAGAAATTATTGTCG
CCTCCATCTTCATGGCCGTGAAATCGGCTCGCTGACGGGCTTCTCGCGCTGGATTTTTTC
ACTATTTTTGAATACATCATTAACGCAATATATATATATATATATTTAT')  
for line in seq1:
  found=re.search(r"([AG]AATT[CT])", line)
  if found:
    found_sub=re.sub(r"[AG]AATT[CT]","(.{5})[AG]^AATT[CT](.{3})",seq1)
    print(f"Apo1 site is here:{found_sub}")'''


#9(Need to check this with TA)
re_dict={}
with open("re_file.txt" , "r") as file_obj:
  for line in file_obj:
    line=line.rstrip()
    found=re.search(r"(^\w+\s[\W?\s?][\w\s]+[\W?\s?])(\D+)", line)
    if found:
       print(f"{found.group(1)}{found.group(2)}", sep="\t")
       re_name=found.group(1)
       re_site=found.group(2)
       re_name,re_site=line.split( )
       re_name.append
       re.site.append
       re_dict[re_name]=re_site
       print(re_dict)
     
# re_name=re_name.append
 #      re_site=re_site.append
  #     re_dict[re_name]=re_site       
   #:w

    #:print(re_dict)'''





