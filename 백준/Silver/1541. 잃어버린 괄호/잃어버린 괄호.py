data = input().split('-')
s = 0
for i in data[0].split('+'):
    s += int(i)
for i in data[1:]:
    for j in i.split('+'):
        s -= int(j)
print(s)