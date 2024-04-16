def rotate_matrix(matrix, direction):
    n = len(matrix)
    operations = []

    if direction == "L":
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                operations.extend([
                    [[i, j], [j, n - i - 1]],
                    [(j, n - i - 1), (n - i - 1, n - j - 1)],
                    [(n - i - 1, n - j - 1), (n - j - 1, i)]
                ])
    elif direction == "R":
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                operations.extend([
                    [[i, j], [n - j - 1, i]],
                    [(j, n - i - 1), (n - i - 1, n - j - 1)],
                    [(n - i - 1, n - j - 1), (n - j - 1, i)]
                ])
    return operations


n, direction = input().split()
matrix = [list(map(int, input().split())) for _ in range(int(n))]

operations = rotate_matrix(matrix, direction)

print(len(operations))
for operation in operations:
    item1, item2 = operation
    print(*item1, *item2)
