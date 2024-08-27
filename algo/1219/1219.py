import sys
sys.stdin = open('./input (4).txt')

def solution(t):
    V, E = map(int,input().split()) #점, 선
    edges = list(map(int, input().split()))
    A = 0
    B = 99
    #그래프를 만들어서 각 자리에 어떤 길로 나눠져있는지 확인
    graph = [[] for _ in range(100)]
    for i in range(E):
        v1, v2 = edges[i*2], edges[i*2+1]
        graph[v1].append(v2)
        # graph[v2].append(v1) #순방향 탐색을 위해 안한다.

    visted = [0]*100

    def dfs(start_node):
        stack = [start_node]
        while stack:
            cur_n = stack.pop()

            if visted[cur_n]:
                continue

            visted[cur_n] = 1
            if cur_n == B:
                return 1

            for next_n in graph[cur_n]:
                if not visted[next_n]:
                    stack.append(next_n)
        else:
            return 0

    print(f'#{t} {dfs(A)}')


if __name__ == '__main__':
    T = 10
    for t in range(1, T + 1):
        solution(t)