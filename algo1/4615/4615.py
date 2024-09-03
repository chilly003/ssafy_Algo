#오셀로 게임
import sys
sys.stdin = open('sample_input(1).txt')

def solution(t):
    #N 오셀로 판의 크기, M 턴 수
    N , M = map(int,input().split())
    arr = [[0]*N for _ in range(N)]

    for _ in range(M):
        i, j, color = map(int,input().split())
        i -= 1
        j -= 1
        arr[i][j] = color
        for k in range(1, N):
            #확인하는 위치에 돌이 있는데 같은 색깔이 아니고 현재 위치 기준과 그 끝에 같은 돌 색이면 색을 바꿔줘라
            #순서대로 상, 하, 우, 좌, 오른쪽 위 대각선, 왼쪽 위 대각선, 왼쪽 아래 대각선, 오른쪽 아래 대각선
            if i - k >= 0 and arr[i-k][j] != color and arr[i-k][j] != 0 and arr[i-k-1][j] == color:
                arr[i-k][j] = color
            if i + k < N and arr[i+k][j] != color and arr[i+k][j] != 0 and arr[i+k+1][j] == color:
                arr[i+k][j] = color
            if j + k < N and arr[i][j+k] != color and arr[i][j+k] != 0 and arr[i][j+k+1] == color:
                arr[i][j+k] = color
            if j - k >= 0 and arr[i][j-k] != color and arr[i][j-k] != 0 and arr[i][j-k-1] == color:
                arr[i][j-k] = color
            if i - k >= 0 and j + k < N and arr[i-k][j+k] != color and arr[i-k][j+k] != 0 and arr[i-k-1][j+k+1] == color:
                arr[i-k][j+k] = color
            if i - k >= 0 and j - k >= 0 and arr[i-k][j-k] != color and arr[i-k][j-k] != 0 and arr[i-k-1][j-k-1] == color:
                arr[i-k][j-k] = color
            if i + k < N and j - k >= 0 and arr[i+k][j-k] != color and arr[i+k][j-k] != 0 and arr[i+k+1][j-k-1] == color:
                arr[i+k][j-k] = color
            if i + k < N and j + k < N and arr[i+k][j+k] != color and arr[i+k][j+k] != 0 and arr[i+k+1][j+k+1] == color:
                arr[i+k][j+k] = color

    black = white = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                black += 1
            elif arr[i][j] == 2:
                white += 1

    return print(f'#{t} {black} {white}')

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        solution(t)

