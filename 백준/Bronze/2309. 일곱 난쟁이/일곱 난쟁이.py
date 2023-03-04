import itertools
#조합 라이브러리 이용
h = [int(input()) for _ in range(9)] 

for i in itertools.combinations(h, 7):
    if sum(i) == 100:
        for j in sorted(i): #오름차순 정렬
            print(j)
        break
