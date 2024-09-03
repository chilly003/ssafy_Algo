import sys
sys.stdin = open('input (2).txt')

#계산 함수
def caculate(a):
    len_a = len(a)
    temp = []

    for i in range(len_a):
        if a[i].isdigit():
            temp.append(a[i])
        else:
            if a[i] == '+':
                tmep_pop1 = int(temp.pop())
                tmep_pop2 = int(temp.pop())
                temp.append(tmep_pop2+tmep_pop1)
            elif a[i] == '-':
                tmep_pop1 = int(temp.pop())
                tmep_pop2 = int(temp.pop())
                temp.append(tmep_pop2-tmep_pop1)
            elif a[i] == '/':
                tmep_pop1 = int(temp.pop())
                tmep_pop2 = int(temp.pop())
                temp.append(tmep_pop2//tmep_pop1)
            else:
                tmep_pop1 = int(temp.pop())
                tmep_pop2 = int(temp.pop())
                temp.append(tmep_pop2*tmep_pop1)
    return temp[0]

#후위 순회
def pre(start, left, right, a, arr_dict):
    if start:
        pre(left[start], left, right, a, arr_dict)
        pre(right[start], left, right, a, arr_dict)
        a.append(arr_dict[start])


def solution():
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]

    #각 노드 좌표에 어떤 값이 들어 갔는지 딕셔너리로 저장
    arr_dict = {}
    for i in range(N):
        arr_dict[i+1] = arr[i][1]

    left = [0] * (N + 1)
    right = [0] * (N + 1)
    roots = [0] * (N + 1)

    #부모 자식 좌표
    new_arr = []
    for i in range(N):
        if len(arr[i]) > 2:
            for j in range(2, len(arr[i])):
                new_arr.append([arr[i][0], arr[i][j]])

    #저장한 부모 자식 좌표로 왼,오 자리 저장하기
    for i in range(len(new_arr)):
        p, c = int(new_arr[i][0]), int(new_arr[i][1])

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c
        roots[c] = p

    #a는 후위로 저장한 각 노드의 값임
    start = 1
    a = []
    pre(start, left, right, a, arr_dict)

    return caculate(a)

if __name__ == '__main__':
    for t in range(1, 11):
        print(f'#{t} {solution()}')
