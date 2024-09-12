import sys
import heapq
sys.stdin = open('5251_input.txt')


def dijkstra(start):
    pq = []
    # 시작 노드 최단 거리는 0
    # heapq 에 리스트로 저장할 때는 맨 앞의 데이터를 기준으로 정렬된다.
    heapq.heappush(pq, (0, start))
    distance[start] = 0  # 출발점 초기화

    # 우선순위 큐가 빌 때 까지 반복
    while pq:
        # 가장 최단 거리인 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(pq)

        #도착지점이면 거리 리턴
        if now == n:
            return dist
        # 현재 노드가 이미 처리됐다면 skip
        if distance[now] < dist:
            continue

        # 현재 노드와 연결된 다른 인접한 노드 확인
        for next in graph[now]:
            next_node = next[0]
            cost = next[1]

            new_cost = dist + cost

            # 다음 노드를 가는 데 더 많은 비용혹은 같은 비용일 경우
            if new_cost >= distance[next_node]:
                continue

            # 다음 노드를 가는데 적은 비용이 드는 경우
            distance[next_node] = new_cost
            heapq.heappush(pq, (new_cost, next_node))


T = int(input())
for t in range(1, T+1):
    INF = int(1e9)  # 무한을 의미하는 값으로 10억

    # 노드의 개수, 간선의 개수를 입력받기
    n, m = map(int, input().split())
    # 시작 노드 번호(문제에 따라 다름)
    start = 0
    # 인접리스트 만들기
    graph = [[] for i in range(n + 1)]
    # 누적거리를 저장할 테이블 - INF 로 저장
    distance = [INF] * (n + 1)

    # 간선 정보를 입력
    for _ in range(m):
        a, b, w = map(int, input().split())
        graph[a].append([b, w])


    # 다익스트라 알고리즘 실행
    result = dijkstra(start)

    print(f'#{t}', result)
    print(graph)


if __name__ == '__main__':
    pass