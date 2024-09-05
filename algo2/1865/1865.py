import sys
sys.stdin = open('input (1).txt')

def sol(lev, work):
    global max_work

    #종료 조건
    if lev == N:
        max_work = max(max_work, work)
        return

    #가지치기
    if work <= max_work:
        return

    for i in range(N):
        if visited[i]:
            continue
        visited[i] = 1
        sol(lev + 1, work * (arr[lev][i]*0.01))
        visited[i] = 0


T = int(input())
for t in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    max_work = 0

    sol(0, 1)
    # print(visited)
    max_work = max_work * 100
    print(f'#{t}', '%f'% max_work)

if __name__ == '__main__':
    pass