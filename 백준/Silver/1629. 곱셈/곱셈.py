import sys

a, b, c = map(int, sys.stdin.readline().split())


def Recursive(num, z):
    if z == 1:
        return num % c
    if z % 2 == 0: # 짝수
        y = Recursive(num, z//2)
        return (y * y) % c
    else:
        y = Recursive(num, (z-1)//2)
        return (y * y * num) % c


print(Recursive(a, b))
