import random

def f(A, n):
    if (n == 0):
        return 0
    else:
        return f(A, n-1) + A[n-1]


A = [random.randint(1, 100) for _ in range(10)]
print(A)

Wert = f(A, len(A))
print ("Endergebnis:", Wert)
print ("Arraysumme:", sum(A))

print ("--- Ende ---")