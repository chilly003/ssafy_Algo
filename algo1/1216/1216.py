import sys
sys.stdin = open('input.txt')

def solution(t):
    N = int(input())
    arr = [input() for _ in range(100)] # 행
    max_len = 0                         # 비교값
    cul_arr = []
    # 열만 들어간 숫자 모임 만들기
    # zip으로 만들 수 있는데 잘 모르겠음;;
    for j in range(0,100):
        temp_str = ''
        for i in range(0,100):
            temp_str += arr[i][j]
        cul_arr.append(temp_str)

    # 각 구간이 만약 회문이라면 그 길이를 보고
    # 그 길이가 맥스보다 크다면 다시 업데이트
    # 근데 이렇게 하면 너무너무 오래걸림
    for i in range(100):
        for j in range(100):
            for k in range(100):
                if j + k < 101:
                    temp_arr = arr[i][j:j + k]
                    if temp_arr == temp_arr[len(temp_arr)-1::-1]:
                        if len(temp_arr) > max_len:
                            max_len = len(temp_arr)

    for i in range(100):
        for j in range(100):
            for k in range(100):
                if j + k < 101:
                    temp_arr = cul_arr[i][j:j + k]
                    if temp_arr == temp_arr[len(temp_arr)-1::-1]:
                        if len(temp_arr) > max_len:
                            max_len = len(temp_arr)

    return max_len


if __name__ == "__main__":
    T = 10
    for t in range(1, T + 1):
        print(f'#{t} {solution(t)}')

