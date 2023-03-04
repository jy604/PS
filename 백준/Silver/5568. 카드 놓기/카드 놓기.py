import itertools
n = int(input())
k = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
result = set()
for i in list(itertools.permutations(arr, k)):
    result.add(''.join(list(map(str,i))))

print(len(result))