import sys
sys.stdin = open('text.txt')

def island_num(i, j):
    stack = [(i, j)]
    temp = []
    # 뭉쳐있는 섬들을 모두 찾을 때까지
    while stack:
        x, y = stack.pop()
        if (x, y) not in temp:
            temp.append((x, y))
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx, ny = x + dx, y + dy
                if 0 <= nx < N and 0 <= ny < M and map_arr[nx][ny] == 1:
                    stack.append((nx, ny))

    return temp


def make_bridge(i, j, num):
    global cost_dict, connect

    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = i + dx, j + dy
        cnt = 0
        #범위 내에 있으며 만난 숫자가 자기 자신이 아닐때
        while 0 <= nx < N and 0 <= ny < M:
            if map_arr[nx][ny] == num:
                break
            #다른 섬을 만났고 다리의 거리가 2이상일 때
            if map_arr[nx][ny] and cnt > 1:
                #거리 딕셔너리에 있는 값 보다 적다면 업데이트
                if cost_dict[(map_arr[nx][ny], num)] > cnt:
                    cost_dict[(map_arr[nx][ny], num)] = cnt
                    cost_dict[(num, map_arr[nx][ny])] = cnt
                    #섬 연결을 확인위해 업데이트
                    connect.update(str(num))
                    connect.update(str(map_arr[nx][ny]))
            #다른 섬은 맞는데 거리가 1이하이면 종료
            elif map_arr[nx][ny] and cnt <= 1:
                break

            cnt += 1
            nx += dx
            ny += dy


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    map_arr = [list(map(int, input().split())) for _ in range(N)]

    arr_idx = []
    visited = set()

    # 1. 섬(1이 뭉쳐있는 경우)을 찾고 그 섬의 인덱스를 리스트에 담기.
    for i in range(N):
        for j in range(M):
            if map_arr[i][j] == 1 and (i, j) not in visited:
                island = island_num(i, j)
                arr_idx.append(island)
                # 리스트에 리스트를 업데이트 하면 중복되었지만 순서만 다른 경우가 업데이트된다.
                # set으로 중복 제거
                visited.update(island)

    # 2. 섬 색칠
    color = 1
    for i in arr_idx:
        for j in i:
            map_arr[j[0]][j[1]] = color
        color += 1

    # 3. 다리 만들기
    cost_dict = {}      #방향에 따라 비용 정리.
    for i in range(1, color):
        for j in range(1, color):
            if i < j:
                cost_dict[(i, j)] = 1e9   #다리가 어디서부터 시작인지 모름 그러니 두개 전부 저장
                cost_dict[(j, i)] = 1e9
    # print(cost_dict)

    connect = set()     #섬연결을 알기위한 셋
    #이렇게 안하고 arr_idx로 불러와도 ㄱㅊ 지금 바쁘니까 생략
    for i in range(N):
        for j in range(M):
            if map_arr[i][j] != 0:
                make_bridge(i, j, map_arr[i][j])


    print(map_arr)
    print(connect)
    print(cost_dict)

if __name__ == '__main__':
    pass