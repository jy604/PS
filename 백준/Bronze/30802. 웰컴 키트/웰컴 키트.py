n = int(input())
size = list(map(int, input().split()))
t, p = map(int, input().split())
t_cnt = 0
for i in size:
    if i == 0:
        continue
    elif i <= t:
        t_cnt += 1
    elif i % t == 0:
        t_cnt += i // t
    else:
        t_cnt += i // t + 1
p_bundle = n // p
p_one = n % p

print(t_cnt)
print(p_bundle, p_one, end='')