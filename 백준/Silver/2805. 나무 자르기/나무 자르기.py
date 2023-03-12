import sys
N, M = map(int,sys.stdin.readline().split())
trees = list(map(int,sys.stdin.readline().split()))
ans = 0
left, right = 0, max(trees)
trees.sort()
while left <= right:
    total = 0
    mid = (left+right)//2
    for tree in trees:
        if tree > mid:
            total += (tree-mid)
    if total < M:
        right = mid -1
    else:
        ans = mid
        left = mid +1
print(ans)