def solution(numbers):
    answer = ''
    numbers = sorted(numbers, reverse=True, key= lambda x: (str(x)*4)[0:4])
    for i in numbers:
        answer += str(i)
    if answer[0] == "0":
        answer = "0"
    return answer


# from itertools import permutations
# def solution(numbers):
#     answer = []
#     num = list(permutations(numbers, len(numbers)))
#     for i in num:
#         answer.append("".join(map(str, i)))
#     return max(answer)