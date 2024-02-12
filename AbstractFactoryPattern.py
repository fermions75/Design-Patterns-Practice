from abc import ABC, abstractmethod

# abstract factory
class AbstractShapeFactory(ABC):
    @abstractmethod
    def create_circle(self):
        pass

    @abstractmethod
    def create_rectangle(self):
        pass

# concrete shape factory 1
class RedShapeFactory(AbstractShapeFactory):
    def create_circle(self):
        return RedCircle()
    def create_rectangle(self):
        return RedRectangle()

# concrete shape factory 2
class GreenShapefactory(AbstractShapeFactory):
    def create_circle(self):
        return GreenCircle()
    def create_rectangle(self):
        return GreenRectangle()

# concrete shape factory 3
class BlackShapeFactory(AbstractShapeFactory):
    def create_circle(self):
        return BlackCircle()
    def create_rectangle(self):
        return BlackRectangle()

# product Factory Abstract
class AbstractShapeProduct(ABC):
    @abstractmethod
    def draw(self):
        pass

# concrete products
class RedCircle(AbstractShapeProduct):
    def draw(self):
        print("Drawing a red circle")

class RedRectangle(AbstractShapeProduct):
    def draw(self):
        print("Drawing a red rectangle")


# client
def cleint(factory):
    circle = factory.create_circle()
    circle.draw()

if __name__ == "__main__":
    red_factory = RedShapeFactory()
    cleint(red_factory)