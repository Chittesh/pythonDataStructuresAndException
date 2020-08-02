from operator import attrgetter
class Countries:
    def __init__(self,name,population,area):
        self.name = name
        self.population = population
        self.area = area

    def __repr__(self):
        return repr((self.name, self.population ,self.area))

countriesList = [Countries('India','2000','100'),
                 Countries('China','1000','200'),
                 Countries('USA','500','400')]

#countriesList.sort()        #TypeError: '<' not supported between instances of 'Countries' and 'Countries'
print(countriesList)                            #[('India', '2000', '100'), ('China', '1000', '200'), ('USA', '500', '400')]
countriesList.sort(key=attrgetter('population'))
print(countriesList)                            #[('China', '1000', '200'), ('India', '2000', '100'), ('USA', '500', '400')]
#soritng in reverse order
countriesList.sort(key=attrgetter('population'),reverse=True)
print(countriesList)                             #[('USA', '500', '400'), ('India', '2000', '100'), ('China', '1000', '200')]
print(max(countriesList , key=attrgetter('population')))    #('USA', '500', '400')
print(min(countriesList , key=attrgetter('population')))    #('China', '1000', '200')







