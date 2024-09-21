from collections import deque

def solution(priorities, location):
    stack = deque([])
    #일의 우선순위와 위치를 새로운 큐에 저장
    for i in range(len(priorities)):
        stack.append([priorities[i],i])

    cnt = 0
    #없어질때까지 탐색
    while stack:
        current = stack.popleft()
        #리스트 내의 조건을 확인하는 과정
        #만약 현재 우선순위보다 큰 우선순위가 있다면 다시 스택에 어팬드
        if any(current[0] < q[0] for q in stack):
            stack.append(current)
        #아니라면 카운트 올려주고 동시에 내가 찾고 있는 위치의 요소와 같다면 바로 종료
        else:
            cnt += 1
            if current[1] == location:
                return cnt


if __name__ == '__main__':
    priorities = [1, 1, 9, 1, 1, 1]
    location = 0
    print(solution(priorities, location))