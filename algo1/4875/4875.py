import sys
sys.stdin = open('4875_input.txt')

def solution(t):
    N = int(input())
    miro = [list(map(int, input()))for _ in range(N)]

    # def fstart(N):
    #     for i in range(N):
    #         for j in range(N):
    #             if miro[i][j] ==2 :
    #                 return i, j
    # return -1, 1
    #
    # sti, stj = fstasrt(N)


if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        solution(t)