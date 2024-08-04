n, m = map(int, input().split())
board = []
result = []
for _ in range(n):
    board.append(input())

for w in range(n - 7):
    for b in range(m - 7):
        w_index = 0
        b_index = 0
        for i in range(w, w + 8):
            for j in range(b, b + 8):
                # 2열의 합이 짝수면 같은 수
                if (i + j) % 2 == 0:
                    if board[i][j] != 'W':
                        w_index += 1
                    if board[i][j] != 'B':
                        b_index += 1
                else:
                    if board[i][j] != 'B':
                        w_index += 1
                    if board[i][j] != 'W':
                        b_index += 1
        result.append(min(w_index, b_index))

print(min(result))