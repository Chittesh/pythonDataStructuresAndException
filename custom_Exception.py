class sample:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    def add(self, this):
        if(self.currency == this.currency):
            print("Currencies are equal")
        else:
            #raise Exception ("Currencies are not equal")
            raise customExcpetion("Currencies are not equal")

class customExcpetion(Exception):
    def __init__(self,message):
        super().__init__(message);

object_one = sample("EUR",100)
object_two = sample("EUR",200)
object_three = sample("IND",200)

object_one.add(object_two)              #Currencies are equal
object_one.add(object_three)            #Exception: Currencies are not equal




