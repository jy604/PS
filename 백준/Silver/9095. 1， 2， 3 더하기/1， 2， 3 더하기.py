T = int(input())
result = []


def sub(num, sum):
    global cnt

    if sum > num:
        return  #생각 못함
    if sum == num: #탈출조건이 sum이므로 인자에 무조건 포함
        cnt += 1
        return

    for i in range(1, 4):
        sum += i
        sub(num, sum)
        sum -= i


for _ in range(T):
    num = int(input())
    cnt = 0
    sub(num, 0)
    result.append(cnt)

for answer in result:
    print(answer)