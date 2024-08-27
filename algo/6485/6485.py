#삼성 버스 노선
T = int(input())
for tc in range(1,T+1):
    N = int(input())           #노선수
    count = [0] * 5001         #5000번 버스 정류장까지

    #N개의 노선정보를 모두 읽어 놓고 처리 or 읽을 때마다 처리
    for _ in range(N):
        #a에서 b로 가는 버스 노선의 시점a와  종점b, a<=b
        A, B = map(int,input().split())
        for j in range(A, B+1):
            count[j] += 1
    P = int(input())           #노선수를 출력할 P개의 버스 정류장
    #모두 읽어 놓고 처리
    busstop = [int(input()) for _ in range(P)]
    print(f'#{tc}', end=' ')
    for j in busstop:          #노선수를 출력할 정류장 번호
        print(count[j], end=' ')
    print()