"""
def sigma_x(x):
    #infinity = float('inf')
    total = 0.0
    for k in range(1, 1024):
        total += (1 / float(k)) * (math.tan(x / (2 ** float(k))))
    return total

def run_task_2(a, b, h):
    x = a
    print("\nТаблиця значень для sigma_x(x):")
    print(f"{'x':^10} {'sigma_x(x)':^15}")
    while x <= b:
        print(f"{x:^10.2f} {sigma_x(x) :^15.5f}")
        x += h



"""
import math

x = float(input("Введіть значення x: "))
d = 0.001
total = 0.0
k = 1.0
h = 0.1

if 3 <= x <= 4:
    print("Значення підходить")
    print(f"{'k':^10} {'term':^15} {'total':^15}")

    while True:
        term = abs((1 / float(k)) * (math.tan(x / (2 ** float(k)))))
        if term <= d:
            break
        total += term
        print(f"{k:^10} {term:^15.5f} {total:^15.5f}")
        k += h

    print(f"\nФінальна сума: {total:.5f}")
else:
    print("Значення x має бути в межах [3, 4].")
