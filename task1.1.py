import math

a = 4
b = 4.4
h = 0.2


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

if __name__ == '__main__':
    run_task_11(4, 4.4, 0.2)

