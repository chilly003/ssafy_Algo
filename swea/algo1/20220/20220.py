import sys
sys.stdin = open ('tree_input.txt')

def pre(start, left, right):
    if start:
        print(start, end=' ')
        pre(left[start], left, right)
        pre(right[start], left, right)

def solution():
    N = int(input())
    E = N-1
    arr = list(map(int, input().split()))

    left = [0] * (N+1)
    right = [0] * (N+1)
    root = [0] * (N+1)

    for i in range(E):
        p, c = arr[i*2], arr[i*2+1]

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        root[c] = p

    c = N

    while root[c] != 0:
        c = root[c]

    start = c

    pre(start, left, right)

if __name__ == '__main__':
    solution()

