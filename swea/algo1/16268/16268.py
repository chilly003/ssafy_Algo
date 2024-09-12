import sys
sys.stdin = open('./input1 (1).txt')

def solution(t):
    N , M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for i in range(N):
        for j in range(M):
            current_sum  = 0
            current_sum += arr[i][j]
            #상
            if i-1 >= 0:
                current_sum += arr[i-1][j]
            #하 / 인덱스 위치 주의해서 설정하기
            if i < N -1:
                current_sum += arr[i+1][j]
            #좌
            if j - 1 >= 0:
                current_sum += arr[i][j-1]
            #우
            if j < M -1:
                current_sum += arr[i][j+1]

            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        print(f'#{t} {solution(t)}')