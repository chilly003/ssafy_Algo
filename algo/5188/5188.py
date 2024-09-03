import sys
sys.stdin = open('5188_input.txt')

def solution(t):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    min_num = [float('inf')]
    num = []

    def find_min(N, arr, row, col, num, min_num):
        if sum(num) > min_num[0]:
            return

        if row == N-1 and col == N-1:
            num.append(arr[row][col])
            if sum(num) < min_num[0]:
                min_num[0] = sum(num)
            num.pop()
            return min_num

        if row + 1 < N:
            num.append(arr[row][col])
            find_min(N, arr, row+1, col, num, min_num)
            num.pop()

        if col + 1 < N:
            num.append(arr[row][col])
            find_min(N, arr, row, col + 1, num, min_num)
            num.pop()

    find_min(N, arr, 0, 0, num, min_num)
    print(f'#{t} {min_num[0]}')
    # print(num)

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        solution(t)