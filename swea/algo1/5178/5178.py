import sys
sys.stdin = open('5178_input.txt')

def solution():
    N, M, L = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]

    #트리 딕셔너리
    tree_dict = {}
    for i in range(1, N + 1):
        tree_dict[i] = 0

    #그 딕셔너리 키값이 있는 arr 밸류로 저장
    for i in range(M):
        tree_dict[arr[i][0]] = arr[i][1]

    #순회 하면서 밸류 없는 딕셔너리 값 저장
    for i in range(N, 0, -1):
        if tree_dict[i] == 0:
            tree_dict[i] = tree_dict[i * 2]
            #여기가 좀 거시기함. 할때마다 검사해줘야함.
            #따로 뺄 수 있을거 같지만 귀찬
            if i * 2 + 1 <= N:
                tree_dict[i] += tree_dict[i * 2 + 1]

    return tree_dict[L]

    # return tree_dict

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        print(f'#{t} {solution()}')