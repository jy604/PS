# 두 리스트 묶기 : zip 활용
def solution(name, yearning, photo):
    result = []
    score =  dict(zip(name, yearning))
    # print(score)
    for pic in photo:
        tmp = 0
        for i in pic:
            tmp += score.get(i, 0)
        result.append(tmp)
    return result