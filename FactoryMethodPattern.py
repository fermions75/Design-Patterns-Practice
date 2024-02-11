class Mobile:
    def createMobile(self):
        pass

class Iphone(Mobile):
    def createMobile(self):
        return "Iphone"
    
class Pixel(Mobile):
    def createMobile(self):
        return "Pixel"
    
class Redmi(Mobile):
    def createMobile(self):
        return "Redmi"
    
class MobileFactory:
    def createMobile(self, mobileType):
        if mobileType == "Iphone":
            return Iphone()
        elif mobileType == "Pixel":
            return Pixel()
        elif mobileType == "Redmi":
            return Redmi()
        else:
            return None

if __name__ == "__main__":
    mobile_factory = MobileFactory()
    print(mobile_factory.createMobile("Iphone").createMobile())

    print(mobile_factory.createMobile("Pixel").createMobile())

    print(mobile_factory.createMobile("Redmi").createMobile())