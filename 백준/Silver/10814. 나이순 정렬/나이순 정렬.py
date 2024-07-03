n = int(input())

human = []
for _ in range(n):
    age, name = input().split()
    human.append([int(age),name])

res = sorted(human, key= lambda x : x[0])

for i in res:
    print(i[0], i[1])