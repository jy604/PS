import sys
T = int(sys.stdin.readline())
for _ in range(T):
    r, s = sys.stdin.readline().split()
    list(s)
    for i in range(len(s)):
        print(int(r) * s[i], end='')
    print()