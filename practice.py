class Dog:
    def sound(self):
        print("Brak")

class Cat:
    def sound(self):
        print("meow")


class Animal(Cat,Dog):
    pass

a1=Animal()
a1.sound()