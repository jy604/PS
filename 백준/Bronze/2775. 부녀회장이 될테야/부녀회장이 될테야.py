# 부녀회장이 될테야
T = int(input())
for _ in range(T):
    k = int(input()) # 몇층
    n = int(input()) # 몇호
    # 0층
    floor_0 = [x for x in range(1, n + 1)]
    for i in range(k):
        for j in range(1, n):
            floor_0[j] += floor_0[j - 1]
    print(floor_0[-1])
    # print(floor_0)