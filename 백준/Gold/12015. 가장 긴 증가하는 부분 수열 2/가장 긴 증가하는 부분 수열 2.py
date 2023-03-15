import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
dp = [0] # 길이

for res in a:
    if dp[-1] < res:
        dp.append(res)
    else:
        start = 0
        end = len(dp)

        while start < end:
            mid = (start + end) // 2
            if dp[mid] < res:
                start = mid + 1
            else:
                end = mid
        dp[end] = res
print(len(dp) - 1)