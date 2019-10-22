"""
Hypotenuse exercise
"""
import math

a = input("Input the first leg of the triangle: ")
b = input("Input the second leg of the triangle: ")

a = int(a)
b = int(b)

c2 = a**2 + b**2
c = math.sqrt(c2)

print("c squared is ", c2)
print("c is ", c)

