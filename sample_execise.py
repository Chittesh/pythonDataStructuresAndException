
print([n*n for n in range(1,11)])           #[1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print({n*n for n in range(1,11)})           #{64, 1, 4, 36, 100, 9, 16, 49, 81, 25}
print({n:n*n for n in range(1,11)})         #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100}

print(type([]))                             #<class 'list'>
print(type({}))                             #<class 'dict'>
print(type({1}))                            #<class 'set'>
print(type(()))                             #<class 'tuple'>







