# 230602 3의 배수
n = input()
cnt = 0

while len(n) >= 2:
    res = 0
    for i in range(len(n)):
        res += int(n[i])
    cnt += 1
    n = str(res)

print(cnt)
if int(n) % 3 == 0:
    print("YES")
else:
    print("NO")

