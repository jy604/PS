n = int(input()) # 보드 크기
k = int(input()) # 사과 개수
board = [[0] * (n+1) for _ in range(n+1)] # 맵 정보
info = [] # 방향 회전

for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1 # 사과 위치

# 방향 정보
le = int(input())

for _ in range(le):
    x, c = input().split()
    info.append((int(x), c))
# 동(우), 남(하), 서(좌), 북(상)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]


def turn(direction, c):
    if c == "L": # 왼쪽
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction


def simulate():
    x, y = 1, 1 # 뱀의 머리 위치
    board[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0
    time = 0 # 초시간
    index = 0 # 다음에 회전할 정보
    q = [(x, y)] # 뱀 몸통 정보 꼬리가 앞임

    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]

        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and board[nx][ny] != 2:
        # 사과가 없다면 이동 후에 꼬리 제거
            if board[nx][ny] == 0:
                board[nx][ny] = 2
                q.append((nx, ny))
                px, py = q.pop(0)
                board[px][py] = 0
        # 사과가 있다면 이동 후에 꼬리 그대로 두기
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))
        # 벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1
            break
        x, y = nx, ny
        time += 1
        if index < le and time == info[index][0]: # 회전할 시간일 경우 회전
            direction = turn(direction, info[index][1])
            index += 1
    return time


print(simulate())