import sys
n = int(sys.stdin.readline())
papers = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
w = 0
b = 0


def color_find(x, y, n):
    global w, b
    color = papers[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if color != papers[i][j]:
                color_find(x, y, n//2)
                color_find(x, y + n//2, n // 2)
                color_find(x + n // 2, y, n //2)
                color_find(x + n // 2, y + n // 2, n //2)
                return
    if color == 0:
        w += 1
    else:
        b += 1


color_find(0, 0, n)
print(w)
print(b)