# 빵 : 1, 야채 : 2, 고기: 3
# 스택에 순서대로 들어오면 빼야함 1231
def solution(ingredient):
    result = []
    cnt = 0
    for i in ingredient:
        result.append(i)
        if result[-4:] == [1, 2, 3, 1]:
            cnt += 1
            for _ in range(4):
                result.pop()
    return cnt