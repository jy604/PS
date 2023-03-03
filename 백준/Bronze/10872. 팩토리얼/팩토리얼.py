import sys
n = int(sys.stdin.readline())

def fac(n):
    ans = 1
    for i in range(1, n+1):
        ans *= i
    return ans
print(fac(n))