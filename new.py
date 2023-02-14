def minSumPath():
    grid = [[5, 9, 6], [11, 5, 2]]
    m, n = len(grid), len(grid[0])
    dp = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = grid[0][0]
            elif i < m and j < n:
                up = grid[i][j]
                if i > 0:
                    up += grid[i-1][j]
                else:
                    up += 1000
                left = grid[i][j]
                if j > 0:
                    left += grid[i][j-1]
                else:
                    left += 1000

                dp[i][j] = min(up, left)

    print(dp[m-1][n-1])


minSumPath()
