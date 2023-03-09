import itertools
while 1:
        num_list = list(map(int, input().split()))
        nums = num_list[1:]
        ans = []
        if num_list[0] == 0:
            break
        else:
            for i in itertools.combinations(nums, 6):
                print(*i)
        print()