# 행렬 곱셈 순서
import sys
input = sys.stdin.readline
n = int(input())
nums = []
for _ in range(n):
    nums.append(list(map(int, input().split())))
dp = [[0 for _ in range(n)] for _ in range(n)]

for i in range(1, n):
    for j in range(0, n - i): # 대각선으로 기록하기 위해서 n - i를 함
        if i == 1: # 차이가 1밖에 나지 않는 칸
            dp[j][j + i] = nums[j][0] * nums[j][1] * nums[j+i][1]
            continue
        dp[j][j+i] = 2 **32 #최댓값
        for k in range(j, j + i):
            dp[j][j + i] = min(dp[j][j + i],
                               dp[j][k] + dp[k + 1][j + i] + nums[j][0] * nums[k][1] * nums[j + i][1])

print(dp[0][n - 1]) # 제일 위 오른쪽