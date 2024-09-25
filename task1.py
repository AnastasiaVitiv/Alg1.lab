x = float(input("Введіть значення х "))
import math

a = 4
b = 6
h = 0.2
mn = 4.5
mx = 5
"""
def get_lg_x(x):
    x = (math.e ** x) + 4
    return "Lg is undefined" if x <= 0 else math.log10(x)

def get_cosec_x(x):
    sinus_sqr_x = math.sin(x ** 2)
    return "Cosec is undefined" if sinus_sqr_x == 0 else 1 / sinus_sqr_x

def run_task(func, title):
    print(f"\nТаблиця значень для {title}:")
    print(f"{'x':^10} {'value':^15}")
    x = a
    while x <= b:
        print(f"{x:^10.2f} {func(x):^15.5f}")
        x += h

x = a
if a <= x < mn:
    run_task(get_cosec_x, "cosec^2(x)")
elif mn <= x < mx:
    run_task(get_lg_x, "lg(x)")
elif mx <= x <= b:
    run_task(get_lg_x, "lg(x)")
else:
    print("Не входить в область значень")
"""

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