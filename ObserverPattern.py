class Observer:
    def update(self, msg):
        pass

class User1(Observer):
    def update(self, msg):
        print("User1: ", msg)

class User2(Observer):
    def update(self, msg):
        print("User2: ", msg)

class User3(Observer):
    def update(self, msg):
        print("User3: ", msg)

class Subject:
    def __init__(self):
        self.observers = []
    def add_observer(self, observer):
        self.observers.append(observer)
    def remove_observer(self, observer):
        self.observers.remove(observer)
    def notify_observers(self, msg):
        for observer in self.observers:
            observer.update(msg)

# Client code
if __name__ == "__main__":
    subject = Subject()
    user1 = User1()
    user2 = User2()
    user3 = User3()
    subject.add_observer(user1)
    subject.add_observer(user2)
    subject.add_observer(user3)
    subject.notify_observers("Hello World")
    subject.remove_observer(user2)
    subject.notify_observers("Hello World Again")
    subject.remove_observer(user1)
    subject.notify_observers("Hello World Again and Again")
    subject.add_observer(user1)
    subject.notify_observers("Hello World Again and Again and Again")