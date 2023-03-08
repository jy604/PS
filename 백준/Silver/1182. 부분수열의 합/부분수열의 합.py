def dfs(start):
    global cnt
    if sum(ans) == s and len(ans) > 0:
        cnt += 1

    for i in range(start, n):
        ans.append(num[i])
        dfs(i + 1)
        ans.pop()


n, s = map(int, input().split())
num = list(map(int, input().split()))
cnt = 0
ans = []
dfs(0)
print(cnt)