import math


# 1 - Create a class Book with __init__(self, title, author, price). Add a method discounted_price(self, percent) that returns the price after applying a percentage discount. Create one Book instance and print its discounted price at 20%.


class Books:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def discounted_price(self, percent):
        return self.price - self.price * percent / 100


my_book = Books("jogidas khuman", "Jhaverchand Meghani", 200)
print(my_book.discounted_price(20))


# 2 - Create a class BankAccount with a private-by-convention _balance attribute, a deposit(self, amount) method, and a withdraw(self, amount) method that refuses to let the balance go negative (print an error message instead). Test both deposit and an over-withdrawal.

class BankAccount:
    def __init__(self, balance):
        self.__balance = balance

    def get_balance(self):
        return self.__balance

    def deposit(self, amount):
        self.__balance += amount
        print(self.__balance)

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Error: insufficient balance")
        else:
            self.__balance -= amount
            print(self.__balance)


b1 = BankAccount(1000)
b1.deposit(500)
b1.withdraw(1300)


# 3 - Create a parent class Vehicle with __init__(self, brand) and a method info(self) that prints the brand. Create a child class Car(Vehicle) that adds a seats attribute and overrides info(self) to also print the seat count, calling the parent's info() using super()


class Vehicle:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        print(self.brand)


class Car(Vehicle):
    def __init__(self, brand, seats):
        super().__init__(brand)
        self.seats = seats

    def info(self):
        print(f"{self.brand} and {self.seats}")


tata = Car("Tata", 7)
tata.info()


# 4 - Add __str__ and __eq__ to a class Point(x, y) so that print(point) shows a readable format and two points with the same x/y compare as equal with ==

class Points:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"point({self.x}, {self.y})"

    def __eq__(self, a) -> bool:
        return self.x == a.x and self.y == a.y



p = Points(3, 4)
p1 = Points(3, 4)
print(p,p1)
print(p == p1)


# 5 - Add a @staticmethod to a class MathHelper called is_prime(n) that checks whether a number is prime. Test it with a few numbers including 2, 1, and 17.

class MathHelper:

    @staticmethod
    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(math.isqrt(n)) + 1, 2):
            if n % i == 0:
                return False
        return True


print(MathHelper.is_prime(2))
print(MathHelper.is_prime(17))
print(MathHelper.is_prime(1))
