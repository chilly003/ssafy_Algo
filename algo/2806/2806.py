import sys
sys.stdin = open('sample_input.txt')

def is_safe(chess_N, row, col, N):
    # 같은 열에 다른 퀸이 있는지 확인
    # 이중 포문 해야되나 했는데 아님ㅁ
    for di, dj in [[-1, 0], [1, 0], [0, 1], [0, -1], [-1, -1], [1, 1], [1, -1], [-1, 1]]:
        wi, wj = row + di, col + dj
        while 0 <= wi < N and 0 <= wj < N:
            if chess_N[wi][wj] == 1:
                return False
            wi += di
            wj += dj
    return True

def find(N, row, chess_N):
    #끝까지 탐색했고 가능한 루트라면 1 리턴 -> cnt에 들어간다.
    if row == N:
        return 1

    cnt = 0
    for col in range(N):
        #만약 8방향 순회했는데 다른 퀸이 없다면 재귀함수 해라.
        if is_safe(chess_N, row, col, N):
            chess_N[row][col] = 1  #퀸을 놓음
            cnt += find(N, row + 1, chess_N)  #재귀(어려워ㅜ어리)
            chess_N[row][col] = 0  #원복

    #find 함수가 끝날때 지금까지 가능한 수 리턴
    return cnt

def solution():
    N = int(input())
    chess_N = [[0 for _ in range(N)] for _ in range(N)]

    #1은 예외로
    if N == 1:
        return 1

    #체스판 경우의 수 보기
    return find(N, 0, chess_N)

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        print(f'#{t} {solution()}')