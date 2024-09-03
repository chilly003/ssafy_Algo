# 암호생성기
import sys
from collections import deque
sys.stdin = open('input (7).txt')

def solution(t):
    num = int(input())
    arr = deque(map(int, input().split()))

    #사이클 함수
    def cycle(arr):
        for i in range(1, 6):
            pop_arr = arr.popleft() - i
            if pop_arr > 0:
                arr.append(pop_arr)
            else:
                arr.append(0)
                break
        return arr

    #arr에 0이 나올때까지 돌리기
    while True:
        if 0 not in arr:
            cycle(arr)
        elif 0 in arr:
            break

    print(f'#{t}', end=" ")
    print(*arr)



if __name__ == "__main__":
    T = 10
    for t in range(1, T+1):
        solution(t)