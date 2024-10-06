from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)  # [0]*bridge_length을 덱으로 변환
    truck_weights = deque(truck_weights)  # 리스트를 덱으로 변환

    currentWeight = 0
    while len(truck_weights) != 0:
        time = time + 1

        currentWeight -= bridge.popleft()

        #만약 최근 무게와 그다음 트럭이 기준치와 같거나 작다면
        #무게를 더하고 그걸 다리에 표시해 준다.
        if currentWeight + truck_weights[0] <= weight:
            currentWeight += truck_weights[0]
            bridge.append(truck_weights.popleft())

        #그게 아니라면 앞서 뺀 다리를 새로 놔준다.
        else:
            bridge.append(0)

    #모든 트럭이 다리를 지나는데 얼마나 걸렸는지 파악
    time = time + bridge_length

    return time

if __name__ == '__main__':
    bridge_length = 2
    weight = 10
    truck_weights = [7,4,5,6]
    print(solution(bridge_length, weight, truck_weights))