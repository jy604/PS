while 1:
    try:
        n = int(input())
    except:
        break
    num = 1
    i = 1
    while 1:
        if num % n == 0:
            print(i)
            break
        i += 1
        num = num * 10 + 1
