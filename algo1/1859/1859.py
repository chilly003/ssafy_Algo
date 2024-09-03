#원재의 사재기
import sys
sys.stdin = open('input (1).txt')


def solution(t):
    N = int(input())
    arr = list(map(int, input().split()))
    max_profit = 0

    for i in range(N-1):
        buy = i + 1 #구매 개수
        sale = arr[i+1] #판매가
        #인덱스 범위 내에서 움직이게 바꾸기
        profit = (sale*buy) - sum(arr[0:i+1]) #판매 - 구매
        if profit > max_profit:
            max_profit = profit

    return max_profit


if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        print(f'#{t} {solution(t)}')