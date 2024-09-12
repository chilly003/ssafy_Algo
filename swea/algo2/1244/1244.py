import sys
sys.stdin = open('input.txt')


def recur(N, numbers, time, visited):
    global max_cnt

    #이미 최소값에 넣은 집합이라면 바로 종료
    num_str = ''.join(numbers)
    if (num_str, time) in visited:
        return

    #방문 안한 집합이라면 방문에 넣기
    visited.add((num_str, time))

    #교체 횟수와 같을 때 최댓값 업데이트
    if time == N:
        max_cnt = max(int(num_str), max_cnt)
        return

    #i를 중심으로 탐색
    len_n = len(numbers)
    for i in range(len_n):
        for j in range(i + 1, len_n):
            #바꾸기
            numbers[i], numbers[j] = numbers[j], numbers[i]
            recur(N, numbers, time + 1, visited)
            #원복
            numbers[i], numbers[j] = numbers[j], numbers[i]

            # #이미 최대값을 찾았다면 종료(솔직히 잘 이해안감 그래서 이해하는 걸로 진행)
            # if max_cnt == int(''.join(sorted(numbers, reverse=True))):
            #     return


T = int(input())
for t in range(1, T + 1):
    max_cnt = 0
    number, n = input().split()
    N = int(n)
    numbers = list(number)
    visited = set()  #방문한 상태를 기록하는 집합

    recur(N, numbers, 0, visited)

    print(f'#{t} {max_cnt}')