T = int(input())

for _ in range(T):
    s = list(input().split())
    for word in s:
        print(word[::-1], end=' ')
    print()