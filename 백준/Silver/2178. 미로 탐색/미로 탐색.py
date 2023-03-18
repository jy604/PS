# 미로 탐색
# bfs
import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
graph = []
for i in range(n):
    graph.append(list(map(int, input().rstrip())))

# 방향 표시 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        # 4 방향으로 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # 미로에 벗어난 경우 처리하는 부분
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            #벽인 부분
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1: # 방문했을 경우
                graph[nx][ny] = graph[x][y] + 1
                q.append((nx, ny))
    return graph[n - 1][m - 1]


print(bfs(0,0))