import math

def selection_sort_columns(matrix):
    rows = 0
    for _ in matrix:
        rows += 1
    cols = 0
    for _ in matrix[0]:
        cols += 1

    for col in range(cols):
        for i in range(rows):
            min_idx = i
            for j in range(i + 1, rows):
                if matrix[j][col] < matrix[min_idx][col]:
                    min_idx = j
            matrix[i][col], matrix[min_idx][col] = matrix[min_idx][col], matrix[i][col]
    return matrix

def row_sum(row):
    total = 0
    for val in row:
        total += val
    return total

def geometric_mean(sums):
    multiplication = 1
    count = 0
    for s in sums:
        multiplication *= s
        count += 1
    return multiplication ** (1 / count)

def main():
    matrix = [
        [2, 0, 33, -1, -21],
        [78, 7, -4, -3, 11],
        [-2, -7, -1, -9, 0],
        [13, 61, 60, 42, -10],
        [1, 0, 4, 0, 16]
    ]

    sorted_matrix = selection_sort_columns([row[:] for row in matrix])

    sums = [row_sum(row) for row in sorted_matrix]

    geo_mean = geometric_mean(sums)

    print("Відсортована матриця:")
    for row in sorted_matrix:
        print(row)

    print("\nСуми елементів кожного рядка:")
    for s in sums:
        print(s)

    print(f"\nСереднє геометричне значення = {geo_mean}")

if __name__ == "__main__":
    main()
