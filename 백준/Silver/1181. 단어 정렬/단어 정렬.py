n = int(input())
word = []
for i in range(n):
    word.append(input())

word_list = list(set(word))

sort_word = []
for i in word_list:
    sort_word.append((len(i), i))
result = sorted(sort_word)

for len_word, word in result:
    print(word)