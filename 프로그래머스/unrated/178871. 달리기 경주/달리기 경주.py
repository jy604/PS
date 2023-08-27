# callings에 적힐때마다 앞의 거랑 위치를 바꿔줘야함
# 인덱스 구하는 법,,, enumerate (idx, value)
def solution(players, callings):
    result = { player: i for i, player in enumerate(players) } # 이름:현재등수
    # print(result) 
    # {'mumu': 0, 'soe': 1, 'poe': 2, 'kai': 3, 'mine': 4}
    for call in callings:
        idx = result[call] # 추월한 선수의 현재 등수
        result[call] -= 1 # 추월한 선수의 등수 수정
        result[players[idx - 1]] += 1 # 추월당한 선수(앞선수)의 등수 수정
        players[idx - 1], players[idx] = players[idx], players[idx - 1] # swap
    return players