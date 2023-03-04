n = int(input())
word = []

for _ in range(n):
    word.append(input())
word_list = list(set(word)) #set 자료형으로 중복 제거 후 새 리스트로 넣음

sort_word = []
for i in word_list: #중복만 제거한 리스트 정렬하는 for문
    sort_word.append((len(i), i)) #인덱스를 만들어서 word의 단어수만큼 인덱싱 하여 묶어서 저장
result = sorted(sort_word) #단어수별로 sort됨

for len_word, word in result: #리스트에 인수가 2개일 경우 매개변수도 2개 써줘야함
    print(word) #필요한 값만 출력