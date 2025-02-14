# 조합 안 쓰고 이중반복문으로 찾기
k = [int(input()) for _ in range(9)]
total_height = sum(k) # 난쟁이 전체 키의 합

# 가짜 두 명 고르기
# 이중 반복문 사용

f1, f2 = 0, 0
for i in range(8):
    for j in range(i + 1, 9):
        if k[i] + k[j] == total_height - 100:
            f1, f2 = k[i], k[j]
            break
    if f1 != 0:
        break

k.remove(f1)
k.remove(f2)

for i in sorted(k):
    print(i)