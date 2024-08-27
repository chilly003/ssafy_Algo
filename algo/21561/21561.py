import sys
sys.stdin = open('./sample_input.txt')

def solution(t):
    N, M = map(int, input().split())
    #문자를 엔터 기준으로 받기 때문에 list map 필요없이 그냥 받으면 된다.
    arr = [input() for _ in range(N)]
    #이제 세로로 된 문자 입력해야함.
    cul_arr = []
    #문제 잘 읽기 정사각형임
    for j in range(0, N):
        #중간에 세로 문자를 담을 빈 단어장 만들어주기
        temp_str = ''
        for i in range(0, N):
            #세로로 된 문자만 받고 받고 반복
            temp_str += arr[i][j]
        #보석함에 저장^^
        cul_arr.append(temp_str)
    return cul_arr


if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        print(f'#{t} {solution(t)}')