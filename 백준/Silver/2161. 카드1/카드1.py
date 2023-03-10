n = int(input())
cards = [i for i in range(1, n+1)]
ans = []
while len(cards) > 1:
    ans.append(cards.pop(0))
    cards.append(cards.pop(0))

for k in ans:
    print(k, end=' ')
print(cards[0])