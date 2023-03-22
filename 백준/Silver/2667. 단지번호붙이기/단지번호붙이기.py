# 단지번호 붙이기

import sys
from collections import deque
input = sys.stdin.readline


def bfs(g, x, y):
    q = deque()
    q.append((x, y))
    cur_count = 0
    if g[x][y] == '1':
        cur_count = 1
    visited[x][y] = 1
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx in range(n) and ny in range(n):
                if g[nx][ny] == '1' and not visited[nx][ny]:
                    visited[nx][ny] = 1
                # g[nx][ny] = 0 # 다시 방문 못하게 0으로 바꿈
                # g[nx][ny] = g[x][y] + 1
                    cur_count += 1
                    q.append((nx, ny))
    return cur_count


n = int(input())
g = []
for _ in range(n):
    g.append(input().rstrip())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
visited = [[0] * n for _ in range(n)]
result = []
for i in range(n):
    for j in range(n):
        if g[i][j] == '1' and not visited[i][j]:
            result.append(bfs(g, i, j))

result.sort()
print(len(result))
for i in result:
    print(i)
