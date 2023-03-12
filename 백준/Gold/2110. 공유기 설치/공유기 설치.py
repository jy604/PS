import sys
n, c = map(int, sys.stdin.readline().split())
router = []
for i in range(n):
    router.append(int(sys.stdin.readline()))
router.sort()
result = 0
start = 1
end = router[-1] - router[0] # max()는 시간복잡도가 높아서 쓰면 안됨 gap 값
# 두 공유기 사이의 거리를 이분탐색으로 실행 > mid가 두 공유기 사이의 gap길이임
while start <= end:
    first = router[0]
    cnt = 1
    mid = (start + end) // 2
    for i in range(1, len(router)): # index
        if router[i] >= first + mid:
           first = router[i]
           cnt += 1

    if cnt < c:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)