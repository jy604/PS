import sys
input = sys.stdin.readline

while True:
    gram = list(map(int, input().split()))
    n = gram[0] # 직사각형의 수
    if n == 0: # 직사각형의 수가 0이면 멈춤
        break
    stk = []
    max_area = 0 # 넓이를 저장하는 변수
    for i in range(1, n+1):
        if len(stk) == 0:
            stk.append((i, gram[i])) # [(인덱스, 높이)]
        else:
            if stk[-1][1] <= gram[i]: # 현재 높이보다 스택 top의 높이가 작거나 같을 경우
                stk.append((i, gram[i])) # 스택에 더함
            else:
                while len(stk) > 0 and stk[-1][1] > gram[i]:
                    remove = stk.pop()
                    if len(stk) == 0:
                        width = i - 1
                    else:
                        width = i - 1 - stk[-1][0]
                    max_area = max(max_area, remove[1] * width)
            # 다 빼고 나면 스택에 저장된 것은 모두 i보다 작거나 같은 직사각형뿐이므로
            # i번째 idx를 넣어줌
                stk.append((i, gram[i]))
    # 위 과정이 끝나고도 스택에 요소가 남아있다면
    while stk:
        remove = stk.pop()
        if len(stk) == 0:
        # pop하고 스택이 비었다면 (0 ~ len - 1)까지 전체 폭이 width가 된다.
            width = n
        else:
            width = (n - stk[-1][0])
        max_area = max(max_area, remove[1] * width)
    print(max_area)