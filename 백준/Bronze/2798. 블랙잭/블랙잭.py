import itertools
n, m = map(int, input().split())

arr = list(map(int, input().split()))
res = itertools.combinations(arr, 3)
result = 0
for i in res:
    if (m+1 > sum(i)):
        result = max(result, sum(i))
print(result)