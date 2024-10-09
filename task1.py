x = float(input("Введіть значення х "))
import math

a = 4
b = 6
h = 0.2
mn = 4.5
mx = 5

while x <= b:
    if a <= x < mn:
        y = 1 / math.sin(x ** 2)
    elif mn <= x < mx:
        y = x + math.log(math.sqrt(x ** 7))
    elif mx <= x <= b:
        y = math.log10((math.e ** x) + 4)
    else:
        print("Не входить в область значень")
    x += h
print(y)
