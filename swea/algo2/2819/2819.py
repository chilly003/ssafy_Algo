import sys
sys.stdin = open('sample_input.txt')

def sol(lev, text, i, j):
    global set_text

    #종료 조건
    if lev == 7:
        return set_text.add(text)

    #동서남북으로 범위 내에서 돌기
    if 0 <= i + 1 < 4:
        sol(lev + 1, text + str(arr[i+1][j]), i + 1, j)

    if 0 <= j + 1 < 4:
        sol(lev + 1, text + str(arr[i][j+1]), i, j + 1)

    if 0 <= i - 1 < 4:
        sol(lev + 1, text + str(arr[i - 1][j]), i - 1, j)

    if 0 <= j - 1 < 4:
        sol(lev + 1, text + str(arr[i][j-1]), i, j - 1)


T = int(input())
for t in range(1, T+1):
    arr = [list(map(int, input().split())) for _ in range(4)]
    set_text = set()

    for i in range(4):
        for j in range(4):
            sol(0,'', i, j)

    print(f'#{t}', len(set_text))

if __name__ == '__main__':
    pass