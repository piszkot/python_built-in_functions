"""
Detailed explanation of Python's abs() function.
"""


# -----------------------------
# BASIC USAGE
# -----------------------------

# abs() returns the absolute value of a number

print(abs(-42))        # 42
print(abs(-3.14))      # 3.14
print(abs(7))          # 7


# -----------------------------
# CUSTOMIZED abs()
# -----------------------------

# abs(obj) internally calls:
# obj.__abs__()

class Temperature:
    def __init__(self, degrees):
        self.degrees = degrees

    def __abs__(self):
        return Temperature(abs(self.degrees))

    def __repr__(self):
        return f"{self.degrees}°"


t = Temperature(-42)
print(abs(t))          # 42°


# -----------------------------
# COMPLEX NUMBERS
# -----------------------------

# For complex numbers, abs() returns the magnitude:
# abs(a + bj) = √(a² + b²)

print(abs(3 + 4j))     # 5.0      → √(3² + 4²) = √25 = 5
print(abs(1 + 1j))     # 1.4142…  → √2
print(abs(-5 + 0j))    # 5.0      → same as regular abs()
