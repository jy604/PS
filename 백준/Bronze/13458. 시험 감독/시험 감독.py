n = int(input())
nums = list(map(int, input().split()))
b, c = map(int, input().split())

cnt = n
for i in nums:
    i -= b
    if i > 0:
        if i % c:
            cnt += (i // c) + 1
        else:
            cnt += (i // c)

print(cnt)