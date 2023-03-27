# 회의실 배정
import sys
input = sys.stdin.readline
n = int(input())
cnt = 0
time = []

for i in range(n):
    start, end = map(int, input().split())
    time.append([start, end])
# 시간 정렬 시작시간으로 오름차순 후, 끝나는 시간으로 다시 오름차순
time = sorted(time, key= lambda x:x[0])
time = sorted(time, key= lambda x:x[1])
# print(time)
cnt = 0
last = 0 # 가장 최근에 뽑인 강의의 끝나는 시간
for i, j in time:
    if i >= last: # 다른 강의 시작 시간이 끝나는 시간보다 크거나 같다면
        cnt += 1 # 강의를 시작할 수 있음
        last = j # 강의 종료시간 대입
print(cnt)