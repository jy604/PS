import sys
n, k = map(int, sys.stdin.readline().split())
x = []
for _ in range(n):
    x.append(int(sys.stdin.readline()))

x.sort()
start = x[0]
end = x[-1] + k
result = 0
while start <= end:
    mid = (start + end) // 2
    total = 0
    for i in x:
        if mid >= i:
            total += (mid - i)
    if total <= k:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)