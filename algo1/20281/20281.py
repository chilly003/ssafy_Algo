import sys
sys.stdin = open('bit_input.txt')

def solution(t):
    code = {
        '001101': 0,
        '010011': 1,
        '111011': 2,
        '110001': 3,
        '100011': 4,
        '110111': 5,
        '001011': 6,
        '111101': 7,
        '011001': 8,
        '101111': 9
    }

    num = input().strip()
    a = []
    #16진수 10진수로 바꾸기
    for i in num:
        b = (int(i, 16))
        a.append(bin(b)[2:])

    # 10진수를 2진수로 바꾼다.
    # 단 그냥 바꾸면 4자리로 안나오니 필요한 4자리가 되게 필요한 만큼의 0을 앞에 붙여준다.
    for i in range(len(a)):
        if len(a[i]) < 4:
            a[i] = '0' * (4 - len(a[i])) + a[i]

    c = ''.join(a)

    #암호비트패턴을 사용할 수 있는 인덱스 번호 알기
    idx = 0
    for i in range(len(c)):
        if c[i:i+6] in code:
            break
        else:
            idx += 1

    end = len(c)
    result = []
    for e in range(idx, end - idx, 6):
        result.append(code[c[e:e+6]])
        # print(code[c[e:e+6]])

    return result

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        print(f'#{t}', *solution(t))