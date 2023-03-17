n, m = map(int, input().split())
res = []


def n_m(start):
    if len(res) == m:
        print(' '.join(map(str, res)))
        return

    for i in range(start, n+1):
            res.append(i)
            n_m(i)
            res.pop()

n_m(1)