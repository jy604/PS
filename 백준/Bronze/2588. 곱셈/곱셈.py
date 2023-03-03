a = int(input())
b = int(input())
result = list(map(int, str(b)))
result = [int(i) for i in result]
sum = 0
for i in reversed(range(len(result))):
    print(a*result[i])
    sum += a*result[i]
print(a*b)