import sys
sys.stdin = open ('1231.txt')

def pre(start, left, right, abc_dict, a):
    if start:
        pre(left[start], left, right, abc_dict, a)
        a += abc_dict[start]
        pre(right[start], left, right, abc_dict, a)

def solution(t):
    N = int(input())
    arr = [list(map(str, input().split())) for _ in range(N)]
    abc_dict = {}
    new_arr = []

    left = [0] * (N+1)
    right = [0] * (N+1)
    root = [0] * (N+1)

    #문자 딕셔너리
    for i in range(N):
        abc_dict[int(arr[i][0])] = arr[i][1]

    #좌표 값 새로 만들기
    for i in range(N):
        if len(arr[i]) > 2:
            for j in range(2, len(arr[i])):
                new_arr.append([arr[i][0], arr[i][j]])

    #각 좌표 오른쪽 왼쪽 자식, 부모 확인
    for i in range(len(new_arr)):
        p, c = int(new_arr[i][0]), int(new_arr[i][1])

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        root[c] = p

    #어처피 끝값에서 올려야 하니까 이거 안해도 되는 줄 알았는데 아닌가봄
    #왜그런거지?
    c = N
    while root[c] != 0:
        c = root[c]

    start = c
    a = []
    pre(start, left, right, abc_dict, a)
    print(f'#{t} {"".join(a)}')

if __name__ == '__main__':
    T = 10
    for t in range(1,T+1):
        solution(t)

