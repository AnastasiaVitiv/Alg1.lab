x = float(input("Введіть значення х"))
import math

def get_lg_x(x):
    x = (math.e ** x) + 4
    if x == 0:
        return "Lg is undefined for this value"
    lg_x = math.log10(x)
    return lg_x

def run_task_12(a, b, h):
    x = a
    print("\nТаблиця значень для lg(x):")
    print(f"{'x':^10} {'lg(x)':^15}")
    while x <= b:
        print(f"{x:^10.2f} {get_lg_x(x):^15.5f}")
        x += h

def get_cosec_sqr_x(x):
    sqr_x = x**2
    sinus_sqr_x = math.sin(sqr_x)
    if sinus_sqr_x == 0:
        return "Cosec is undefined for this angle"
    cosec_sqr_x = 1 / sinus_sqr_x
    return cosec_sqr_x

def run_task_11(a, b, h):
    x = a
    print("\nТаблиця значень для cos(x):")
    print(f"{'x':^10} {'cos(x)':^15}")
    while x <= b:
        print(f"{x:^10.2f} {get_cosec_sqr_x(x):^15.5f}")
        x += h



def get_lg_x(x):
    x = (math.e ** x) + 4
    if x == 0:
        return "Lg is undefined for this value"
    lg_x = math.log10(x)
    return lg_x

def run_task_13(a, b, h):
    x = a
    print("\nТаблиця значень для lg(x):")
    print(f"{'x':^10} {'lg(x)':^15}")
    while x <= b:
        print(f"{x:^10.2f} {get_lg_x(x):^15.5f}")
        x += h

if x < 4.5 and x >= 4:
    run_task_11(4, 6, 0.2)


elif x >= 4.5 and x < 5:
    run_task_12(4, 6, 0.2)

elif x >= 5 and x <= 6:
    run_task_13(4, 6, 0.2)

else:
    print("Не входить в область значень")
