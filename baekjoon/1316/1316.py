import sys
sys.stdin = open('test.txt')


T = int(input())
for _ in range(1, T+1):
    N = int(input())
    cnt = 0
    for _ in range(N):
        word = str(input())
        abc_dict = {}
        for i in word:
            abc_dict[i] = 0


        check = True
        for i in range(len(word)):
            if i != 0 and abc_dict[word[i]] == 1:
                if word[i] != word[i-1]:
                    check = False
                    break
            else:
                abc_dict[word[i]] += 1

        if check:
            cnt += 1

    print(cnt)


if __name__ == '__main__':
    pass