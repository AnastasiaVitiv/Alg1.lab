import math

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


if __name__ == '__main__':
    run_task_2(3, 4, 0.1)