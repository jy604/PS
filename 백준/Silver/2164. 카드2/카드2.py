from collections import deque
import sys
n = int(sys.stdin.readline())
cards = deque(list(range(1, n+1)))
ans = []
while len(cards) > 1:
    ans.append(cards.popleft())
    cards.append(cards.popleft())

print(cards[0])