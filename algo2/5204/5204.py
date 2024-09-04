import sys
sys.stdin = open('5204_input.txt')


def merge_sort(arr, N, cnt):
    if len(arr) == 1:
        return arr , cnt

    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    left, cnt = merge_sort(left, N, cnt)
    right, cnt = merge_sort(right, N, cnt)

    return merge(left, right, cnt)

def merge(left, right, cnt):
    result = [0] * (len(left) + len(right))
    l = r = 0

    if left[-1] > right[-1]:
        cnt += 1

    #인덱스가 길이 범위 밖으로 나가면 종료
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result[l+r] = left[l]
            l += 1

        else:
            result[l+r] = right[r]
            r += 1

    #남아있는 것들을 그냥 리설트에 넣고 인덱스 추가
    # result.extend(left[l:])
    # result.extend(right[r:])
    while l < len(left):
        result[l + r] = left[l]
        l += 1

    while r < len(right):
        result[l + r] = right[r]
        r += 1

    return [result, cnt]

def sol():
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0
    result = merge_sort(arr, N, cnt)

    return result[0][N//2], result[1]

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        print(f'#{t}', *sol())