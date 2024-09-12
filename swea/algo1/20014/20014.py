import sys
sys.stdin = open('4881_input.txt')

def solution(t):
    N = int(input())
    arr = [list(map(int, input().split()))for _ in range(N)]
    min_num = int('inf')

    def recur(row,col,cur_num,perms,N):
        global min_num
        if row == N:
            global min_num
            if cur_num < min_num:
                min_num = cur_num
            return
        # else:
        #     return
        for i in range(N):
            if i not in perms:
                perms.append(i)
                recur(row + 1, col,cur_num+arr[i][j], perms, N)
                perms.pop()

        return min_num

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        print(f'#{t} {solution(t)}')