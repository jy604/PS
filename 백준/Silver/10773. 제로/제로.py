import sys
stk = [] #스택 리스트

k = int(sys.stdin.readline()) #명령어 개수

for i in range(k):
    nums = int(sys.stdin.readline()) #정수 입력
    if nums == 0:
        stk.pop()
    else:
        stk.append(nums)

print(sum(stk))