import sympy as sp
from sympy import *
import matplotlib.pyplot as plt

# James Miller
# 20630524

# Student ID Variables
a = 4
b = 2
c = 5
d = a + b + c
###

x, y = sp.symbols('x, y')  # Define the symbols needed in ths project.

# Part One

# 1B)
p1bLeft = sp.limit((a + 1) * x * sp.exp(-x) * sp.sin((b + 1) / x), x, '-')
p1bRight = sp.limit((a + 1) * x * sp.exp(-x) * sp.sin((b + 1) / x), x, '+')
p1bTwo = sp.limit((a + 1) * x * sp.exp(-x) * sp.sin((b + 1) / x), x, 0)

print(f"{p1bLeft}, {p1bRight}, {p1bTwo}")
