n = input()
cnt = 0

for i in range(1, int(n)+1):
    list_num = list(map(int, str(i)))
    if len(list_num) <= 2:
        cnt += 1
    elif list_num[0] - list_num[1] == list_num[1] - list_num[2]:
        #각 자리수의 차를 구하는 식... 1,2의 차이랑 2,3의 차이가 같아야함
        cnt += 1
print(cnt)