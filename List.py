list = [2,4,8]
print(sum(list))    #14
print(max(list))    #8
print(min(list))    #2
print(len(list))    #3
#append will add value at the end
list.append(74)
print(list)         #[2, 4, 8, 74]
# insert based on the idex
list.insert(3,45)
print(list)         #[2, 4, 8, 45, 74]
#remove
list.remove(45)
print(list)         #[2, 4, 8, 74]
#checking a number is present
print(4 in list)    #True
# to get index of a specific element
print(list.index(4))    #1
print(list.index(100))  #empty value








