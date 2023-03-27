# 신입 사원
import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    n = int(input())
    p = []
    for i in range(n):
        p.append(list(map(int, input().split())))
    # [1, 4] [2, 3] [3, 2] [4, 1] [5, 5] 서류 기준으로 오름차순 정렬
    p.sort()
    tmp = p[0][1]
    cnt = 1 # 1등 이미 넣음
    for j in range(len(p)):
        if tmp > p[j][1]:
            cnt += 1
            tmp = p[j][1]
    print(cnt)