import sys
sys.stdin = open('input (3).txt')

def solution(t):
    N = 4
    result = [[1], [1, 1]]
    if N == 1:
        result = 1
    if N == 2:
        return result

    stack1 = [1 ,1]
    for _ in range(N-2):

        for i in range(len(stack1)-1):
            stack2 = []
            plus = stack1[i]+stack1[i+1]
            stack2.append(plus)

        stack1 = [1] + stack2 + [1]
            #
            # for _ in range(len(stack1)-1):
            #     stack1.pop()
            #
            # stack1.append(stack2)
            # stack1.append(1)
            # result.append(stack1)

    return result


if __name__ == '__main__':
    T = 1
    for t in range(1, T + 1):
        print(f'#{t} {solution(t)}')