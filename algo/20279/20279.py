def solution():
    #비효율그잡체 코드
    num = '01D06079861D79F99F'
    #먼저 16진수를 10진수로 바꾼다.
    a = []
    for i in num:
        b = (int(i, 16))
        a.append(bin(b)[2:])

    # print(a)
    #10진수를 2진수로 바꾼다.
    #단 그냥 바꾸면 4자리로 안나오니 필요한 4자리가 되게 필요한 만큼의 0을 앞에 붙여준다.
    for i in range(len(a)):
        if len(a[i]) < 4:
            a[i] = '0' * (4-len(a[i])) + a[i]

    # print(a)

    c = ''.join(a)

    #7씩 슬라이싱해서 다시 10진수로 바꾼다.
    d = []
    for i in range(0,len(c),7):
        # print(i)
        d.append(int(c[i:i+7], 2))

    return d

if __name__ == '__main__':
    print(f'#1', *solution())