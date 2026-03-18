# =============================================================================
# Python Built-in Functions - Complete Reference with Examples
# =============================================================================
# Python 3.x | All built-in functions as of Python 3.12
# https://docs.python.org/3/library/functions.html
# =============================================================================


# -----------------------------------------------------------------------------
# abs() - Returns the absolute value of a number
# -----------------------------------------------------------------------------
import random
print("\nabs() ------------------------------------------------------------------\n")
print(abs(-42))        # 42
print(abs(-3.14))      # 3.14
print(abs(7))          # 7


# customized abs()
print("\ncustomized abs()")


class Temperature:
    def __init__(self, degrees):
        self.degrees = degrees

    def __abs__(self):
        return Temperature(abs(self.degrees))

    def __repr__(self):
        return f"{self.degrees}°"


t = Temperature(-42)
print(abs(t))

# complex numbers:
print("\ncomplex numbers")
print(abs(3 + 4j))   # 5.0  → √(3² + 4²) = √25 = 5
print(abs(1 + 1j))   # 1.4142...  → √2
print(abs(-5 + 0j))  # 5.0  → default abs() for complex numbers
print("\n------------------------------------------------------------------------")


# -----------------------------------------------------------------------------
# aiter() - Returns an asynchronous iterator (Python 3.10+)
# -----------------------------------------------------------------------------
# Used with async for loops; requires an async iterable object.
# async for item in aiter(async_iterable): ...

# The primary purpose of aiter() is to enable the creation of objects that can be iterated over in a non-blocking manner.
# This allows the program to perform other tasks—such as animating a user interface or handling other users—while waiting for the next item from the aiter stream.


# -----------------------------------------------------------------------------
# all() - Returns True if all elements in an iterable are truthy (or iterable is empty)
# -----------------------------------------------------------------------------
print(all([True, 1, "hello"]))   # True
print(all([True, 0, "hello"]))   # False
print(all([]))                   # True  (vacuously true)


# -----------------------------------------------------------------------------
# anext() - Retrieves the next item from an async iterator (Python 3.10+)
# -----------------------------------------------------------------------------
# Used in async contexts: value = await anext(async_iterator)


# -----------------------------------------------------------------------------
# any() - Returns True if at least one element in the iterable is truthy
# -----------------------------------------------------------------------------
print(any([False, 0, "hello"]))  # True
print(any([False, 0, ""]))       # False
print(any([]))                   # False


# -----------------------------------------------------------------------------
# ascii() - Returns a string with non-ASCII characters escaped
# -----------------------------------------------------------------------------
print(ascii("café"))    # "caf\xe9"
print(ascii("hello"))   # "hello"


# -----------------------------------------------------------------------------
# bin() - Converts an integer to a binary string (prefixed with '0b')
# -----------------------------------------------------------------------------
print(bin(10))     # '0b1010'
print(bin(-5))     # '-0b101'
print(bin(255))    # '0b11111111'


# -----------------------------------------------------------------------------
# bool() - Converts a value to Boolean (True or False)
# -----------------------------------------------------------------------------
print(bool(0))       # False
print(bool(""))      # False
print(bool(42))      # True
print(bool("hi"))    # True
print(bool(None))    # False


# -----------------------------------------------------------------------------
# breakpoint() - Drops into the debugger at the call site (Python 3.7+)
# -----------------------------------------------------------------------------
# breakpoint()  # Opens pdb debugger; useful for interactive debugging


# -----------------------------------------------------------------------------
# bytearray() - Returns a mutable sequence of bytes
# -----------------------------------------------------------------------------
ba = bytearray(5)            # bytearray of 5 zero bytes
ba2 = bytearray(b"hello")    # from bytes literal
ba2[0] = 72                  # mutable: change 'h' to 'H'
print(ba2)                   # bytearray(b'Hello')


# -----------------------------------------------------------------------------
# bytes() - Returns an immutable bytes object
# -----------------------------------------------------------------------------
print(bytes(4))              # b'\x00\x00\x00\x00'
print(bytes("hi", "utf-8"))  # b'hi'
print(bytes([72, 101, 108]))  # b'Hel'


# -----------------------------------------------------------------------------
# callable() - Returns True if the object appears callable (has __call__)
# -----------------------------------------------------------------------------
print(callable(len))         # True  (built-in function)
print(callable(42))          # False (integer)
print(callable(print))       # True


# -----------------------------------------------------------------------------
# chr() - Returns the string representing a character from a Unicode code point
# -----------------------------------------------------------------------------
print(chr(65))    # 'A'
print(chr(8364))  # '€'
print(chr(128512))  # '😀'


# -----------------------------------------------------------------------------
# classmethod() - Transforms a method into a class method (used as decorator)
# -----------------------------------------------------------------------------
class Dog:
    species = "Canis familiaris"

    @classmethod
    def get_species(cls):
        return cls.species


print(Dog.get_species())   # 'Canis familiaris'


# -----------------------------------------------------------------------------
# compile() - Compiles source into a code object that can be executed
# -----------------------------------------------------------------------------
code = compile("x = 2 + 3", "<string>", "exec")
exec(code)
print(x)   # 5


# -----------------------------------------------------------------------------
# complex() - Creates a complex number
# -----------------------------------------------------------------------------
print(complex(2, 3))     # (2+3j)
print(complex("3+4j"))   # (3+4j)
print(complex(5))        # (5+0j)


# -----------------------------------------------------------------------------
# delattr() - Deletes a named attribute from an object
# -----------------------------------------------------------------------------
class Point:
    x = 10
    y = 20


p = Point()
delattr(Point, "y")
# print(p.y)  # AttributeError: y was deleted


# -----------------------------------------------------------------------------
# dict() - Creates a new dictionary
# -----------------------------------------------------------------------------
d1 = dict(a=1, b=2)            # {'a': 1, 'b': 2}
d2 = dict([("x", 10), ("y", 20)])  # from iterable of pairs
d3 = dict({"name": "Alice"})   # from another dict
print(d1, d2, d3)


# -----------------------------------------------------------------------------
# dir() - Returns a list of names in the current scope or object's attributes
# -----------------------------------------------------------------------------
print(dir([]))       # lists all list methods/attributes
print(dir())         # names in current scope


# -----------------------------------------------------------------------------
# divmod() - Returns a tuple (quotient, remainder) of integer division
# -----------------------------------------------------------------------------
print(divmod(17, 5))    # (3, 2)  → 17 = 3*5 + 2
print(divmod(9.5, 2))   # (4.0, 1.5)


# -----------------------------------------------------------------------------
# enumerate() - Adds a counter to an iterable, returns enumerate object
# -----------------------------------------------------------------------------
fruits = ["apple", "banana", "cherry"]
for i, fruit in enumerate(fruits, start=1):
    print(i, fruit)
# 1 apple
# 2 banana
# 3 cherry


# -----------------------------------------------------------------------------
# eval() - Evaluates a string as a Python expression
# -----------------------------------------------------------------------------
result = eval("3 * (4 + 2)")
print(result)   # 18
print(eval("[x**2 for x in range(5)]"))  # [0, 1, 4, 9, 16]


# -----------------------------------------------------------------------------
# exec() - Executes dynamically created Python code (statements)
# -----------------------------------------------------------------------------
exec("for i in range(3): print(i)")
# 0
# 1
# 2


# -----------------------------------------------------------------------------
# filter() - Constructs an iterator from elements for which a function is True
# -----------------------------------------------------------------------------
numbers = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda n: n % 2 == 0, numbers))
print(evens)   # [2, 4, 6]

# None as function filters out falsy values
mixed = [0, 1, "", "hi", None, 42]
print(list(filter(None, mixed)))   # [1, 'hi', 42]


# -----------------------------------------------------------------------------
# float() - Converts a value to a floating-point number
# -----------------------------------------------------------------------------
print(float(7))         # 7.0
print(float("3.14"))    # 3.14
print(float("inf"))     # inf
print(float("-inf"))    # -inf


# -----------------------------------------------------------------------------
# format() - Formats a value according to a format spec
# -----------------------------------------------------------------------------
print(format(3.14159, ".2f"))   # '3.14'
print(format(255, "08b"))       # '11111111' (padded binary)
print(format(1000000, ","))     # '1,000,000'
print(format("hi", ">10"))      # '        hi'


# -----------------------------------------------------------------------------
# frozenset() - Returns an immutable frozenset object
# -----------------------------------------------------------------------------
fs = frozenset([1, 2, 3, 2, 1])
print(fs)          # frozenset({1, 2, 3})
# fs.add(4)        # AttributeError: frozensets are immutable


# -----------------------------------------------------------------------------
# getattr() - Returns the value of a named attribute of an object
# -----------------------------------------------------------------------------
class Car:
    brand = "Toyota"
    speed = 120


car = Car()
print(getattr(car, "brand"))            # 'Toyota'
print(getattr(car, "color", "red"))     # 'red'  (default if not found)


# -----------------------------------------------------------------------------
# globals() - Returns the current global symbol table as a dictionary
# -----------------------------------------------------------------------------
g = globals()
print(type(g))   # <class 'dict'>
# print(g.keys()) # all global variable names


# -----------------------------------------------------------------------------
# hasattr() - Returns True if the object has the named attribute
# -----------------------------------------------------------------------------
class Robot:
    name = "R2D2"


r = Robot()
print(hasattr(r, "name"))     # True
print(hasattr(r, "color"))    # False


# -----------------------------------------------------------------------------
# hash() - Returns the hash value of an object (if hashable)
# -----------------------------------------------------------------------------
print(hash("hello"))   # some integer (platform-dependent)
print(hash(42))        # 42
print(hash((1, 2)))    # hash of a tuple


# -----------------------------------------------------------------------------
# help() - Invokes the built-in help system (interactive or for an object)
# -----------------------------------------------------------------------------
# help(str)    # prints documentation for the str type
# help()       # starts interactive help


# -----------------------------------------------------------------------------
# hex() - Converts an integer to a lowercase hexadecimal string
# -----------------------------------------------------------------------------
print(hex(255))    # '0xff'
print(hex(16))     # '0x10'
print(hex(-42))    # '-0x2a'


# -----------------------------------------------------------------------------
# id() - Returns the unique identity (memory address) of an object
# -----------------------------------------------------------------------------
a = "hello"
b = "hello"
print(id(a))           # some integer
print(id(a) == id(b))  # True (CPython interns short strings)


# -----------------------------------------------------------------------------
# input() - Reads a line from stdin, optionally displaying a prompt
# -----------------------------------------------------------------------------
# name = input("Enter your name: ")   # waits for user input
# print(f"Hello, {name}!")


# -----------------------------------------------------------------------------
# int() - Converts a value to an integer
# -----------------------------------------------------------------------------
print(int(3.99))       # 3  (truncates, doesn't round)
print(int("42"))       # 42
print(int("0xff", 16))  # 255 (hex string with base)
print(int("1010", 2))  # 10  (binary string)


# -----------------------------------------------------------------------------
# isinstance() - Returns True if the object is an instance of the given class(es)
# -----------------------------------------------------------------------------
print(isinstance(42, int))          # True
print(isinstance(3.14, (int, float)))  # True  (tuple of types)
print(isinstance("hi", list))       # False


# -----------------------------------------------------------------------------
# issubclass() - Returns True if a class is a subclass of another
# -----------------------------------------------------------------------------
print(issubclass(bool, int))    # True  (bool inherits from int)
print(issubclass(int, float))   # False
print(issubclass(float, object))  # True (everything inherits from object)


# -----------------------------------------------------------------------------
# iter() - Returns an iterator object for an iterable
# -----------------------------------------------------------------------------
it = iter([10, 20, 30])
print(next(it))   # 10
print(next(it))   # 20

# iter with sentinel: calls callable until sentinel value is returned
# it2 = iter(lambda: random.randint(1, 6), 6)  # rolls until 6 appears


# -----------------------------------------------------------------------------
# len() - Returns the number of items in an object
# -----------------------------------------------------------------------------
print(len("hello"))        # 5
print(len([1, 2, 3]))      # 3
print(len({"a": 1}))       # 1
print(len(range(100)))     # 100


# -----------------------------------------------------------------------------
# list() - Creates a list from an iterable
# -----------------------------------------------------------------------------
print(list("abc"))          # ['a', 'b', 'c']
print(list(range(5)))       # [0, 1, 2, 3, 4]
print(list((1, 2, 3)))      # [1, 2, 3]
print(list({1, 2, 3}))      # [1, 2, 3]  (order may vary)


# -----------------------------------------------------------------------------
# locals() - Returns a dictionary of the current local symbol table
# -----------------------------------------------------------------------------
def demo_locals():
    x = 10
    y = 20
    print(locals())   # {'x': 10, 'y': 20}


demo_locals()


# -----------------------------------------------------------------------------
# map() - Applies a function to every item of an iterable
# -----------------------------------------------------------------------------
nums = [1, 2, 3, 4]
squares = list(map(lambda n: n**2, nums))
print(squares)   # [1, 4, 9, 16]

# map with multiple iterables
sums = list(map(lambda a, b: a + b, [1, 2, 3], [10, 20, 30]))
print(sums)      # [11, 22, 33]


# -----------------------------------------------------------------------------
# max() - Returns the largest item in an iterable or among arguments
# -----------------------------------------------------------------------------
print(max([3, 1, 4, 1, 5, 9]))    # 9
print(max(3, 1, 4, 1, 5, 9))      # 9
print(max("apple", "banana", "cherry"))  # 'cherry' (lexicographic)
words = ["cat", "elephant", "ox"]
print(max(words, key=len))         # 'elephant' (longest word)


# -----------------------------------------------------------------------------
# memoryview() - Returns a memory view object of a bytes-like object
# -----------------------------------------------------------------------------
b = bytearray(b"hello")
mv = memoryview(b)
print(mv[0])         # 104  (ASCII for 'h')
mv[0] = 72           # modify in place: 'h' → 'H'
print(b)             # bytearray(b'Hello')


# -----------------------------------------------------------------------------
# min() - Returns the smallest item in an iterable or among arguments
# -----------------------------------------------------------------------------
print(min([3, 1, 4, 1, 5, 9]))    # 1
print(min(3, 1, 4))               # 1
words = ["cat", "elephant", "ox"]
print(min(words, key=len))         # 'ox' (shortest word)


# -----------------------------------------------------------------------------
# next() - Retrieves the next item from an iterator
# -----------------------------------------------------------------------------
it = iter([100, 200, 300])
print(next(it))          # 100
print(next(it))          # 200
print(next(it, "done"))  # 300
print(next(it, "done"))  # 'done'  (default when exhausted)


# -----------------------------------------------------------------------------
# object() - Returns a new featureless object (base for all classes)
# -----------------------------------------------------------------------------
obj = object()
print(type(obj))          # <class 'object'>
print(isinstance(obj, object))  # True


# -----------------------------------------------------------------------------
# oct() - Converts an integer to an octal string
# -----------------------------------------------------------------------------
print(oct(8))     # '0o10'
print(oct(255))   # '0o377'
print(oct(-64))   # '-0o100'


# -----------------------------------------------------------------------------
# open() - Opens a file and returns a file object
# -----------------------------------------------------------------------------
# Writing to a file
with open("/tmp/example.txt", "w") as f:
    f.write("Hello, file!\n")

# Reading from a file
with open("/tmp/example.txt", "r") as f:
    content = f.read()
    print(content)   # Hello, file!

# Common modes: 'r' read, 'w' write, 'a' append, 'b' binary, 'x' exclusive create


# -----------------------------------------------------------------------------
# ord() - Returns the Unicode code point for a given character
# -----------------------------------------------------------------------------
print(ord("A"))    # 65
print(ord("€"))    # 8364
print(ord("😀"))   # 128512


# -----------------------------------------------------------------------------
# pow() - Returns base to the power of exp; optional mod for modular exponentiation
# -----------------------------------------------------------------------------
print(pow(2, 10))        # 1024
print(pow(2, -1))        # 0.5
print(pow(2, 10, 1000))  # 24  (modular: 1024 % 1000)


# -----------------------------------------------------------------------------
# print() - Prints objects to a text stream (stdout by default)
# -----------------------------------------------------------------------------
print("Hello", "World", sep=", ")    # Hello, World
print("No newline", end=" ")         # No newline <stays on same line>
print("← same line")
print(1, 2, 3, sep=" | ")           # 1 | 2 | 3


# -----------------------------------------------------------------------------
# property() - Returns a property attribute (used as a decorator)
# -----------------------------------------------------------------------------
class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2


c = Circle(5)
print(c.radius)    # 5
print(c.area)      # 78.539...
c.radius = 10
print(c.radius)    # 10


# -----------------------------------------------------------------------------
# range() - Returns an immutable sequence of numbers
# -----------------------------------------------------------------------------
print(list(range(5)))          # [0, 1, 2, 3, 4]
print(list(range(2, 10, 2)))   # [2, 4, 6, 8]
print(list(range(10, 0, -2)))  # [10, 8, 6, 4, 2]


# -----------------------------------------------------------------------------
# repr() - Returns a developer-friendly string representation of an object
# -----------------------------------------------------------------------------
print(repr("hello\nworld"))   # "'hello\\nworld'"  (shows escape sequences)
print(repr([1, 2, 3]))        # '[1, 2, 3]'
print(repr(3.14))             # '3.14'


# -----------------------------------------------------------------------------
# reversed() - Returns a reverse iterator for a sequence
# -----------------------------------------------------------------------------
print(list(reversed([1, 2, 3, 4])))   # [4, 3, 2, 1]
print(list(reversed("hello")))         # ['o', 'l', 'l', 'e', 'h']
for char in reversed("abc"):
    print(char, end="")   # cba


print()  # newline after the above


# -----------------------------------------------------------------------------
# round() - Rounds a number to a given number of decimal places
# -----------------------------------------------------------------------------
print(round(3.14159, 2))   # 3.14
print(round(3.5))          # 4  (rounds to even in Python 3)
print(round(2.5))          # 2  (banker's rounding)
print(round(1234, -2))     # 1200


# -----------------------------------------------------------------------------
# set() - Creates a new set object (unordered, unique elements)
# -----------------------------------------------------------------------------
s = set([1, 2, 2, 3, 3, 3])
print(s)                    # {1, 2, 3}
print(set("mississippi"))   # {'m', 'i', 's', 'p'}
s.add(4)
print(s)                    # {1, 2, 3, 4}


# -----------------------------------------------------------------------------
# setattr() - Sets the value of a named attribute on an object
# -----------------------------------------------------------------------------
class Person:
    pass


person = Person()
setattr(person, "name", "Alice")
setattr(person, "age", 30)
print(person.name)   # Alice
print(person.age)    # 30


# -----------------------------------------------------------------------------
# slice() - Returns a slice object representing the set of indices
# -----------------------------------------------------------------------------
s = slice(1, 8, 2)   # start=1, stop=8, step=2
data = list(range(10))
print(data[s])        # [1, 3, 5, 7]

# Equivalent to: data[1:8:2]
print(data[1:8:2])    # [1, 3, 5, 7]


# -----------------------------------------------------------------------------
# sorted() - Returns a new sorted list from an iterable
# -----------------------------------------------------------------------------
print(sorted([3, 1, 4, 1, 5, 9]))              # [1, 1, 3, 4, 5, 9]
print(sorted([3, 1, 4], reverse=True))          # [4, 3, 1]
words = ["banana", "apple", "cherry", "date"]
# ['date', 'apple', 'banana', 'cherry']
print(sorted(words, key=len))
print(sorted(words, key=lambda w: w[-1]))        # sort by last character


# -----------------------------------------------------------------------------
# staticmethod() - Transforms a method into a static method (decorator)
# -----------------------------------------------------------------------------
class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def is_even(n):
        return n % 2 == 0


print(MathUtils.add(3, 4))      # 7
print(MathUtils.is_even(6))     # True


# -----------------------------------------------------------------------------
# str() - Returns a string version of an object
# -----------------------------------------------------------------------------
print(str(42))          # '42'
print(str(3.14))        # '3.14'
print(str([1, 2, 3]))   # '[1, 2, 3]'
print(str(True))        # 'True'
print(str(b"hi", "utf-8"))  # 'hi'  (decode bytes)


# -----------------------------------------------------------------------------
# sum() - Sums the items of an iterable, optionally starting from a value
# -----------------------------------------------------------------------------
print(sum([1, 2, 3, 4, 5]))        # 15
print(sum(range(101)))             # 5050
print(sum([1.5, 2.5, 3.0]))        # 7.0
print(sum([[1, 2], [3], [4]], []))  # [1, 2, 3, 4]  (flatten lists)


# -----------------------------------------------------------------------------
# super() - Returns a proxy object that delegates method calls to a parent class
# -----------------------------------------------------------------------------
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} makes a sound"


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)   # calls Animal.__init__
        self.breed = breed

    def speak(self):
        parent_sound = super().speak()
        return f"{parent_sound} — Woof!"


d = Dog("Rex", "Labrador")
print(d.speak())   # Rex makes a sound — Woof!


# -----------------------------------------------------------------------------
# tuple() - Creates a tuple from an iterable
# -----------------------------------------------------------------------------
print(tuple([1, 2, 3]))       # (1, 2, 3)
print(tuple("hello"))         # ('h', 'e', 'l', 'l', 'o')
print(tuple(range(4)))        # (0, 1, 2, 3)
print(tuple({1, 2, 3}))       # (1, 2, 3) — set order may vary


# -----------------------------------------------------------------------------
# type() - Returns the type of an object, or creates a new type dynamically
# -----------------------------------------------------------------------------
print(type(42))             # <class 'int'>
print(type("hello"))        # <class 'str'>
print(type([]))             # <class 'list'>
print(type(None))           # <class 'NoneType'>

# Create a new class dynamically: type(name, bases, dict)
MyClass = type("MyClass", (object,), {"greet": lambda self: "Hello!"})
obj = MyClass()
print(obj.greet())          # Hello!


# -----------------------------------------------------------------------------
# vars() - Returns the __dict__ attribute of an object (its writable attributes)
# -----------------------------------------------------------------------------
class Sample:
    def __init__(self):
        self.x = 1
        self.y = 2


s = Sample()
print(vars(s))   # {'x': 1, 'y': 2}
print(vars())    # same as locals() when called without argument


# -----------------------------------------------------------------------------
# zip() - Aggregates elements from multiple iterables into tuples
# -----------------------------------------------------------------------------
names = ["Alice", "Bob", "Charlie"]
ages = [30, 25, 35]
cities = ["Warsaw", "Berlin", "Paris"]

for name, age, city in zip(names, ages, cities):
    print(f"{name}, {age}, {city}")
# Alice, 30, Warsaw
# Bob, 25, Berlin
# Charlie, 35, Paris

# zip stops at the shortest iterable
print(list(zip([1, 2, 3], [10, 20])))   # [(1, 10), (2, 20)]

# Unzip with *
pairs = [(1, "a"), (2, "b"), (3, "c")]
nums, letters = zip(*pairs)
print(nums)     # (1, 2, 3)
print(letters)  # ('a', 'b', 'c')


# -----------------------------------------------------------------------------
# __import__() - Low-level import mechanism (use importlib for programmatic imports)
# -----------------------------------------------------------------------------
math = __import__("math")
print(math.sqrt(16))   # 4.0
# Prefer: import math  or  importlib.import_module("math")
