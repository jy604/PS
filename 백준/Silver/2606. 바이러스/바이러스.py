from collections import deque
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
for i in range(m): # 간선의 수만큼 돌려야함
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n + 1)
cnt = 0


def bfs(v):
    global cnt
    q = deque([v])
    while q:
        x = q.popleft()
        visited[x] = 1
        for i in graph[x]:
            if visited[i] ==0:
                visited[i] = 1
                q.append(i)
                cnt += 1
    print(cnt)

bfs(1)