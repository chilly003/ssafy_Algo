import sys
sys.stdin = open('./4835_input (1).txt')

def solution(i):
    # N, M = map(int, input().split())
    # arr = list(map(int, input().split()))
    #
    # max_sum = sum(arr[0:M])
    # min_sum = sum(arr[0:M])
    #
    # for k in range(1, N-M+1):
    #     temp_sum = sum(arr[k:k+M])
    #     if temp_sum > max_sum:
    #         max_sum = temp_sum
    #     elif temp_sum < min_sum:
    #         min_sum = temp_sum
    #
    # print(f"#{i} {max_sum - min_sum}")


    N, M = map(int,input().split())
    arr = list(map(int, input().split()))

    max_s = sum(arr[0:M])
    min_s = sum(arr[0:M])

    for k in range(1, N-M+1):
        temp = sum(arr[k:k+M])
        if temp > max_s:
            max_s = temp
        elif temp < min_s:
            min_s = temp

    print(f'#{i} {max_s - min_s}')

if __name__ == "__main__":
    T = int(input())
    for i in range(1,T+1):
        solution(i)