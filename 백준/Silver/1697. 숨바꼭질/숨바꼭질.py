# 숨바꼭질
# 수빈, 동생 위치
from collections import deque


def bfs(x):
    q = deque([x])

    while q:
        x = q.popleft()
        if x == k:
            return dist[x]
        for nx in (x - 1, x + 1, 2 * x):
            if 0 <= nx <= max and not dist[nx]:
                dist[nx] = dist[x] + 1
                q.append(nx)


n, k = map(int, input().split())
max = 100001
dist = [0] * (max + 1)

print(bfs(n))