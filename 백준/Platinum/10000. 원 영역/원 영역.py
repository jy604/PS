# 원 영역
# 1. 왼쪽 점부터 오름차순으로 정렬
# 2. 왼쪽점들 다 스택에 담은 뒤, 하나씩 꺼냄
# 2. 원이 만들어질때 ()마다 안/밖이 분리 됨 > cnt 1 증가
# 3. 원 안이 원으로 꽉 찰 경우, 영역이 2 추가 > cnt 2 증가

import sys
n = int(input())
circles = []
stk = []


cnt= 1 # 영역 수

for _ in range(n):
    x, r = map(int, sys.stdin.readline().split())
    circles.append(("(", x-r)) # 왼쪽 점 = 원의 중심 - 반지름
    circles.append((")", x+r)) # 오른쪽 점 = 원의 중심 - 반지름
# 정렬하는 법
    # ()( < 오른쪽 점이 왼쪽점보다 앞으로 와야함
circles.sort(key=lambda x:(x[0]), reverse=True)
circles.sort(key=lambda x:x[1])

# 왼쪽 점 '('스택에 담음
for circle in circles:
    if circle[0] == "(":
        stk.append(circle)
        continue

    total_radius = 0  # 내접원 확인 하는 변수

# 현재 점이 오른쪽 점 ')'
    while stk:
        prev = stk.pop()
        
        # 왼쪽 점을 만날 경우
        if prev[0] == "(":
            # 원의 지름 = 현재점) - 이전 점 (
            diameter = circle[1] - prev[1]
            if total_radius == diameter:
                cnt += 2
            else:
                cnt += 1
        # 원이 있다는 표시
            stk.append(("O", diameter))
            break
        # 내접원이 있을경우
        elif prev[0] == "O":
            total_radius += prev[1]

print(cnt)