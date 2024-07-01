# 1697
# 숨바꼭질
from collections import deque
n, k = map(int, input().split())
max = 100001
# dx = [-1, 1, *2] int형이어야함
result = [0] * (max + 1)
def bfs(x):
    q = deque([x])

    while q:
        x = q.popleft()
        if x == k:
            return result[x]
        # for i in range(3):
        #     nx = x + dx[i]
        for nx in (x - 1, x + 1, x * 2):
            if 0 <= nx <= max and result[nx] == 0:
                result[nx] = result[x] + 1
                q.append(nx)

print(bfs(n))