import sys
m, n, l = map(int, sys.stdin.readline().split())
shoot = list(map(int, sys.stdin.readline().split())) # 사대
shoot.sort()
animals = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

cnt = 0

for a, b in animals:
    start = 0
    end = len(shoot) - 1
    while start < end:
        mid = (start + end) // 2
        if shoot[mid] < a:
            start = mid + 1
        else:
            end = mid
    if abs(shoot[end] - a)+b <= l or abs(shoot[end - 1] -a)+b <= l:
        cnt += 1

print(cnt)