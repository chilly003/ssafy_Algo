#다양한 연산자(^제곱 연산 포함), 괄호, 숫자, 2자리 이상에 대한 표현식을 후위표기법으로 바꾸기

#stack 내에서의 연산 우선순위
#괄호의 목적은 연산 순서 명시
#괄호 안의 연산을 먼저 수행해야 하므로 스택 안에서 괄호는 '('는 낮은 우선순위를 갖도록 함.
#모든 연산자가 처리될때까지 괄호 '(' 스택에 남아 있도록 함.
#닫는 괄호를 만났을 때 스택에서 여는 괄호를 만날 때까지 모든 연산자를 꺼내서 쉬움
isp = {'(':0, '+':1, '-':1, '*':2, '/':2, '*':3}
expression = '(335+4) * (42-6^2)/5'

#스택 초기화
top = -1
stack = [0]*len(expression)
postfix = [] #리스트에 후위표기법을 저장함

i = 0
while i < len(expression):
    ch = expression[i]
    #숫자인지파악
    if ch.isdigit():
        tem_num = ch
        #연속된 숫자인지 파악
        for j in range(i+1, len(expression)):
            if expression[j].isdigit():
                tem_num += expression[j]
                i = j #이렇게 설정안해주면 숫자 중복해서 인식
            else:
                break
        postfix.append(tem_num)
    elif ch == '(':
        top += 1
        stack[top] = ch
    elif ch ==')':
        #연산자를 포스트픽스에 넣기
        while top > -1 and stack[top] != '(':
            postfix.append(stack[top])
            top -= 1  #스택안의 여는괄호 제거
        top -= 1
    elif ch in isp:   #연산자인 경우
        #현재 연산자의 우선순위가 스택의 top 연산자의 우선 순위보다 같거나 작은 경우.
        #스택 탑에 있는 연산자를 포스트픽스에 넣기
        while top > -1 and isp[stack[top]] >= isp[ch]:
            postfix.append(stack[top])
            top -= 1
        top += 1
        stack[top] = ch

    i += 1 #인덱스 증가

    #스택에 남아 있는 연산자들 포스트픽스에 추가
while top > -1:
    postfix.append(stack[top])
    top -= 1
print(postfix)