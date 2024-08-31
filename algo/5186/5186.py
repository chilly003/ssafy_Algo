import sys
sys.stdin = open('./5186_input.txt', 'r')

def solution():
    N = float(input())
    
    result = ''

    #0이 되면 멈추기
    while N != 0:
        N *= 2
        #만약 1보다 같거나 크면 2진수 사용표시, 1빼기
        if N >= 1:
            result += '1'
            N -= 1
        #아니라면 2진수 미사용 표시
        else:
            result += '0'

    if len(result) >= 13:
        return 'overflow'
    else:
        return result

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        print(f'#{t} {solution()}')