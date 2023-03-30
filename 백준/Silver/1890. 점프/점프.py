import sys
input = sys.stdin.readline
n = int(input())
map = [list(map(int, input().split())) for i in range(n)]
dp = [[0] * n for i in range(n)] # visited
dp[0][0] = 1

for x in range(n):
    for y in range(n):
        if x == n - 1 and y == n - 1:
            break
        dx = x + map[x][y]
        dy = y + map[x][y]

        if dx < n:
            dp[dx][y] += dp[x][y]
        if dy < n:
            dp[x][dy] += dp[x][y]

print(dp[n - 1][n - 1])