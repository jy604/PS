# 동전
T = int(input())
for _ in range(T):
    # 동전의 개수
    n = int(input())
    # 동전의 종류
    coins = list(map(int, input().split()))
    m = int(input()) # 목표 금액

    # dp 테이블 초기화
    dp = [0] * (m + 1)
    dp[0] = 1
    for coin in coins:
        for i in range(1, m + 1):
            if i >= coin:
                dp[i] += dp[i - coin]
    print(dp[m])