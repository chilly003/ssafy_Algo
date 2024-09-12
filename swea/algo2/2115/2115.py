import sys
sys.stdin = open('sample_input (1).txt')

def sol(lev, total):
    global max_profit

    #종료 조건 모든 일꾼이 일을 끝냈을 때
    if lev == 2:
        max_profit = max(max_profit, total)
        return

    for i in range(N):
        for j in range(N):
            if visited[i][j:j+M]:
                continue
            visited[i][j:j+M] = True * M
            #조합 함수를 따로 뺀다.
            profit = find_max(arr[i][j:j+M])
            sol(lev + 1, total+ profit)
            visited[i][j:j+M] = False * M


#조합함수로 담을 수 있는 최대 수가 뭔지 구하기
def find_max(find):
    if sum(find) <= C:
        return sum(find)



T = int(input())
for t in range(1, T+1):
    N, M, C = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False]*N]*N
    max_profit = 0

    #벌통 개수를 생각해서 움직이기
    for i in range(N):
        for j in range(N-M+1):
            sol(0, 0)


    print(f'#{t} {max_profit}')
if __name__ == '__main__':
    pass