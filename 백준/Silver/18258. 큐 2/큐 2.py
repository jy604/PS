import sys
from collections import deque

n = int(sys.stdin.readline())
queue = deque([])

for _ in range(n):
    i = sys.stdin.readline().split()

    if i[0] == 'push':
        queue.append(i[1])
    elif i[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft() # 선입선출
    elif i[0] == 'size':
        print(len(queue))
    elif i[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif i[0] == 'front': # 출력만, 삭제 x
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif i[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])