# 인접 리스트로 구현한 dfs와 bfs
from collections import deque

n, m, v = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for g in graph:
    g.sort()

dfs_visited = [0] * (n + 1)
bfs_visited = [0] * (n + 1)


def dfs(v):
    dfs_visited[v] = True  # 방문 처리
    print(v, end=' ')
    for i in graph[v]:
        if not dfs_visited[i]:
            dfs(i)


def bfs(v):
    bfs_visited[v] = 1
    q = deque([v])
    while q:
        v = q.popleft()
        print(v, end=' ')

        for i in graph[v]:
            if not bfs_visited[i]:
                q.append(i)
                bfs_visited[i] = 1


dfs(v)
print()
bfs(v)
