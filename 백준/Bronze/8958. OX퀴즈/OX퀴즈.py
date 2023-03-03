import sys
T = int(sys.stdin.readline())
for _ in range(T):
    a = sys.stdin.readline()
    count = 0
    total = 0

    for i in range(len(a)):
        if a[i] == "O":
            count += 1
            total += count
        elif a[i] == "X":
            count = 0
    print(total)