"""
Detailed explanation of Python's len() function.
"""


# -----------------------------
# BASIC USAGE
# -----------------------------

# len() returns  the length (the number of items) of an object

print(len([1, 2, 3]))          # 3 (list)
print(len("hello"))            # 5 (string)
print(len({"a": 1, "b": 2}))   # 2 (dictionary keys)


# -----------------------------
# UNDER THE HOOD
# -----------------------------

# len(obj) internally calls:
# obj.__len__()

class CustomClass:
    def __len__(self):
        return 42


x = CustomClass()
print(len(x))  # 42


# -----------------------------
# REQUIREMENTS FOR __len__()
# -----------------------------

# __len__() must:
# - return a non-negative integer
# - otherwise Python raises an error

class BadLen:
    def __len__(self):
        return -1  # Invalid

# Uncommenting below will raise ValueError
# print(len(BadLen()))


# -----------------------------
# TIME COMPLEXITY
# -----------------------------

# In most built-in types, len() is O(1)
# because the size is stored internally

# But you can accidentally make it slow:

class SlowLen:
    def __init__(self, data):
        self.data = data

    def __len__(self):
        # Inefficient: counts every time
        return sum(1 for _ in self.data)


slow = SlowLen([1, 2, 3, 4])
print(len(slow))  # Works, but inefficient


# -----------------------------
# OBJECTS WITHOUT LENGTH
# -----------------------------

# Some objects do not support len()

# Uncommenting below will raise TypeError
# print(len(10))  # int has no __len__()


# -----------------------------
# GENERATORS AND ITERATORS
# -----------------------------

gen = (x for x in range(10))

# Uncommenting below will raise TypeError
# print(len(gen))

# To get length, you must convert to list (costly)
print(len(list(gen)))  # 10


# -----------------------------
# TRUTHINESS (BOOLEAN CONTEXT)
# -----------------------------

my_list = [1, 2, 3]

if my_list:
    print("List is not empty")

# Equivalent to:
if len(my_list) != 0:
    print("List is not empty (checked via len)")


# -----------------------------
# SPECIAL CASES
# -----------------------------

# range is efficient (does not store elements)
print(len(range(1_000_000)))  # O(1)


# -----------------------------
# NUMPY BEHAVIOR (if installed)
# -----------------------------

# len() returns size of first dimension, not total elements

try:
    import numpy as np

    arr = np.array([[1, 2], [3, 4]])
    print(len(arr))  # 2 (rows, not total elements)

except ImportError:
    print("NumPy not installed")


# -----------------------------
# COMMON PITFALLS
# -----------------------------

# 1. Generator is not a list
# len(x for x in range(10))  # ❌ TypeError

# 2. Unicode characters
print(len("💩"))  # 1 (character, not bytes)

# 3. Length vs truthy values
print(len([0, False, None]))  # 3


# -----------------------------
# BEST PRACTICES
# -----------------------------

# ✔ Use len() instead of manual counting
# ✔ Avoid calling len() repeatedly in loops if value doesn't change
# ✔ Implement __len__ only when it makes logical sense


# -----------------------------
# SUMMARY
# -----------------------------

# - len() calls __len__()
# - Must return non-negative int
# - Usually O(1)
# - Not supported for all types (e.g., int, generators)
# - Can be customized in user-defined classes
