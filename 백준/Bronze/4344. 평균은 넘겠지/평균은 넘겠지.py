import sys
c = int(sys.stdin.readline())
for _ in range(c):
    n = list(map(int, sys.stdin.readline().split()))
    avg = sum(n[1:])/n[0]
    cnt = 0
    for score in n[1:]:
        if score > avg:
            cnt += 1
    rate = cnt / n[0] * 100
    print('{0:0.3f}%'.format(rate))