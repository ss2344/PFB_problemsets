#!/usr/bin/env python3
import sys
#No 1
taxa='sapiens, erectus, neanderthalensis'
print(taxa)
print(taxa[1])
print(type(taxa))
taxa_split= taxa.split(', ')
print(taxa_split)
species=taxa_split
print(species[1])
print(type(species))
sort_species=sorted(species,key=None,reverse=False)
print(sort_species)
sort_species_length=sorted(species, key=len)
print(sort_species_length)


#No4
number=1
while number >=1 and number <=100:
  print("number:" ,number)
  number+=1
print('Done')

#No 5
number=1
prev_factorial=1
while number<=1000:
  current_factorial= number*prev_factorial
  print("current_factorial of number:", current_factorial)
  prev_factorial=current_factorial
  number+=1
print('Done')

#No 6
numbers= [101,2,15,22,95,33,2,27,72,15,52]
for number in numbers:
 if number % 2 ==0:
   print(number)

# no7 
numbers=[101,2,15,22,95,33,2,27,72,15,52]
for number in numbers:
  print(number)

###
even_nums=[]
odd_nums=[]
numbers=[101,2,15,22,95,33,2,27,72,15,52]
for number in numbers:
  if number%2==0:
    even_nums.append(number)   
  else:
    odd_nums.append(number)
print(even_nums)
print(odd_nums)

sum_even=sum(even_nums)
print('sum of even numbers:', sum_even)
sum_odd= sum(odd_nums)
print('sum of odd numbers:', sum_odd)


# no 8
range(99)
for num in range(99):
  print(num)
for num in range(100):
  print(num+1)
# no9
for num in range(100):
 list_num= list(range(100)) 
print(list_num)

#no10
num_1=int(sys.argv[1])
num_2=int(sys.argv[2])
list_nums=list(range (num_1, num_2+1))
print(list_nums)
#no 11
sequences=['ATGCCCGGCCCGGC','GCGTGCTAGCAATACGATAAACCGG', 'ATATATATCGAT','ATGGGCCC']
for seq in sequences:
  print(seq)
for seq in sequences:
  print(len(seq),seq, sep='\t')  
