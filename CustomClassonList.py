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
print(countriesList)            #[('India', '2000', '100'), ('China', '1000', '200'), ('USA', '500', '400')]
print(countriesList[0])         #('India', '2000', '100')
print(countriesList[0:1])       #[('India', '2000', '100')]
countriesList.append(Countries('Russia','500','600'))
print(countriesList)            #[('India', '2000', '100'), ('China', '1000', '200'), ('USA', '500', '400'), ('Russia', '500', '600')]






