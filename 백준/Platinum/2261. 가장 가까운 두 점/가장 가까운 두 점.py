# 가장 가까운 두 점
# 분할 정복
# 1. 모든 점을 x좌표를 기준으로 정렬한다
# 2. 완전탐색으로 x좌표의 최소값을 찾는다
# 3. 3개 이하로 분할이 되면 점 사이의 최소 거리를 찾는다
# 3 - 1. x좌표 기준에서 후보군을 찾는다.
# 4. y좌표 기준으로 정렬
# 5. x좌표와 똑같이 d사이에 있는 점들의 후보군을 구하여 min_dict를 업데이트해준다. d 사이가 아닐경우 break
# 6. sol(0, n-1) 재귀호출해서 min_dict를 출력한다


import sys

n = int(input())
coordinate = [list(map(int, sys.stdin.readline().split())) for _ in range(n)] # x, y

coordinate.sort()


# 두 점 사이 거리 계산하는 함수
def get_dist(a, b):
    return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2


# 완전탐색 함수
def sol(start, end):
    # 점 하나 > 최대값
    if start == end:
        return sys.maxsize
    # 점 두 개 > 거리 계산 바로 때림
    if end - start == 1:
        return get_dist(coordinate[start],coordinate[end])
    # 분할정복
    mid = (start + end) // 2
    min_dict = min(sol(start, mid), sol(mid, end)) # d

    # x후보군 리스트에 집어넣기
    x_target = []
    for i in range(start, end+1):
        if (coordinate[mid][0] - coordinate[i][0]) ** 2 < min_dict:
            x_target.append(coordinate[i])

    # y기준으로 정렬하기
    x_target.sort(key=lambda x:x[1])

    # d범위에 있는 y좌표들을 찾기 위한 for문
    for i in range(len(x_target)-1):
        for j in range(i+1, len(x_target)):
            if (x_target[i][1] - x_target[j][1]) ** 2 < min_dict:
                min_dict = min(min_dict, get_dist(x_target[i],x_target[j]))
            else:
                break
    return min_dict


print(sol(0, n-1))