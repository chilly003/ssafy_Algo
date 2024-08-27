from collections import deque
import sys
sys.stdin = open('5105_input.txt')

def bfs(i,j,N,maze):
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append([i,j])
    visited[i][j] = 1

    while q:
        ti, tj = q.popleft()

        #종료 조건
        if maze[ti][tj] == 2:
            return visited[ti][tj] - 1 - 1

        #탐색 조건
        ##탐색 범위가 인덱스 범위 안에 있으며 벽이 아니여야 하고 들린 곳이 아니여야한다.
        for di, dj in [[-1,0],[1,0],[0,1],[0,-1]]:
            wi, wj = ti+di, tj+dj
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi,wj])
                visited[wi][wj] = visited[ti][tj] + 1

    return 0


def solution():
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    #시작 지점 찾기
    start_i = 0
    start_j = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 3:
                start_i += i
                start_j += j

    return bfs(start_i, start_j, N, maze)

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        print(f'#{t} {solution()}')
