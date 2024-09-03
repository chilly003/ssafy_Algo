import sys
sys.stdin = open('./input.txt')

def solution(t):
    arr = [list(map(int, input().split()))for _ in range(9)]

    #행 비교
    for i in range(9):
        srow_arr = sorted(arr[i])
        for j in range(9):
            if srow_arr[j] != j+1:
                return 0

    # 열 비교
    for j in range(9):
        scol_arr = [arr[i][j] for i in range(9)]
        if scol_arr[i] != i+1:
            return 0

    # 박스 비교
    # for i in range(0,len(arr),)

    print(f'#{t} {arr}')


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        solution(t)