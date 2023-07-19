
n = int(input()) # 색종이 수
paper = []

for _ in range(n):
    width = list(map(int, input().split()))
    paper.append(sorted(width))

paper.sort()

dp = [1 for _ in range(n)] # 가장 긴 증가하는 부분 수열

for i in range(n):
    for j in range(i):
        if paper[i][1] >= paper[j][1]:
            dp[i] = max(dp[i], dp[j] + 1)
            
print(max(dp))