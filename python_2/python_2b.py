#!/usr/bin/env python3
import sys
string = sys.argv[1]
count=int(string)
print(type(count))
#count=30
if count<0:
  message= 'is negative'
  print(count, message)
elif count==0:
  message='is zero'
  print(count,message)
elif count>0 and count<50:
  if count<50 and count%2==0:
    message='it is an even number that is smaller than 50'
    print(count,message)
  else:
    print('Odd number')
elif count>50 and count%3==0:
  message='it is larger than 50 and divisible by 3'
  print(count,message)
else:
  print('not matching')
