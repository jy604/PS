from sys import stdin
from collections import deque

n = int(stdin.readline())
queue = deque([])
for _ in range(n):
    i = stdin.readline().split()

    if i[0] == 'push':
        queue.append(i[1])

    elif i[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()

    elif i[0] == 'size':
        print(len(queue))

    elif i[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)

    elif i[0] == 'front':
        if len(queue) == 0:
             print(-1)
        else:
            print(queue[0])

    elif i[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])