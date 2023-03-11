import sys
n = int(sys.stdin.readline())
tower = list(map(int, sys.stdin.readline().split()))
result = [0] * n
stk = []
for i in range(n):
    t = tower[i] # for문 돌아갈때 현재 탑
    while stk:
        if t <= stk[-1][1]:
            result[i] = stk[-1][0] + 1
            stk.append([i, t])
            break
        else:
            stk.pop()
    if not stk:
        stk.append([i, t])

print(*result)