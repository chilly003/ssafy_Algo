import heapq

def solution(operations):
    answer = []
    heapq.heapify(answer)
    for i in operations:
        if i[0] == "I":
            heapq.heappush(answer,int(i[2:]))
        elif i == "D -1" and answer:
            heapq.heappop(answer)
        elif i == "D 1" and answer:
            a = max(answer)
            answer.pop(answer.index(a))

    real_a = []
    if answer:
        real_a.append(max(answer))
        real_a.append(min(answer))
    else:
        real_a = [0,0]

    return real_a


if __name__ == '__main__':
    operations = ["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]
    print(solution(operations))