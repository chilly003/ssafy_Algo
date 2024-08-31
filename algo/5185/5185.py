import sys
sys.stdin = open('./5185_input.txt')


def solution():
    hex_dict = {
        '0': '0000','1': '0001','2': '0010','3': '0011','4': '0100','5': '0101','6': '0110',
        '7': '0111','8': '1000','9': '1001','A': '1010','B': '1011','C': '1100','D': '1101',
        'E': '1110','F': '1111'
    }
    N, hex_N = map(str, input().split())

    ##방법 1
    # result = []
    # for i in range(int(N)):
    #     result.append(bin(int(hex_N[i], 16))[2:])
    # for i in range(len(result)):
    #     if len(result[i]) < 4:
    #         result[i] = '0' * (4 - len(result[i])) + result[i]
    # out = ''
    # for i in range(len(result)):
    #     out += result[i]

    ##방법 2
    out = ''
    for i in range(int(N)):
        out += hex_dict[hex_N[i]]

    return out

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        print(f'#{t} {solution()}')