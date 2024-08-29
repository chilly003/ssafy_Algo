import heapq

def find_min(disc, disc_start, N, time):
    pass
    

def solution(disc):
    N = len(disc)

    disc_start = []
    for i in range(N):
        disc_start.append([disc[i][1], disc[i][0]])


    ##문제 이렇게 구현하면 소요시간과 시작시간 따오는게 달라질 수 있을거 같음
    # 소요 시간, 시작 시간 --> 소요시간의 최소힙
    heapq.heapify(disc_start)
    # 시작 시간, 소요 시간 --> 시작시간의 최소힙
    heapq.heapify(disc)

    #시작 시간
    time = 0
    time += disc[0][0]

    find_min(disc, disc_start, N, time)

    print(disc, disc_start)

if __name__ == '__main__':
    disc = [[0, 3], [1, 9], [2, 6]]
    solution(disc)