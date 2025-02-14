from itertools import combinations
k = sorted([int(input()) for _ in range(9)])

com_list =list(combinations(k, 7))

for i in com_list:
    ans = sum(i)
    if ans == 100:
        # print(i) 튜플 형태로 출력
        for j in i:
            print(j)
        break
