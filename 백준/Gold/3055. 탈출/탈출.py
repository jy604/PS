# 고슴도치 탈출
import sys
from collections import deque
input = sys.stdin.readline
r, c = map(int, input().split())

graph = [list(input().strip()) for _ in range(r)]
dist = [[0] * c for _ in range(r)]
q = deque()
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
# 고슴이 먼저 움직임
# 고슴 > 물 > 고슴 > 물

def bfs(a, b):
    while q:
        x, y = q.popleft()
        if graph[a][b] == 'S':
            return dist[a][b]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 조건
            if 0 <= nx < r and 0 <= ny < c:
                if (graph[nx][ny] == '.' or graph[nx][ny] == 'D') and graph[x][y] == 'S':
                    graph[nx][ny] = 'S' # 고슴이 움직이기
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))
                # 고슴이랑 물이 만나는 경우 물이 고슴이 죽임
                elif (graph[nx][ny] == '.' or graph[nx][ny] == 'S') and graph[x][y] == '*':
                    graph[nx][ny] = '*'
                    q.append((nx, ny))
    return "KAKTUS"


for x in range(r):
    for y in range(c):
        if graph[x][y] == 'S':
            q.append((x, y))
        elif graph[x][y] == 'D':
            a, b = x, y

for x in range(r):
    for y in range(c):
        if graph[x][y] == '*':
            q.append((x, y))

print(bfs(a, b))
