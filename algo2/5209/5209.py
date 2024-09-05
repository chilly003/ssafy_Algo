import sys
sys.stdin = open('5209_input.txt')

def sol(lev, total):
    global min_sum
    #종료 조건
    if lev == N:
        min_sum = min(min_sum, total)

    #가지치기
    if total > min_sum:
        return

    for i in range(N):
        if visited[i]:
            continue
        #재귀 불러오기
        visited[i] = True
        sol(lev+1, total + arr[lev][i])
        visited[i] = False


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [False] * N
    min_sum = float('inf')

    sol(0,0)

    print(f'#{t} {min_sum}')

if __name__ == '__main__':
    pass