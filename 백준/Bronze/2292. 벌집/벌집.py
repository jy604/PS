n = int(input())
p = 1
cnt = 1
while n > p:
    p += (6 * cnt)
    cnt += 1
print(cnt)