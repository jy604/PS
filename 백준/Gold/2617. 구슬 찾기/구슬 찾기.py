# 구슬 찾기
# 이분 탐색
import sys
input = sys.stdin.readline
# 구슬 개수, 쌍
n, m = map(int, input().split())

# 무거운 리스트, 가벼운 리스트 구분하여 생성
h_list = [[] for _ in range(n + 1)]
l_list = [[] for _ in range(n + 1)]
mid = (n + 1)//2

for _ in range(m):
    x, y = map(int, input().split())
    h_list[y].append(x)
    l_list[x].append(y)


def dfs(graph, v):
    global cnt
    for i in graph[v]:
        if not visited[i]:
            visited[i] = 1
            cnt += 1
            dfs(graph, i)

res = 0

for i in range(1, n + 1):
    visited = [0] * (n + 1)
    cnt = 0
    dfs(h_list, i)
    if cnt >= mid:
        res += 1
    cnt = 0
    dfs(l_list, i)
    if cnt >= mid:
        res += 1

print(res)