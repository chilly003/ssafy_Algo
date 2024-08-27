import sys
sys.stdin = open('5097_input.txt')
from collections import deque

def solution(t):
    N ,M = map(int, input().split())
    arr = deque(map(int, input().split()))

    for _ in range(M):
        arr_pop = arr.popleft()
        arr.append(arr_pop)


    print(f'#{t} {arr[0]}')

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        solution(t)