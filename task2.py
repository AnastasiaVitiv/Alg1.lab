import math

d = 0.001
term = 0.0
h = 0.1
a = 3
b = 4

print(f"{'x':^10} {'term':^15}")


x = a
while x <= b:
    mysum = 0
    k = 1
    term = (1 / k) * (math.tan(x / (2 ** k)))

    while abs(term) > d:
        mysum += term

        term = abs((1 / k) * (math.tan(x / (2 ** k))))
        k += 1

    print(f"{x} {mysum}")
    x = x + h
    x = round(x, 4)
