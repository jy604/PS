from collections import deque

n, k = map(int, input().split())
coins = list(set(int(input()) for _ in range(n))) # 동전 종류
visited = [0] * 10001


def bfs(val, cnt):
    q = deque()
    flag = True

    for coin in coins:
        if coin < k:
            q.append([coin, 1])
            visited[coin] = 1

    while q:
        val, cnt = q.popleft()
        if val == k:
            print(cnt)
            flag = False
            break

        for coin in coins:
            if coin + val > k:
                continue
            if visited[val+coin] == 0:
                visited[val+coin] = 1
                q.append([val+coin, cnt+1])
    if flag:
        print(-1)

bfs(0,1)