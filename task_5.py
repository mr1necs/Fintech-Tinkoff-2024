def max_mushrooms(n, forest):
    dp = [[0, 0, 0] for _ in range(n)]

    for j in range(3):
        if forest[0][j] == 'C':
            dp[0][j] = 1
        elif forest[0][j] == 'W':
            dp[0][j] = 0

    for i in range(1, n):
        for j in range(3):
            if forest[i][j] == 'W':
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i-1][max(0, j-1)], dp[i-1][j], dp[i-1][min(2, j+1)]) + (forest[i][j] == 'C')

    return max(dp[n-1])


n = int(input())
forest = [input().strip() for _ in range(n)]
forest.reverse()
print(max_mushrooms(n, forest))


"""
def max_mushrooms(n, grid):
    dp = [[0, 0, 0] for _ in range(n)]

    for j in range(3):
        if grid[n-1][j] == 'C':
            dp[0][j] = 1

    for i in range(1, n):
        for j in range(3):
            if grid[n-1-i][j] == 'W':
                dp[i][j] = 0
            else:
                dp[i][j] = max(dp[i-1][max(0, j-1)], dp[i-1][j], dp[i-1][min(2, j+1)]) + (grid[n-1-i][j] == 'C')

    return max(dp[n-1])


n = int(input())
forest_map = [input().strip() for _ in range(n)]
print(max_mushrooms(n, forest_map))
"""