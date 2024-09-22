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
