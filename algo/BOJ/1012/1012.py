import sys
sys.stdin = open('1012.txt')

def dfs(x,y,cabbage_field,N,M):
    cabbage_field[x][y] = 0
    for dx, dy in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        ix = x + dx
        jy = x + dy
        if 0 <= ix < N and 0 <= jy < M and cabbage_field[ix][jy] == 1:
            dfs(ix,jy,cabbage_field,N,M)

def solution(t):
    #배추밭 가로,세로, 좌표값
    N, M, K = map(int,input().split())
    cabbage_field = [[0]*M for _ in range(N)]

    #배추 심기
    for _ in range(K):
        x, y = map(int,input().split())
        cabbage_field[x][y] = 1

    #배추흰지렁이 수
    Cabbage_white_worm = 0

    #배추가 심어진 위치 중심으로 몇개의 배추가 이어져 있는지 확인 후 지렁이 추가
    for x in range(N):
        for y in range(M):
            if cabbage_field[x][y] == 1:
                dfs(x,y,cabbage_field,N,M)
                Cabbage_white_worm += 1

    return Cabbage_white_worm

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        print(f'#{t} {solution(t)}')
