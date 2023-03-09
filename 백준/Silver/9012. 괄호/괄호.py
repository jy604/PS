import sys
T = int(sys.stdin.readline())

for _ in range(T):
    stk = [] #for문 안에 적기
    ans = 0
    stk = sys.stdin.readline()
    for i in stk:
        if i == '(':
            ans += 1
        elif i == ')':
            ans -= 1
        if ans < 0:
            print("NO")
            break
    if ans > 0:
        print("NO")
    elif ans == 0:
        print("YES")