#새로운 코드
import sys
sys.stdin = open('test.txt')
from collections import Counter

def solution(t):
    N, M, K = map(int, input().split())
    people = sorted(list(map(int, input().split())))
    people_count = Counter(people)
    fish = 0
    max_time = len(people)

    for i in range(max_time):
        if people[i]:
            fish += K
        if i in people_count:
            fish -= people_count[i]
        if fish < 0:
            print(f'#{t} Impossible')
            return

    print(f'#{t} Possible')

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T+1):
        solution(t)