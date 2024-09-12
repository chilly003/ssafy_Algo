import sys

sys.stdin = open('5249_input.txt')

from heapq import heappop, heappush


def prim(start):
    heap = list()
    MST = [0] * (N + 1)

    sum_weight = 0

    heappush(heap, (0, start))

    while heap:
        weight, v = heappop(heap)

        if MST[v]:
            continue

        MST[v] = 1
        sum_weight += weight


        for next in range(N + 1):
            if graph[v][next] == 0:
                continue
            if MST[next]:
                continue

            heappush(heap, (graph[v][next], next))

    return sum_weight


T = int(input())
for t in range(1, T + 1):
    N, E = map(int, input().split())
    graph = [[0] * (N + 1) for _ in range(N + 1)]
    for _ in range(E):
        u, v, w = map(int, input().split())
        graph[u][v] = w
        graph[v][u] = w

    result = prim(0)
    print(f'#{t} {result}')


if __name__ == '__main__':
    pass