import math

d = 0.001
term = 0.00
h = 0.1
a = 3
b = 4

print(f"{'k':^10} {'x':^10} {'term':^15}")

k = 1
x = a
while (term > d or term is 0.00) and x <= b:
    print(f"{k:^10} {x:^10.1f} {term:^15.5f}")
    term += abs((1 / k) * (math.tan(x / (2 ** k))))
    k += 1
    x += h
