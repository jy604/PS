import heapq
import sys

n = int(sys.stdin.readline())
cards = []
for _ in range(n):

    heapq.heappush(cards, int(sys.stdin.readline()))

total = 0
while len(cards) > 1:
    a = heapq.heappop(cards)
    b = heapq.heappop(cards)

    res = a + b
    total += res
    heapq.heappush(cards, res)

print(total)