import heapq
import sys

n = int(sys.stdin.readline())
heap = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        if heap: # heappop는 최소힙 동작 > -1 곱해 가장 작은 수로 만듦
            print((-1)*heapq.heappop(heap))
        else:
            print(0)
    else:
        heapq.heappush(heap, (-1)*x)