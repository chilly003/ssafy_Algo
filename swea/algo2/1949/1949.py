delta = [[-1, 0], [0, 1], [1, 0], [0, -1]]
def recur(arr, cnt, i, j):
    '''
    :param arr: 변형된 산
    :param cnt: 등산로 길이
    :param i: 인덱스
    :param j: 인덱스
    '''
    global max_len

    max_len = max(cnt, max_len)

    #상우하좌 자신보다 작은 수 탐색
    for di, dj in delta:
        ni, nj = di + i, dj + j
        if 0 <= ni < N and 0 <= nj < N and arr[ni][nj] < arr[i][j]:
            recur(arr, cnt + 1, ni, nj)


T  = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    ar = [list(map(int, input().split())) for _ in range(N)]
    #봉우릭
    max_num = max(map(max, ar))
    max_len = 0

    for i in range(N):
        for j in range(N):
            #산 K 만큼 깎기
            for k in range(1, K+1):
                ar[i][j] -= k
                for row in range(N):
                    for col in range(N):
                        if ar[row][col] == max_num: #봉우리만 탐색
                            recur(ar, 1, row, col)
                #산 원복
                ar[i][j] += k

    print(f'#{t}', max_len)