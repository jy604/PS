import sys

n = int(sys.stdin.readline())
quad = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
w = 0
b = 1
result = []


def zip(x, y, n):
    s = []
    for i in range(x, x+n):
        for j in range(y, y+n):
            s.append(quad[i][j]) # 값 넘어옴
    if s == [0 for i in range(n*n)]:
        result.append(0)# s가 0으로 다 채워질때
        # 0으로 출력
    elif s == [1 for i in range(n*n)]: # s가 1로 다 채워질때
        result.append(1)# 1로 출력
    else:
        result.append("(")
        zip(x, y, n//2)
        zip(x, y + n//2, n // 2)
        zip(x + n // 2, y, n //2)
        zip(x + n // 2, y + n // 2, n //2)
        result.append(")")
    return result


zip(0,0,n)

for k in result:
    print(k, end='')