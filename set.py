numbers = [3,4,5,2,3,5,6,9]
print(numbers)                  #[3, 4, 5, 2, 3, 5, 6, 9]
set_numbers = set(numbers)
print(set_numbers)              #{2, 3, 4, 5, 6, 9}
#adding at 4th index
#set_numbers.add(88,4)          #TypeError: add() takes exactly one argument (2 given)
set_numbers.add(23)
print(set_numbers)              #{2, 3, 4, 5, 6, 9, 23}
#removing
set_numbers.remove(23)
print(set_numbers)              #{2, 3, 4, 5, 6, 9}
#print(set_numbers[2])          #TypeError: 'set' object does not support indexing
print(2 in set_numbers)         #True
print(max(set_numbers))         #9
print(len(set_numbers))         #6

set_one = set(range(1,6))       #{1, 2, 3, 4, 5}
set_two = set(range(4,11))      #{4, 5, 6, 7, 8, 9, 10}
#Union of set
print(set_one | set_two)        #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
#Intersection of set
print(set_one & set_two)        #{4, 5}
#subtraction of set
print(set_one - set_two)        #{1, 2, 3}
print(set_two - set_one)        #{6, 7, 8, 9, 10}







