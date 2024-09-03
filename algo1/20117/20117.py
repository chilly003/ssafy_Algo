from collections import deque
import sys
sys.stdin = open('input (10).txt')


def bfs(i, j, N, maze):
    # visited = [[0] * N] * N 이렇게 하면 얕은 복사라 값이 다 바뀌니깐 for문으로 써주기
    visited = [[0] * N for _ in range(N)]
    q = deque()
    q.append([i, j])
    visited[i][j] = 1
    while q:
        ti, tj = q.popleft()
        if maze[ti][tj] == 3:
            return 1
        for di, dj in [[-1, 0], [1, 0], [0,-1], [0, 1]]:
            wi, wj = ti + di, tj + dj
            #인덱스 범위 벗어나지 않고 벽이 아니여야함. 그리고 이미 탐색한 곳이 아니여야함.
            if 0 <= wi < N and 0 <= wj < N and maze[wi][wj] != 1 and visited[wi][wj] == 0:
                q.append([wi, wj])
                visited[wi][wj] = 1
    return 0

def solution():
    testcase = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    return bfs(1, 1, 16, maze)

if __name__ == '__main__':
    for t in range(1, 11):
        print(f'#{t} {solution()}')
