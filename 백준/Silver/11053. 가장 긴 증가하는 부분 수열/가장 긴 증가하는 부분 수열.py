# 가장 긴 증가하는 부분 수열
# 저번 값보다 이번 값이 크면 최댓값 + 1
n = int(input())
a = list(map(int, input().split()))

dp = [1] * n
# dp[0] = 1
for i in range(1, n):
    for j in range(0, i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1) # 횟수 추가

print(max(dp))