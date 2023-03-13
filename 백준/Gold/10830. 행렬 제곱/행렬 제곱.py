import sys

n, b = map(int, sys.stdin.readline().split())
res = []
for _ in range(n):
    res.append(list(map(int, sys.stdin.readline().split())))


def mult(n, m1, m2):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            for k in range(n):
                result[i][j] += m1[i][k] * m2[k][j]
            result[i][j] %= 1000
    return result


def square(n, b, res):
    if b == 1:  # 제곱이 1일때
        return res
    elif b == 2:  # 거듭제곱 == 행렬 곱셈
        return mult(n, res, res)
    else:
        tmp = square(n, b // 2, res)
        if b % 2 == 0:  # 지수가 짝수
            return mult(n, tmp, tmp)
        else:
            return mult(n, mult(n, tmp, tmp), res)


result = square(n, b, res)

for row in result:
    for num in row:
        print(num % 1000, end=' ')
    print()