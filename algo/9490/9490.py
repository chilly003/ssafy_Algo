import sys
sys.stdin = open('./input1.txt')

def solution(t):
    N , M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_sum = 0
    for i in range(N):
        for j in range(M):
            #current_sum이 for문 밖에 있을 경우 초기화가 안되니 주의해서 위치 파악하자.
            current_sum = 0
            #처음 포인트가 되는 위치 기준을 먼저 더해주고
            current_sum += arr[i][j]
            #그 위치의 꽃잎 개수만큼 상,하,좌,우를 더해준다!!!
            petal = arr[i][j]
            #상 // 위로갈 때 인덱스 [0][0]을 넘어갈 수 없다. 그러니 if문으로 제한 걸어주기
            #if문 안쓰면 인덱스 에러가 뜬다.
            current_sum += sum(arr[i-u][j] for u in range(1,petal+1) if i - u >= 0)

            #하 // 아래로 갈 때 인덱스 [N]을 넘어갈 수 없다. 똑같이 if문으로 제한 걸기
            current_sum += sum(arr[i+d][j] for d in range(1,petal+1) if i + d <= N - 1)

            #좌 //상과 동일
            current_sum += sum(arr[i][j-l] for l in range(1,petal+1) if j - l >= 0)

            #우 //하와 동일
            current_sum += sum(arr[i][j+e] for e in range(1,petal+1) if j + e <= M - 1)

            #값 업데이트
            if current_sum > max_sum:
                max_sum = current_sum
    return max_sum

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        print(f'#{t} {solution(t)}')