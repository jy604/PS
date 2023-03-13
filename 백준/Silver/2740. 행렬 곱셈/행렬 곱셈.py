N, M = map(int, input().split())
maxtrix1, maxtrix2 = [], [] # nxm 행렬
for _ in range(N):
    maxtrix1.append(list(map(int, input().split())))
M2, K = map(int, input().split())
for _ in range(M2):
    maxtrix2.append(list(map(int, input().split())))

result = [[0 for _ in range(K)] for _ in range(N)]

for n in range(N):
    for k in range(K):
        for m in range(M):
            result[n][k] += maxtrix1[n][m] * maxtrix2[m][k]

for row in result:
    for num in row:
        print(num, end=' ')
    print()