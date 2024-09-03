import sys
sys.stdin = open('test2.txt')


def solution(t):
    # 아래처럼 플러스 해주는 이유는 마지막 등산로의 값도 구하기 위해서
    # 이렇게 안해주면 이어지는 등산로가 아닌걸로 판단하고 마지막 등산로는
    # 계산들 안한다. 위처럼 if문 반복이 싫다면 값을 더해줘서 검사해주기
    N = int(input()) + 1
    arr = list(map(int, input().split())) + [0]
    max_b = float('inf') #비교값 양수로 크게
    max_len = 0 #정답을 저장할 공간
    start_point = arr[0] #첫 시작 포인트
    length = 1 #최저 길이도 1임

    for i in range(0,N-1): #i+1 값을 검사할 거니까 -1 해줘야함 범위주의
        if arr[i] <= arr[i+1]:
            length += 1
        else:
            if length >= 2:
                slope = (arr[i] - start_point)/length
                if slope < max_b:
                    max_b = slope
                    max_len = length
                elif slope == max_b:
                    if length > max_len:
                        max_len = length
            start_point = arr[i+1] #지점 재설정
            length = 1             #길이 재설정

    return max_len

if __name__ == "__main__":
    T = int(input())
    for t in range(1, T + 1):
        print(f'#{t} {solution(t)}')