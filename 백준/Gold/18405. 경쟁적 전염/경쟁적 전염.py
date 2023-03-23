import sys
from collections import deque
input = sys.stdin.readline

n, k = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(n)]
vi = []
for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            vi.append((graph[i][j], i, j))
s, x, y = map(int, input().split())
# print(graph)
# print(vi)
# visited = [[0] * n for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(s, x, y):
    q = deque(vi)
    time = 0
    while q:
        if time == s:
            break
        for _ in range(len(q)):
            p, a, b = q.popleft()
            for i in range(4):
                nx = a + dx[i]
                ny = b + dy[i]
                if 0 <= nx < n and 0 <= ny < n:
                    if graph[nx][ny] == 0:
                        graph[nx][ny] = graph[a][b]
                        q.append((graph[nx][ny], nx, ny))
        time += 1
    return graph[x - 1][y - 1]


vi.sort()
print(bfs(s, x, y))

