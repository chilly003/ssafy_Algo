import sys
sys.stdin = open('sample_input.txt')

def recur(N, K, mm, idx, cnt, visited, where):
    global min_num
    i, j = idx[0], idx[1]
    # 동 서 남 북 기준으로 만들었음
    compass = {1: [1,0],
               2: [-1,0],
               3: [0, 1],
               4: [0, 1]}

    if mm[i][j] == "Y":
        return min_num

    # 처음은 위로 바라보고 있다는 것을 앎.
    # 근데 이후 방향을 돌린다면 이걸 알아야 회전을 하느냐 안하느냐를 알 수 잇음

    for di, dj, c in [[1,0,1], [-1,0,2], [0, 1, 3], [0, -1, 4]]:
        wi , wj = i + di, j + dj
        if 0 <= wi < N and 0 <= wj < N and visited[wi][wj]:





def s():
    N, K = map(int, input().split())
    mm = [list(map(str, input())) for _ in range(N)]
    idx = []
    visited = [[0 for _ in range(N)]for _ in range(N)]
    #위치 찾기
    for i in range(len(mm)):
        for j in range(len(mm[i])):
            if mm[i][j] == "X":
                idx.append(i)
                idx.append(j)
    min_num = 1e9
    visited[i][j] = 1
    recur(N, K, mm, idx ,0, visited, 4)

    return min_num


if __name__ == "__main__":
    T = int(input())
    for t in (1, T+1):
        print(f'#{t} {s()}')