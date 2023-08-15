# 1- Classes
from abc import ABC, abstractmethod
from collections import namedtuple

# Classes : Blueprint for creating new objects
# Object : Instance of a class

# Class : Human
# Object : John, Mary, Susan, Paul

# 2- Creating Classes
# 3- Constructors
# 4- Class Vs Instance Attributes
# Every first word of class name should start with Capital Letters eg, Customer, User
class Point:
    default_color = "Red"

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


Point.default_color = "Yellow"
point = Point(1, 2)
print(type(point))
print(
    isinstance(point, Point)
)  # Return boolean whether point is an instance of Point Class
print(isinstance(point, int))
print(point.default_color)
print(point.default_color)
point.draw()

another = Point(3, 4)
print(another.default_color)
another.draw()

# 5- Class and Instance Methods
# 6- Magic Methods
# 7- Comparing Objects
# 8- Performing Arithmetics
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @classmethod
    def zero(cls):
        return cls(0, 0)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == self.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __lt__(self, other):
        return self.x < other.x and self.y < other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    def draw(self):
        print(f"Point ({self.x}, {self.y})")


point = Point.zero()
point.draw()
print(str(point))

point = Point(10, 20)
other = Point(1, 2)
print(point == other)
print(point < other)
print(point > other)
result = point + other
print(result.x)
print(result.y)


class Animal:
    def __init__(self, legs, food, shelter):
        self.legs = legs
        self.food = food
        self.shelter = shelter

    def showAnimal(self):
        print("The animal has {} legs: ".format(self.legs))
        print("The animal eats: {}".format(self.food))
        print("The animal lives in: {}".format(self.shelter))


cat = Animal(4, "Mouse", "House")
tiger = Animal(4, "Meat", "Forest")
cat.showAnimal()
tiger.showAnimal()
print(dir(cat))

# 9- Making Custom Containers
# 10- Private Members  =>  __tags (private attribute)
class TagCloud:
    def __init__(self):
        self.tags = {}

    def add(self, tag):
        self.tags[tag.lower()] = self.tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.tags.get(tag.lower(), 0)

    def __setitem__(self, tag, count):
        self.tags[tag.lower()] = count

    def __len__(self):
        return len(self.tags)

    def __iter__(self):
        return iter(self.tags)


cloud = TagCloud()
cloud["Python"] = 1
cloud.add("Python")
cloud.add("Python")
print(cloud.tags)

cloud1 = TagCloud()
print(cloud1.__dict__)


# 11- Properties
class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        if price < 0:
            raise ValueError("Price cannot be negative")
        self.__price = price


#    price = property(get_price, set_price)
product = Product(10)
product.price = 2
print(product.price)

# 12- Inheritance
# 14- Method overriding


class Animal:
    def __init__(self):
        print("Animal constructor")
        self.age = 1

    def eat(self):
        print("eat")


class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal constructor")
        self.weight = 2

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


m = Mammal()
m.eat()
m.walk()
print(m.age)  # AttributeError: 'Mammal' object has no attribute 'age'
print(m.weight)


# 13- Object class
print(isinstance(m, Animal))
print(isinstance(m, object))

# 15- Multi-level Inheritance
class Bird(Animal):
    def fly(self):
        print("fly")


class Chicken(Bird):
    pass


# 16- Multiple Inheritance
class Employee:
    def greet(self):
        print("Employee Greet")


class Person:
    def greet(self):
        print("Person Greet")


class Manager(Person, Employee):  # Python run the method of the first Called's Class
    pass


manager = Manager()
manager.greet()


class Flyer:
    def fly(self):
        pass


class Swimmer:
    def swim(self):
        pass


class FlyingFist(Flyer, Swimmer):
    pass


# 17- Good example of inheritance
# 18- Abstract Base Classes
# we cannot create the instance of Abstract Class


class InvalidOperationError(Exception):
    pass


class Stream(ABC):
    def __init__(self):
        self.opened = False

    def open(self):
        if self.opened:
            raise InvalidOperationError("File is already open")
        self.opened = True

    def close(self):
        if not self.opened:
            raise InvalidOperationError("File is already close")
        self.opened = False

    @abstractmethod  # decorator
    def read(self):
        pass


class FileStream(Stream):
    def read(self):
        print("Reading data from a file.")


class NetworkStream(Stream):
    def read(self):
        print("Reading data from a network.")


class MemoryStream(Stream):
    def read(self):
        print("Reading data from memory stream.")


memory = MemoryStream()
memory.read()

# 19- Polymorphism, Poly=> Many, Morphism -> Forms, ManyForms
# Note: Python is Dynamic Language, You don't need
# 20- Duck Typing
class UIControl(ABC):
    @abstractmethod
    def draw(self):
        pass


# Note: Python is Dynamically Typed Language, You don't need UIControl as a base in TextBox and DropDownList,
# as long as the draw method iterate the object. because we don't specific the type of the control in draw method.
# It can be anyone string, list, tuple, dictionary, array.


class TextBox(UIControl):
    def draw(self):
        print("TextBox")


class DropDownList(UIControl):
    def draw(self):
        print("DropDownList")


# can pass single object or list of object
# controls is purely a label
# We can pass any kind of object to this draw function as long as this object is iterable,
# python will be happy
def draw(controls):
    for control in controls:
        control.draw()


ddl = DropDownList()
tb = TextBox()
print(isinstance(ddl, UIControl))
draw([tb, ddl])

# 21- Extending Built-in Types
class Text(str):
    def duplicate(self):
        return self + self


text = Text("Python")
print(text.duplicate())


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list = TrackableList()
list.append(1)

# 22- Data Classes
# from collections import namedtuple
# If you are working with Classes that have only data and no methods,
# you might want to use a "namedtuple" instead
# namedtuple are immutable.
Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1.x)
# p1.x = 10  # AttributeError: can't set attribute
# print(p1.x)  # Will throw error
# p1 = Point(x=10, y=20) # will get False with this line
print(p1 == p2)
