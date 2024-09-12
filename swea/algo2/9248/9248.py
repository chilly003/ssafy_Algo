import sys
sys.stdin = open('s_input.txt')

def sol():
    N = int(input())
    arr = list(map(int, input().split()))

    result = 'YES'
    while arr:
        arr_fake = arr
        i = min(arr)
        x = max(arr)
        #중복 검사 필요한데...
        if len(set(arr_fake)) == 1:
            break
        if arr.count(i) > 1 or arr.count(x) > 1:
            result = 'NO'
            break
        elif len(arr) > 1 and arr.count(i) == 1 and arr.count(x) == 1:
            arr.remove(i)
            arr.remove(x)

    return result

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        print(f'#{t} {sol()}')