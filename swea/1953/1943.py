import sys
sys.stdin = open('sample_input.txt')

types = {1: ((-1, 0), (1, 0), (0, -1), (0, 1)),
         2: ((-1, 0), (1, 0)),
         3: ((0, -1), (0, 1)),
         4: ((-1, 0), (0, 1)),
         5: ((1, 0), (0, 1)),
         6: ((1, 0), (0, -1)),
         7: ((-1, 0), (0, -1))}


def recur(idx, r, c):
    # 종료 조건
    if idx == L:
        return

    for dr, dc in types[maze[r][c]]:
        nr = r + dr
        nc = c + dc
        if 0 <= nr < N and 0 <= nc < M and maze[nr][nc] != 0 and visited[nr][nc] == 0:
            # 연결된 통로인지 확인
            if (-dr, -dc) in types[maze[nr][nc]]:
                visited[nr][nc] = 1
                possible[nr][nc] = 1
                recur(idx + 1, nr, nc)
                visited[nr][nc] = 0


T = int(input())

for t in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    maze = [list(map(int, input().split())) for _ in range(N)]

    # visited : 방문 처리할 행렬
    # possible : L시간 안에 갈 수 있는 곳을 처리할 행렬
    visited = [[0] * M for _ in range(N)]
    possible = [[0] * M for _ in range(N)]
    # 시작 위치인 맨홀은 방문 처리
    visited[R][C] = 1
    possible[R][C] = 1

    # 맨홀에 도착한 상태에서 시작하므로 이미 1시간이 경과한 것
    recur(1, R, C)

    print(f'#{t} {sum(sum(possible[i]) for i in range(N))}')