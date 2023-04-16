import math

"""
lg n
√
n
n
n lg n
n2
n3
2n
n!
"""

def f2(num):
    return "{:.2f}".format(num)

n = 100

print ("\n\n")

print("n        :",  n)
print("2n       :",  2*n)
print("Log n    :", f2(math.log(n, 10)))
print("n*Log n  :", f2(n * math.log(n, 10)))
print("Wurzel n :", f2(math.sqrt(n)))
print("n^2      :", pow(n, 2))
print("n^3      :", pow(n, 3))
print("n!       :",  "{:.2e}".format(math.factorial(n)))

print ("\n\n")

