arr = input()
stk = []
tmp = 1
ans = 0
for i in range(len(arr)):
    a = arr[i]
    if a == '(':
        tmp *= 2
        stk.append(a)
    elif a == '[':
        tmp *= 3
        stk.append(a)

    elif a == ')':
        if not stk or stk[-1] == '[':
            ans = 0
            break
        if arr[i-1] == '(':
            ans += tmp
        tmp //= 2
        stk.pop()
    else:
        if not stk or stk[-1] == '(':
            ans = 0
            break

        if arr[i-1] == '[':
            ans += tmp
        tmp //= 3
        stk.pop()

if stk:
    ans = 0
print(ans)