import sys
sys.stdin = open('5201_input.txt')

def sol():
    N, M = map(int, input().split())
    N_arr = list(map(int, input().split()))
    M_arr = list(map(int, input().split()))

    #오름차순으로 정렬해서 마지막 무게만 보게하기
    N_arr.sort()
    M_arr.sort()

    result = []
    #인덱스 확인
    idx_N = N - 1

    #while 쓸때 주의, M_arr과 idx_N 둘 중 하나라도 0이 나오면 종료.
    #그래서 or이 아닌 and를 씀.
    while M_arr and idx_N > -1:
        if M_arr[-1] >= N_arr[idx_N]:       #제일 큰 용량에 큰 무게가 담기는지 확인
            result.append(N_arr[idx_N])     #담기면 어펜드
            N_arr[idx_N] = float('inf')     #그리고 다시는 못 담게 무한으로 바꿔주기
            M_arr.pop()                     #사용한 트럭은 제외
            idx_N -= 1                      #인덱스 줄여주기

        elif M_arr[-1] < N_arr[idx_N]:      #만약 안담기는 무게면 인덱스만 줄여주기
            idx_N -= 1


    return sum(result)

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        print(f'#{t} {sol()}')
