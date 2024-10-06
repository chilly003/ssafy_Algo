import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    # print(scoville)
    while scoville[0] <K:
        new_S = heapq.heappop(scoville) + heapq.heappop(scoville) *2
        heapq.heappush(scoville, new_S)
        # print(scoville)
        answer += 1
        # print(answer)
        if len(scoville) ==1 and scoville[0] < K:
            return -1

    return answer

if __name__ == '__main__':
    scoville = [1, 2, 3, 9, 10, 12]
    K = 7
    print(solution(scoville, K))