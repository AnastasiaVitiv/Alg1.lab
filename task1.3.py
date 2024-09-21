import math

a = 4
b = 6
h = 0.2
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

if __name__ == '__main__':
    run_task_12(4, 6, 0.2)
