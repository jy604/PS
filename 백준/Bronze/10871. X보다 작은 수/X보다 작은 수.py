n, x = map(int, input().split())
num = list(map(int, input().split()))

for i in range(len(num)):
    if num[i] < x:
        print(num[i], end=' ')