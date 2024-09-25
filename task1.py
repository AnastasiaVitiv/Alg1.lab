x = float(input("Введіть значення х "))
import math

a = 4
b = 6
h = 0.2
mn = 4.5
mx = 5
def calculate(x):
    if x < mn and x >= a:
        return 1 / math.sin(x ** 2)

    elif x >= mn and x < mx:
        return x + math.log(math.sqrt(x ** 7))

    elif x >= mx and x <= b:
        return math.log10((math.e ** x) + 4)

    else:
        return "Не входить в область значень"

result = calculate(x)
print(f"Результат: {result}")
