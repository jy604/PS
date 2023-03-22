import sys
from collections import deque
input = sys.stdin.readline


def bfs(x, y):
    q = deque()
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    if graph[y][x] == 1:
        q.append((x, y))
        visited[y][x] = 1
        cnt = 1
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < m and 0 <= ny < n:
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    q.append((nx, ny))
                    cnt += 1
    return cnt


T = int(input())
for _ in range(T):
    # 배추 밭 가로, 세로, 배추 수
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    visited = [[0] * m for _ in range(n)]
    res = []

    # 배추 심어야함!
    for j in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1 and visited[j][i] == 0:
                res.append(bfs(i, j))

    print(len(res))