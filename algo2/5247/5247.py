import sys
sys.stdin = open('5247_input.txt')

def find_min(num, cnt):
    global min_count
    if num < 1:
        return

    if num >= 1000000:
        return

    if num == M:
        min_count = min(min_count, cnt)
        return

    find_min(num + 1, cnt + 1)
    find_min(num - 1, cnt + 1)
    find_min(num * 2, cnt + 1)
    find_min(num - 10, cnt + 1)

T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())

    min_count = -1e9
    find_min(N, 0)

    print(min_count)

if __name__ == "__main__":
    pass