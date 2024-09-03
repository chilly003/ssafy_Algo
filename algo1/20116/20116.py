from collections import deque
import sys
sys.stdin = open('5102_input.txt')

def bfs(start, goal, V, node_point):
    #0번째는 없음, 인덱스 위치 맞춰서 +1
    visited = [0] * (V+1)
    q = deque()
    q.append(start)
    visited[start] = 1

    while q:
        find = q.popleft()
        #종료 조건
        if find == goal:
            return visited[find] - 1
        #탐색 조건
        for go in node_point[find]:
            if visited[go] == 0:
                #go한 숫자를 find로 찾아야함
                q.append(go)
                visited[go] = visited[find] + 1

    return 0


def solution():
    V, E = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(E)]
    #1차원으로 만들기
    node = [i for l in arr for i in l]
    start, goal = map(int, input().split())

    #포인트 만들기
    node_point = [[] for _ in range(V+1)]
    for i in range(E):
        v1, v2 = node[2*i], node[2*i+1]
        node_point[v1].append(v2)
        node_point[v2].append(v1)

    return bfs(start, goal, V, node_point)


if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        print(f'#{t} {solution()}')
