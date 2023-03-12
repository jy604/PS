import sys
n = int(sys.stdin.readline())
liquid = list(map(int, sys.stdin.readline().split()))
liquid.sort()
start = idx_start = 0
end = idx_end = n - 1
min_data = sys.maxsize
while start < end:
    total  = liquid[start] + liquid[end]

    if abs(total) <= min_data:
        min_data = abs(total)
        idx_start = start
        idx_end = end

    if total > 0:
        end -= 1
    else:
        start += 1
print(liquid[idx_start], liquid[idx_end])