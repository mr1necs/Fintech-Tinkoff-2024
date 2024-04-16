def rotate(n, m, matrix):
    rotated_matrix = []
    for j in range(m):
        row = []
        for i in range(n - 1, -1, -1):
            row.append(matrix[i][j])
        rotated_matrix.append(row)

    return rotated_matrix


n, m = map(int, input().split())
matrix = []
for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

rotated = rotate(n, m, matrix)

for row in rotated:
    print(*row)
