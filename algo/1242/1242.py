import sys
sys.stdin = open('sample_input.txt')

def solution():
    N, M = map(int, input().split())
    arr = [list(input().split()) for _ in range(N)]
    code_dict = {'0001101': 0, '0011001': 1, '0010011': 2, '0111101': 3, '0100011': 4,
                 '0110001': 5, '0101111': 6, '0111011': 7, '0110111': 8, '0001011': 9}

    #중복된 열은 빼고 저장해줘
    find_code = []
    for i in range(len(arr)-1):
        if arr[i] == arr[i+1]:
            pass
        else:
            find_code.append(arr[i])

    #0을 제외한 코드는 뭐야?
    code = []
    for i in find_code:
        code.append(i[0].strip('0'))

    #만약 요소중에 0이 있다면 그 0을 기준으로 요소 2개로 나눠줘!
    real_code = []
    for i in code:
        if '0' in i:
            # for j in range(len(i)):
            #     if i[j] == 0:
            #         pass #여기를 만약 0이 나오면 그 전까지 있던 요소 저장, 0 끝나면 그 후에 저장 해야함
            real_code.append(''.join(i.split('0')))
        else:
            real_code.append(i)

    #먼저 16진수를 10진수로 바꾸고 2진수로 다시 바뀐다.
    depalce_2 = []
    for i in range(1, len(real_code)):
        depalce_2.append(bin(int(real_code[i], 16))[2:])

    #부족한 자리 만큼 앞에 0을 채워줘라
    for i in range(len(depalce_2)):
        if len(depalce_2[i]) < 4:
            depalce_2[i] = '0' * (4-len(depalce_2[i])) + a[i]

    find_spycode = ''.join(depalce_2)

    #어디서부터 시작해야하는지 찾아줘라
    idx = 0
    for i in range(len(find_spycode)):
        if find_spycode[i:i+7] in code_dict:
            break
        else:
            idx += 1

    end = len(find_spycode)
    result = []
    #각 자리에 맞는 딕셔너리 밸류값 찾기
    for e in range(idx, end - idx, 7):
        result.append(code_dict[find_spycode[e:e+7]])

    return result

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T+1):
        print(f'#1', solution())