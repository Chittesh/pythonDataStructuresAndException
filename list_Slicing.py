numbers = [0,1,2,3,4,5,6,7,8,9,10]
# 0 to 5th position
print(numbers[:6])              #[0, 1, 2, 3, 4, 5]
#2nd to 5th postion
print(numbers[2:6])             #[2, 3, 4, 5]
# from postion 3 to last
print(numbers[3:])              #[3, 4, 5, 6, 7, 8, 9, 10]
#from 2nd to 5th postion at interval of 2
print(numbers[2:6:2])           #[2, 4]
#getting only at intevals of 2
print(numbers[::2])             #[0, 2, 4, 6, 8, 10]
#to print from reverse
print(numbers[::-1])            #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#we can deletet the number
del numbers[2:6]
print(numbers)
numbers = [0,1,2,3,4,5,6,7,8,9,10]  #[0, 1, 6, 7, 8, 9, 10]
#we can replace numbers
numbers[2:4] = [88,99]
print(numbers)                  #[0, 1, 88, 99, 4, 5, 6, 7, 8, 9, 10]






