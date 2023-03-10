import sys


def binary_serach(arr, target): # array, target, left, right
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) //2
        if target == arr[mid]:
            return 1
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return 0


n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
m = int(sys.stdin.readline())
target = list(map(int, sys.stdin.readline().split()))
arr.sort() # 이분 탐색은 항상 정렬된 상태로 시작

for k in range(m):
    print(binary_serach(arr, target[k]))