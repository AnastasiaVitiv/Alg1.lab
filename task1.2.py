import math

a = 4.5
b = 5
h = 0.2
def get_x_plus_ln_x(x):
    ln_x = math.sqrt(x**7)
    if ln_x == 0:
        return "Ln is undefined for this value"
    x_plus_ln_x = x + math.log(ln_x)
    return x_plus_ln_x

def run_task_12(a, b, h):
    x = a
    print("\nТаблиця значень для ln(x):")
    print(f"{'x':^10} {'ln(x)':^15}")
    while x <= b:
        print(f"{x:^10.2f} {get_x_plus_ln_x(x):^15.5f}")
        x += h


if __name__ == '__main__':
    run_task_12(4.5, 5, 0.2)
