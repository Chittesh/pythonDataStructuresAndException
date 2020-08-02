animals = ['Cat', 'Dog', 'Elephant']

print(len(animals))             #3
animals.append('Fish')
print(animals)                  #['Cat', 'Dog', 'Elephant', 'Fish']
animals.remove('Fish')
print(animals)                  #['Cat', 'Dog', 'Elephant']
animals.append('Fish')
print(animals)                  #['Cat', 'Dog', 'Elephant', 'Fish']
# Delete opertion based on index
del animals[2]
print(animals)                  #['Cat', 'Dog', 'Fish']
#Extend key word - Individual inputs are being added
animals.extend("Bat")
print(animals)                  #['Cat', 'Dog', 'Fish', 'B', 'a', 't']
# but when we pass a list to extend it is added as list
animals.extend(["Bat"])
print(animals)                  #['Cat', 'Dog', 'Fish', 'B', 'a', 't', 'Bat']

animals.append(["Mosue","Snake"])
print(animals)                  #['Cat', 'Dog', 'Fish', 'B', 'a', 't', 'Bat', ['Mosue', 'Snake']]
animals.extend(["Mosue","Snake"])
# this is same as animals += animals
print(animals)                  #['Cat', 'Dog', 'Fish', 'B', 'a', 't', 'Bat', ['Mosue', 'Snake'], 'Mosue', 'Snake']




