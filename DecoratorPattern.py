class Coffee:
    description = ""
    cost = 0
    def getCost(self):
        return self.cost
    def getDescription(self):
        return self.description
    

class Espresso(Coffee):
    def __init__(self):
        self.description = "Espresso"
        self.cost = 100
    
    def getCost(self):
        return self.cost
    def getDescription(self):
        return self.description

class Latte(Coffee):
    def __init__(self):
        self.description = "Latte"
        self.cost = 130
    
    def getCost(self):
        return self.cost
    def getDescription(self):
        return self.description

class CoffeeDecorator(Coffee):
    def __init__(self, coffee):
        self.coffee = coffee
    def getCost(self):
        return self.coffee.getCost()
    def getDescription(self):
        return self.coffee.getDescription()

class CreamDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        self.coffee = coffee
    def getCost(self):
        return self.coffee.getCost() + 20
    def getDescription(self):
        return self.coffee.getDescription() + " with Cream"

class SugarDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        self.coffee = coffee
    def getCost(self):
        return self.coffee.getCost() + 10
    def getDescription(self):
        return self.coffee.getDescription() + " with Sugar"

class CreamDecorator(CoffeeDecorator):
    def __init__(self, coffee):
        self.coffee = coffee
    def getCost(self):
        return self.coffee.getCost() + 20
    def getDescription(self):
        return self.coffee.getDescription() + " with Cream"


# client code
if __name__ == "__main__":
    espresso = Espresso()
    espresso_sugar = SugarDecorator(espresso)
    espresso_sugar_cream = CreamDecorator(espresso_sugar)

    print("Cost: ", espresso_sugar_cream.getCost())
    print("Description: ", espresso_sugar_cream.getDescription())