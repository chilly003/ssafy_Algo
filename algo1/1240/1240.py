import sys
sys.stdin = open('input (3).txt')

def solution(t):
    #세로, 가로
    N, M = map(int, input().split())
    arr = [list(map(int,input())) for _ in range(N)]
    #코드 찾는 딕셔너리
    code_dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
                 '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

    new_arr = []

    #새로운 리스트 만들기
    for i in range(len(arr)):
        if 1 in arr[i]:
            new_arr.append(arr[i])

    #끝지점은 항상 1로 끝나니깐 이걸 기준으로 종료되는 지점 알기
    end = M - 1
    for j in range(M-1, -1, -1):
        if new_arr[0][j] != 0:
            break
        else:
            end -= 1

    #코드는 56자 라는 것을 알기에 그만큼 뒤로 가면 시작 지점이 나온다.
    start = end - 55
    spy_code = []
    #리스트에 담겨있는 코드들 join으로 받아서 문자로 바꿔주기
    #사실 이렇게 안하고 그냥 딕셔너리를 진수로 바꿔서 바로 받는 방법도 있지만 일단 그냥 해보기
    for i in range(start, end, 7):
        a = "".join([str(n) for n in new_arr[0][i:i+7]])
        spy_code.append(code_dict[a])

    #홀수, 짝수 자리에 있는 것들 더하기
    hol = 0
    cchack = 0
    for i in range(len(spy_code)//2):
        hol += int(spy_code[i * 2])
        cchack += int(spy_code[i * 2 + 1])

    #조건에 맞으면 홀짝 더한거, 안맞으면 0출력
    if (hol*3 + cchack) % 10 == 0:
        print(f'#{t} {hol + cchack}')
    else:
        print(f'#{t} 0')


if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        solution(t)