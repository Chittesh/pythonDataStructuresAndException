occurances = dict(a=5, b=8 , c=9)
print(occurances)                   #{'a': 5, 'b': 8, 'c': 9}

print(occurances.get('a'))          #5
occurances['d'] = 11
print(occurances)                   #{'a': 5, 'b': 8, 'c': 9, 'd': 11}
print(occurances.get('z'))          #None

#if there are no return value we can set a return value by default
print(occurances.get('z',10))       #10
#Keys
print(occurances.keys())            #dict_keys(['a', 'b', 'c', 'd'])
#Values
print(occurances.values())          #dict_values([5, 8, 9, 11])
#items - format of a tuple
print(occurances.items())           #dict_items([('a', 5), ('b', 8), ('c', 9), ('d', 11)])

for (key,value) in occurances.items():
    print(f'{key} {value}')
#a 5
#b 8
#c 9
#d 11

del occurances['a']
print(occurances)                   #{'b': 8, 'c': 9, 'd': 11}






