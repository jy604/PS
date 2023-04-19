# 약수
# 진짜 약수 = n이 a의 배수, a가 1과 n이 아님
# 진짜 약수 중 제일 큰 수 * 제일 작은 수 = n
n = int(input())
num = list(map(int, input().split()))
a = max(num)
b = min(num)
print(a*b)