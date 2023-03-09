import sys
n = int(sys.stdin.readline())
stk = []
cnt = 1
for i in range(n):
    stk.append(int(sys.stdin.readline()))
k = stk[-1]
for i in range(len(stk)-1, -1, -1):
    if k < stk[i]:
        cnt += 1
        k = stk[i] #앞이 더 크면 뒤가 가리기 때문
print(cnt)