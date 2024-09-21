def solution(s):
    answer = True
    temp = []
    for i in s:
        #여는 괄호면 넣어주기
        if i == '(':
            temp.append(i)
        #닫는 괄호가 나오면
        elif i == ')':
            #temp에 여는 괄호가 있으면 체크
            if temp:
                check = temp.pop()
                if check != '(':
                    answer = False
                    break
            #아니라면 바로 틀린답
            else:
                answer = False
                break
    #만약 temp에 뭐가 남아있으면 틀림
    if temp:
        answer = False

    return answer

if __name__ == '__main__':
    s = "(()("
    print(solution(s))