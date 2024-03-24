class A:
    def __init__(self):
        pass
    def mymethod(self):
        print("This is method of class A")

class B(A):
    def __init__(self):
        pass
    def mymethod(self):
        print("This is method of class B")

class C(A):
    def __init__(self):
        pass
    def mymethod(self):
        print("This is method of class C")


class D(B, C):
    def __init__(self):
        pass
    

d = D()
d.mymethod()
