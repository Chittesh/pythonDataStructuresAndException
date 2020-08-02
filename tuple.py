def create_name():
    return 'Chittesh','1990','India'

name = create_name()
print(name)                 #('Chittesh', '1990', 'India')
print(type(name))           #<class 'tuple'>

#Destructing a couple
firstName, year, country = name
print(firstName)            #Chittesh
print(year)                 #1990
print(country)              #India

print(name[2])              #India
#values under tuple is immutable
name[1]=1992                #TypeError: 'tuple' object does not support item assignment







