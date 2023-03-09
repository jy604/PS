def dfs(bw):
    global result, cards
    if len(cards) == 3:
        total = sum(cards)
        if total <= m:
          result.append(total)
        return

    for i in range(bw, n):
        cards.append(card[i])
        dfs(i+1)
        cards.pop()


n, m = map(int, input().split())
card = list(map(int, input().split()))
cards = []
result = []
dfs(0)

print(max(result))