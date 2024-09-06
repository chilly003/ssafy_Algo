import sys
sys.stdin = open('sample_input (4).txt')

def sol():
    pass


T = int(input())
for t in range(1, T+1):
    M, A = map(int, input().split())
    move_A = list(map(int, input().split()))
    move_B = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(A)]
    B_map = [[0]*10]*10
    move_dict = {0: (0,0), 1: (1,0), 2:(0,1), 3:(-1,0), 4:(0,-1)}

    print(BC, B_map)

    #이제 지도에 배터리에 해당되는 구역에 색칠해주고 비교 찾기만 하기


if __name__ == '__main__':
    pass