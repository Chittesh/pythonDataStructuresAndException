#Stack is typically called LIFO
#Queue is typically called FIFO

#Stack
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
numbers.append(4)
print(numbers)                  #[1, 2, 3, 4]
#we use the pop method to achive this
# this returns the last element and deletes from it
print(numbers.pop())            #4
print(numbers)                  #[1, 2, 3]

#Queue
numbers = []
numbers.append(1)
numbers.append(2)
numbers.append(3)
print(numbers)                  #[1, 2, 3]
# this returns the first element and deletes from it
print(numbers.pop(0))           #1
print(numbers)                  #[2, 3]






