numbers = [0,1,2,3,4,5,6,7,8,9,10]
# To revese - the original numbers gets reversed
numbers.reverse()
print(numbers)                  #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

numbers = [0,1,2,3,4,5,6,7,8,9,10]
#Iterator - withouot revesrion the numbers but if we want to print the revese order
reversednumbers = reversed(numbers)
for i in reversednumbers:
    print(i,end='')                #10,9,8,7,6,5,4,3,2,1,0,

numbers.reverse()
numbers.sort()
print(numbers)                      #[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numbers.reverse()
print(numbers)                      #[10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

#To get the sotred number but don't modify the numbers
for i in sorted(numbers):
    print(i)                        ##[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

#key filter sorting based on lenght of string
numbers = ['zero','one','two','three','four','five','six','seven','eight','nine','ten']
for i in sorted(numbers,key=len):
    print(i,end=',')        #one,two,six,ten,zero,four,five,nine,three,seven,eight,
print()
#reverse
for i in sorted(numbers,key=len,reverse=True):
    print(i,end=',')        #three,seven,eight,zero,four,five,nine,one,two,six,ten

