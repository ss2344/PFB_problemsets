#!/usr/bin/env python3
fav_dict={'book' :'Jitterbug Perfume','song':'Tom Petty', 'tree':'cedar'}
print(fav_dict['book'])
fav_thing='book'
print(fav_dict[fav_thing])
fav_tree='tree'
print(fav_dict[fav_tree])
fav_dict.update({'organism': 'dog'})
print(fav_dict)
for key in fav_dict:
  print(key,':',  fav_dict[key])
value=fav_dict.get('tree')
print(value)

'''key=input(fav_dict[key])
print(key)

print(fav_dict[key])'''

for key in fav_dict:
  print(key)
fav_dict['organism']='cat'
print(fav_dict)
fav_thing= input()
print(fav_dict[fav_thing])
print('my fav things')
x=input()
print(fav_g(x))
