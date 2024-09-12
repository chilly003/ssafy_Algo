def cook(lev):
    global min_S
    
    #길이기 구하는 조합보다 커지면 볼필요없음
    if len(in_A) > NN or len(in_B) > NN:
        return
    
    #레벨 즉 A와 B의 재료를합친게 N과 같아지면 검사하기
    if lev == N:
        A_cook = 0
        B_cook = 0
        for i in range(NN):
            for j in range(NN):
                A_cook += arr[in_A[i]][in_A[j]]
                B_cook += arr[in_B[i]][in_B[j]]
        min_S = min(min_S, abs(A_cook - B_cook))
        return

    in_A.append(lev)
    cook(lev+1)
    in_A.pop()

    in_B.append(lev)
    cook(lev+1)
    in_B.pop()

    return

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    NN = N//2       #반값
    min_S = 1e9     #최소값
    in_A = []
    in_B = []   

    cook(0)
    print(f'#{t} {min_S}')