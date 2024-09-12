import sys
sys.stdin = open('2477.txt')

def solution():
    melon = int(input())
    x_y = [list(map(int,input().split())) for _ in range(6)]
    return print(x_y)

if __name__ == '__main__':
    solution()
