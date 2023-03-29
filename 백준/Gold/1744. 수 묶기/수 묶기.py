# 수 묶기
n = int(input())
positive = [] # 양수
negative = [] # 음수
result = 0
for _ in range(n):
    arr = int(input())
    if arr > 1:
        positive.append(arr)
    elif arr == 1:
        result += 1
    else:
        negative.append(arr)

# 양수 내림차순으로 정렬
positive.sort(reverse=True)
negative.sort() # 음수는 오름차순
# print(*positive)
# print(*negative)

# 양수리스트에 남은 수가 짝수일경우
if len(positive) % 2 == 0:
    for i in range(0, len(positive), 2):
        result += positive[i] * positive[i + 1]
# 짝수 개가 아닐 경우
else:
    for i in range(0, len(positive) -1, 2):
        result += positive[i] * positive[i + 1]
    result += positive[len(positive) - 1] # 마지막 수
if len(negative) % 2 == 0:
    for i in range(0, len(negative), 2):
        result += negative[i] * negative[i+1]
else:
    for i in range(0, len(negative) -1, 2):
        result += negative[i] * negative[i + 1]
    result += negative[len(negative) - 1] # 마지막 수


print(result)

