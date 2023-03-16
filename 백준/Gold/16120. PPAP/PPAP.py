string = input()
stk = []
ppap = ['P', 'P', 'A', 'P']
for i in range(len(string)):
    stk.append(string[i])
    if stk[-4:] == ppap:
        for _ in range(4):
            stk.pop()
        # stk.pop()
        # stk.pop()
        # stk.pop()
        stk.append("P")
if stk == ppap or stk == ["P"]:
    print("PPAP")
else:
    print("NP")
