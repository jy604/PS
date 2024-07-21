# 1389 케빈 베이컨의 6단계 법칙
from collections import deque
n, m = map(int, input().split())
g = [[] for _ in range(n + 1)]
for i in range(m):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

def bfs(start):
    q = deque()
    q.append(start)
    # 각 노드별 최소경로이기때문에 방문할때마다 초기화해야함
    visited = [0] * (n + 1)
    visited[start] = 1

    while q:
        start = q.popleft()

        for i in g[start]:
            if not visited[i]:
                visited[i] = visited[start] + 1
                q.append(i)
    result = sum(visited[1:])
    return result

res = []
for i in range(1, n + 1):
    res.append(bfs(i))
    # print(res)
print(res.index(min(res)) + 1)