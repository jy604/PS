import sys
n = int(sys.stdin.readline())
board = [0] * n 
visited = [0] * n
ans = 0

def is_pos(x):
    for i in range(x):
        if board[x] == board[i] or abs(board[x] - board[i]) == x - i:
            return False
    return True


def dfs(x):
    global ans
    if x == n:
        ans += 1
        return
    for i in range(n):
        board[x] = i
        if is_pos(x):
            dfs(x+1)
dfs(0)
print(ans)