class Animal:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return self.name + ' says greet'


class Mammal(Animal):
    def __init__(self, name, legs):
        super().__init__(name)
        self.legs = legs


class Human(Mammal):
    def __init__(self, name, legs=2):
        super().__init__(name, legs)

    def greet(self):
        return self.name + ' says hello'

    def speak(self):
        print('My name is', self.name)


print(__name__)
h = Human('Sam')
print(h.greet())
print(h.legs)
print(type(h))
