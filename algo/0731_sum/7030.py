import sys
sys.stdin = open('./sum_input.txt')

def solution(t):

    #테스트 케이스 번호로 사용해도 ㄱㅊ 안해도 ㄱㅊ
    dump = int(input())
    #100*100의 모양을 만들고 거기에 인풋 넣기
    arr = [list(map(int, input().split()))for _ in range(100)]

    max_sum = 0
    # 행 우선
    for i in range(100):
        row_sum = sum(arr[i])
        if row_sum > max_sum:
            max_sum = row_sum

    #열 우선
    for j in range(100):
        col_sum = sum(arr[i][j] for i in range(100))
        if col_sum >max_sum:
            max_sum = col_sum

    #대각선
    left_sum = sum(arr[i][i] for i in range(100))
    if left_sum > max_sum:
        max_sum = left_sum

    #대각선 2
    right_sum = sum(arr[i][99-i] for i in range(100))
    if right_sum > max_sum:
        max_sum = right_sum


    print(f'#{t} {max_sum}')


if __name__ == "__main__":
    T = 10
    for t in range(1, 11):
        solution(t)

