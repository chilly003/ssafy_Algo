import sys
sys.stdin = open('input (2).txt')

def sol(lev, total):
    pass


T = int(input())

dy = [-1,1,0,0]
dx = [0,0,-1,1]

for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * (N*N+1)

    for i in range(N):
        for j in range(N):
            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]

                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    continue

                if arr[ny][nx] == arr[i][j] + 1:
                    visited[arr[i][j]] = 1
                    #체크된 순간 다른 방향 볼 필요 없음.
                    #이유: 동일한 숫자가 없기 때문문
                    break

    cnt = max_cnt = start = 0

    for i in range(N * N -1, -1 , -1):
        if visited[i]:
            cnt += 1
        else:
            if cnt >= max_cnt:
                max_cnt = cnt
                start = i + 1
            cnt = 0


    print(f'#{t} {start} {max_cnt + 1}')

if __name__ == '__main__':
    pass