from collections import deque
import sys

d = deque()
n = int(sys.stdin.readline())


def empty():
    if len(d) == 0:
        return 1
    else:
        return 0

for i in range(n):
    x = sys.stdin.readline().split()

    if x[0] == 'push_front':
        d.appendleft(x[1])

    elif x[0] == 'push_back':
        d.append(x[1])

    elif x[0] == 'pop_front':
        if empty() == 1:
            print(-1)
        else:
            print(d[0])
            d.popleft()

    elif x[0] == 'pop_back':
        if empty() == 1:
            print(-1)
        else:
            print(d[len(d) - 1])
            d.pop()

    elif x[0] == 'front':
        if empty() == 1:
            print(-1)
        else:
            print(d[0])

    elif x[0] == 'back':
        if empty() == 1:
            print(-1)
        else:
            print(d[len(d) - 1])

    elif x[0] == 'size':
        print(len(d))

    elif x[0] == 'empty':
        print(empty())