import sys
sys.stdin = open('input (3).txt')

def recur(cnt, total):
    global ans

    #가지치기 먼저
    if total >= B :
        ans = min(ans, total)
        return

    if cnt == N:
        return

    recur(cnt + 1, total + heights[cnt])
    recur(cnt + 1, total)

T  = int(input())
for t in range(1, T+1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    ans = 1e9   #탑의 최대 높이
    recur(0,0)

    print(f'#{t} {ans - B}')

if __name__ == '__main__':
    pass