import sys
sys.stdin = open('graph_input.txt')

def solution(t):
    cur_node_list = []      #프린트 할라고 만든거임
    print(f'#{t}',end=" ")  #번호 먼저 출력
    V, E = map(int,input().split()) #점, 선
    edges = list(map(int, input().split()))

    #그래프는 각 구간 점을 기준으로 이어진 선들의 종착지 점7은 점 6,3과 이어져있음
    graph = [[] for _ in range(V+1)]
    for i in range(E):
        v1, v2 = edges[i*2], edges[i*2+1]
        graph[v1].append(v2)
        graph[v2].append(v1)

    visted = [0]*(V+1)

    stack = [1]
    while stack:
        cur_node = stack.pop()

        if visted[cur_node]:
            continue

        visted[cur_node] = 1
        cur_node_list.append(str(cur_node))

        for next_node in sorted(graph[cur_node], reverse=True):
            if not visted[next_node]:
                stack.append(next_node)


    print('-'.join(cur_node_list)) #join써서 출력

if __name__ == '__main__':
    T = 1
    for t in range(1, T + 1):
        solution(t)