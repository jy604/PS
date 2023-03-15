import sys
n, k = map(int, sys.stdin.readline().split())
level = []
for _ in range(n):
    level.append(int(sys.stdin.readline()))

level.sort()
start = level[0]
end = level[-1] + k
result = 0
while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in level:
        if x <= mid:
            total += (mid - x)
    if total <= k:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)