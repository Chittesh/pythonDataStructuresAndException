#print(10/0)            #ZeroDivisionError: division by zero
#print(10 + '10')       #TypeError: unsupported operand type(s) for +: 'int' and 'str'
#print(value)            #NameError: name 'value' is not defined
value=[]
#print(value.method())   #AttributeError: 'list' object has no attribute 'method'

#import builtins
#help(builtins)

try:
    i=0
    number = 10/i
except (ZeroDivisionError,TypeError) as error:
    print(error)
    number = 0;
else:               # else block is executed when exception is not thrown
    print("else")
finally:
    print("Finally block")

print(number)

