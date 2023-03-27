# 평범한 배낭
# 물품의 수, 최대 무게
n, k = map(int, input().split())
# dp 테이블 초기화
arr = [[0 for _ in range(k + 1)] for _ in range(n + 1)]
thing = [[0, 0]]
for _ in range(n):
    thing.append(list(map(int, input().split())))

for i in range(1, n + 1):
    for j in range(1, k + 1):
        weight = thing[i][0]
        value = thing[i][1]

        if j < weight: # weight보다 작으면 값을 그대로 가져옴
            arr[i][j] = arr[i - 1][j]
        else: # 아니면 더 큰 값을 넣어줌
            arr[i][j] = max(value + arr[i - 1][j - weight], arr[i - 1][j])

print(arr[-1][-1])