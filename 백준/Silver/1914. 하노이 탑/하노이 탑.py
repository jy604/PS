def honoi(n, a, b, c):
    if n == 1:
        print(a, c, sep=' ')
    else:
        honoi(n - 1, a, c, b)
        honoi(1, a, b, c)
        honoi(n - 1, b, a, c)
n = int(input())
print((2 ** n) - 1)
if n <= 20:
    honoi(n, 1, 2, 3)