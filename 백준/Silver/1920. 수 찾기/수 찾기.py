import sys


def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2  # arr의 idx
        if target == arr[mid]:
            return 1
        if target > arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    return 0


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))

arr.sort()

for i in range(m):
    print(binary_search(arr, target[i]))