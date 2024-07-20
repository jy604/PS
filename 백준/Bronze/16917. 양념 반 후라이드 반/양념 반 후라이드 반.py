a, b, c, x, y = map(int, input().split())

# 반반치킨이 더 비쌀때 각각 주문
if a + b < c * 2:
    print(a * x + b * y)
# min(양, 후) * 반반 주문 + 남은 치킨 주문
else:
    result = 2 * c * min(x, y)
    if x >= y:
        tmp = x - y
        # 남은 치킨이 반반주문과 그냥 주문 중 어느 것이 더 저렴한지 비교
        result += min(tmp * a, tmp * 2 * c)
        print(result)
    else:
        tmp = y - x
        result += min(tmp * b, tmp * 2 * c)
        print(result)