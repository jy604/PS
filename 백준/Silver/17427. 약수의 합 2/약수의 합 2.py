
# n이 5일때, 1~5까지 1은 5개 2는 2개 3,4,4 회원님들
n = int(input())
s = 0
for i in range(1, n + 1):
    s += (n // i) * i
print(s)