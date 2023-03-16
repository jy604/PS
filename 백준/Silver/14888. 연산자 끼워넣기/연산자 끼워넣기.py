n = int(input())
a = list(map(int, input().split()))
ops = list(map(int, input().split())) # +, -, *, //

minimum = 1000000001
maximum = -1000000001
ans = 0


def dfs(ans, cnt, add, sub, mul, div):
    global minimum, maximum
    if cnt == n:
        maximum = max(ans, maximum)
        minimum = min(ans, minimum)

    if add > 0:
        dfs(ans + a[cnt], cnt + 1, add -1, sub, mul, div)
    if sub > 0:
        dfs(ans - a[cnt], cnt + 1, add, sub - 1, mul, div)
    if mul > 0:
        dfs(ans * a[cnt], cnt + 1, add, sub, mul - 1, div)
    if div > 0:
        dfs(int(ans / a[cnt]), cnt + 1, add, sub, mul, div - 1)



dfs(a[0], 1, ops[0], ops[1], ops[2], ops[3])
print(maximum)
print(minimum)