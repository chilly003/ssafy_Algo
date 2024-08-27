import sys
sys.stdin = open('calc_input.txt')

def solution(t):
    income = str(input())
    stack = []
    result = []
    a = ''
    isp = {'+': 1,
           '-': 1,
           '*': 2,
           '/': 2}
    icp = ['+', '-', '*', '/']

    for i in range(len(income)):
        # 피연산자는 결과로 이동
        if income[i] not in icp:
            result.append(income[i])
        # if income[i].isdigit(): 이거 숫자판별

        # 만약 밸류 1인 연산자를 넣을 때
        # 이미 스택 안에 2인 연산자가 있다면
        # 다음 밸류 1인 연산자를 만나거나 스택의 내용이 전부 없어질때까지 팝
        # 마지막으로 검사하고 있던 연산자를 스택에 넣기
        else:
            # 밸류 1인 연산자를 넣었을 때
            if isp[income[i]] < 2:
                if len(stack) == 0:
                    stack.append(income[i])
                elif isp[stack[len(stack) - 1]] >= 2:
                    result.append(stack.pop())
                    stack.append(income[i])

            # 밸류 2안 연산자를 넣었을 때
            elif isp[income[i]] == 2:
                if len(stack) == 0:
                    stack.append(income[i])
                elif isp[stack[len(stack) - 1]] == 2:
                    result.append(stack.pop())
                    stack.append(income[i])
                elif isp[stack[len(stack) - 1]] == 1:
                    stack.append(income[i])

            else:
                stack.append(income[i])

    # 연산식이 끝나면 스택에 있던 모든 연산을 팝해서 결과에 넣기
    for _ in range(len(stack)):
        result.append(stack.pop())

    return a.join(result)

if __name__ == '__main__':
    T = int(input())
    for t in range(1,T+1):
        print(f'#{t} {solution(t)}')