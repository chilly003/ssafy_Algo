import sys
sys.stdin = open('5203_input.txt')

#연속되는 자리수가 있는지 확인하는 함수
def find_ctu(visited1, visited2):
    cnt1 = 0
    cnt2 = 0
    #계속 if를 써야해서 좀 별로다.
    for j in range(10):
        if visited1[j] != 0:
            cnt1 += 1
        if visited2[j] != 0:
            cnt2 += 1
        #만약 연속되는 숫자가 3개 이상 있으면 바로 리턴
        if cnt1 >= 3:
            return 1
        if cnt2 >= 3:
            return 2
        if visited1[j] == 0:
            cnt1 = 0
        if visited2[j] == 0:
            cnt2 = 0

    return 0


def sol():
    card = list(map(int, input().split()))

    player1 = []
    player2 = []

    #연속된 숫자, 중복 숫자 찾기 위한 visited
    visited1 = [0] * 10
    visited2 = [0] * 10

    for i in range(0,12,2):
        player1.append(card[i])
        visited1[card[i]] += 1
        player2.append(card[i+1])
        visited2[card[i+1]] += 1

        #정답 나오자 마자 종료를 위해 업데이트마다 정렬해준다.
        player1.sort()
        player2.sort()

        if i >= 6:
            result = find_ctu(visited1, visited2)
            if 3 in visited1 or result == 1:
                return 1


            elif 3 in visited2 or result == 2:
                return 2

    return 0

if __name__ == '__main__':
    T = int(input())
    for t in range(1, T + 1):
        print(f'#{t} {sol()}')