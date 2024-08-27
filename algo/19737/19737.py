import sys
sys.stdin = open('./4864_input.txt')

def solution(t):

    str1 = str(input())
    str2 = str(input())

    for i in range(len(str2)):
        if str2[i] == str1[0]:
            a = str2[i:i+len(str1)]
            if a == str1:
                return 1
    return 0

if __name__ == "__main__":
    T = int(input())
    for t in range(1,T+1):
        print(f'#{t} {solution(t)}')