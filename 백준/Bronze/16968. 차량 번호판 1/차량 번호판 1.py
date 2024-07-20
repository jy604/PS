form = input()
result = 1
for i in range(0, len(form)):
    if form[i] == 'd':
        if i > 0 and form[i - 1] == 'd':
            result *= 9
        else:
            result *= 10
    elif form[i] == 'c':
        if i > 0 and form[i - 1] == 'c':
            result *= 25
        else:
            result *= 26

print(result)