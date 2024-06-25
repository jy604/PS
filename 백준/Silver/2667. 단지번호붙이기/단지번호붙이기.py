n = int(input())
graph = [list(map(int, input())) for _ in range(n)]

def dfs(x,y):
    global count
    # 범위를 벗어난 경우
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    # 현재 위치가 집이 아닌 경우
    if graph[x][y] == 0:
        return False
    # 현재 위치 방문 처리(0으로 변경)!!!
    graph[x][y] = 0
    count += 1

    dfs(x - 1, y)
    dfs(x + 1, y)
    dfs(x, y - 1)
    dfs(x, y + 1)


result = []

for i in range(n):
    for j in range(n):
        if graph[i][j] == 1:
            count = 0
            dfs(i, j)
            result.append(count)

result.sort()
print(len(result))
for s in result:
    print(s)
