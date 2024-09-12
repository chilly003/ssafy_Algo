import sys
sys.stdin = open('sample_input (4).txt')

#색칠 문제처럼 2차원 리스트에 맞게 파워 값으로 색칠하기
def B_range(BR):
    global B_map, max_charge
    #시작 좌표 및 배터리 정보 
    start_i, start_j, C, P, num = BR

    for i in range(-C, C + 1):
        for j in range(-C + abs(i), C - abs(i) + 1):
            ni, nj = start_j + j, start_i + i
            if 0 <= ni < 10 and 0 <= nj < 10:
                B_map[ni][nj].append(P + num)


def move_and_charge(move_A, move_B, B_map, move_dict, M):
    #0초의 충전
    f_iA = f_jA = 0
    f_iB = f_jB = 9
    cnt_A = [max(B_map[f_iA][f_jA])]
    cnt_B = [max(B_map[f_iB][f_jB])]
    if cnt_A[0] == cnt_B[0]:
        cnt_A[0] = cnt_A[0] // 2
        cnt_B[0] = cnt_B[0] // 2

    #다음 1초부터의 충전
    for i in range(M):
        iA, jA = move_dict[move_A[i]]
        iB, jB = move_dict[move_B[i]]

        f_iA += iA
        f_jA += jA

        f_iB += iB
        f_jB += jB

        chargeA = B_map[f_iA][f_jA]
        chargeB = B_map[f_iB][f_jB]

        #충전기가 '0'빼고 1개면 서로 같은 숫자면 나눠서 넣고 아니면 그대로 넣어라
        if len(chargeA) == 2 and len(chargeB) == 2:
            if chargeA[1] == chargeB[1]:
                cnt_A.append(chargeA[1]//2)
                cnt_B.append(chargeB[1]//2)
            else:
                cnt_A += chargeA
                cnt_B += chargeB

        #충전기가 없으면 건너 뛰어라
        elif len(chargeA) == 1 and len(chargeB) == 1:
            continue

        #충전기가 여러 개 경우
        else:
            #맥스 파워가 같다면 두번째 맥스 파워도 구해라.
            if max(chargeA) == max(chargeB):
                #첫 번째 맥스값 제외한 새로운 리스트
                new_listA = [x for x in chargeA if x != max(chargeB)]
                new_listB = [x for x in chargeB if x != max(chargeA)]

                if max(new_listA) > max(new_listB):
                    cnt_A.append(max(new_listA))
                    cnt_B.append(max(chargeB))

                elif max(new_listA) < max(new_listB):
                    cnt_A.append(max(chargeA))
                    cnt_B.append(max(new_listB))

                #(0,400,300),(0,400,300) 이런경우 아무거나 넣어라
                elif max(new_listA) == max(new_listB):
                    cnt_A.append(max(chargeA))
                    cnt_B.append(max(new_listB))

            #맥스값이 같지 않다면 그대로 넣어줘라
            else:
                cnt_A.append(max(chargeA))
                cnt_B.append(max(chargeB))

    return cnt_A, cnt_B


T = int(input())
for t in range(1, T+1):
    M, A = map(int, input().split())
    move_A = list(map(int, input().split()))
    move_B = list(map(int, input().split()))
    BC = [list(map(int, input().split())) for _ in range(A)]
    #번호 추가(짝수로 나중에 나눌때 나머지값 혼돈 안나게)
    for i in range(len(BC)):
        BC[i].append(i*2)
    #번호에 따른 충전기 딕셔너리
    BC_dict = {}
    for i in BC:
        BC_dict[i[3]+i[4]] = i[4]

    B_map = [[[0] for _ in range(10)] for _ in range(10)]
    move_dict = {0: (0,0), 1: (-1,0), 2:(0,1), 3:(1,0), 4:(0,-1)}

    for BR in BC:
        BR[0] -= 1  #인덱스 수정
        BR[1] -= 1
        B_range(BR)

    cnt_A, cnt_B = move_and_charge(move_A, move_B, B_map, move_dict, M)

    #길이 만큼 돌아서 딕셔너리의 밸류 값을 빼주고 총 값을 구해라
    total = 0
    for i in range(len(cnt_B)):
        if cnt_B[i] == cnt_A[i] and cnt_B[i] != 0:
            total += (cnt_A[i] + cnt_B[i] - BC_dict[cnt_A[i] + cnt_B[i]])

        if cnt_A[i] != 0 and cnt_B[i] != cnt_A[i]:
            total += (cnt_A[i] - BC_dict[cnt_A[i]])

        if cnt_B[i] != 0 and cnt_B[i] != cnt_A[i]:
            total += (cnt_B[i] - BC_dict[cnt_B[i]])

    print(f'#{t} {total}')

if __name__ == '__main__':
    pass