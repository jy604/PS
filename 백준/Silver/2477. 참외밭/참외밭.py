# (가장 큰 사각형 - 제일 작은 사각형) * k
# 동서남북 = 동서(1,2), 남북(3,4)이 짝
k = int(input())
a = [list(map(int, input().split())) for _ in range(6)]
w = []
h = []
result = 0
s_a = []

for i in range(6):
    if a[i][0] == 1 or a[i][0] == 2:
        w.append(a[i][1])
    else:
        h.append(a[i][1])
    # print(w, h)
# print(abs(((w[0] * h[0]) - (w[2] * h[2]))* k))

#s_a의 길이
for i in range(6):
    if a[i][0] == a[(i+2)%6][0]:
        s_a.append(a[(i+1)%6][1])

print(((max(w) * max(h)) - (s_a[0]*s_a[1]))*k)