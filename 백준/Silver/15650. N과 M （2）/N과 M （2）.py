def dfs(bw):
    global result
    if len(result) == m:
        print(' '.join(map(str,result)))
    else:
        for i in range(bw, n+1):
            result.append(i)
            dfs(i+1)
            result.pop()


n, m = map(int, input().split())
result = []
dfs(1)