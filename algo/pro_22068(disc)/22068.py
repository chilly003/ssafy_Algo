import heapq

def find_min(disc, disc_start, N):
    pass

def solution(disc):
    N = len(disc)

    disc_start = []
    for i in range(N):
        disc_start.append([disc[i][1], disc[i][0]])

    # 소요 시간, 시작 시간 --> 소요시간의 최소힙
    heapq.heapify(disc_start)
    # 시작 시간, 소요 시간 --> 시작시간의 최소힙
    heapq.heapify(disc)

    find_min(disc, disc_start, N)

if __name__ == '__main__':
    disc = [[0, 3], [1, 9], [2, 6]]
    solution(disc)