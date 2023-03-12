import sys
n, m = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))
ans = 0

tree.sort()

start = 0
end = max(tree)

while start <= end:
    total = 0
    mid = (start + end) // 2
    for x in tree:
        if mid < x:
            total += (x - mid) # 자른 길이의 합
    if total < m: #나무가 모자랄 경우
        end = mid - 1 #왼쪽 탐색을 하기 위해 end를 줄임
    else:
        ans = mid
        start = mid + 1

print(ans)