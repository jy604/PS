def solution(bridge_length, weight, truck_weights):
    # 다리에 bridge_length대 올라갈 수 있음 = 한 대가 다리 지나는데 걸리는 시간
    bridge = [0] * bridge_length
    
    time = 0
    
    while len(bridge) != 0:
        time += 1
        bridge.pop(0)
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return time