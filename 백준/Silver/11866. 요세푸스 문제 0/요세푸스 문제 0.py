from collections import deque
n, k = map(int, input().split())
p = deque(range(1, n+1))
res = []
for i in range(n):
    while p:
        p.rotate(-(k-1))
        res.append(p.popleft())

        #for _ in range(k-1):
        #     p.append(p.popleft())
        # res.append(p.popleft())
# print(*res)
print(str(res).replace('[', '<').replace(']', '>'))