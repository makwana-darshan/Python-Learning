class Base:
    def sound(self):
        print("Base sound")

class Cat(Base):
    pass

class Dog(Base):
    def sound(self):
        print("Dog sound")

class Animal(Cat, Dog):
    pass

a1 = Animal()
a1.sound()
print(Animal.__mro__)