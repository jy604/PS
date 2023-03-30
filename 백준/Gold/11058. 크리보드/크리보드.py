# 크리보드
n = int(input())
data = [0] * 101

for i in range(1, 7):
    data[i] = i
for i in range(7, n + 1):
    data[i] = max(data[i-3] * 2, data[i -4] * 3, data[i-5]*4)

print(data[n])