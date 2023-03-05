def is_prime(n):
    for j in range(2, int(n ** 0.5) + 1):
        if n % j == 0:
            return False
    if n == 1:
        return False
    return True


T = int(input())

for _ in range(T):
    num = int(input())
    for i in range(num // 2, 0, -1):
        if is_prime(i) and is_prime(num - i):
            print(i, num - i)
            break
