import sys

n = int(sys.stdin.readline())
cnt = [0] * 10001 #작업 배열

#메모리 초과 > 두 식 합치기
# for _ in range(n): #배열에 입력된 값 넣어 raw 배열 만들기
#     array.append(int(sys.stdin.readline()))
#
# for i in range(n):
#     cnt[array[i]] += 1

for _ in range(n):
    cnt[int(sys.stdin.readline())] += 1

#런타임에러 > cnt 전체 안돌도록 조건 달아줘야함
for i in range(10001):
    if cnt[i] != 0:
        for j in range(cnt[i]):
            print(i)