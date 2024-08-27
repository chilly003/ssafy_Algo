# 파일 입력을 시스템 입력으로
import sys
sys.stdin = open('./GNS_test_input.txt')

def solution():
    N , M = map(str, input().split())
    #이번건 문자라 문자로 재정렬 해줘야한다~!
    #str 클래스의 멤버함수라 단독으로 못쓰니 꼭 맵으로 str해주시길
    arr = [list(map(str, input().split()))]
    num_list = []

    #처음 받은arr은 이중으로 둘러싸여 있기에 이중for문 쓰기
    for i in arr:
        for j in i:
            #새로운 리스트 안에 어팬드 해야 추가 된다.
            #이거 모르고 계속 +=이거 씀;
            if j == 'ZRO':
                num_list.append(0)
            if j == 'ONE':
                num_list.append(1)
            if j == 'TWO':
                num_list.append(2)
            if j == 'THR':
                num_list.append(3)
            if j == 'FOR':
                num_list.append(4)
            if j == 'FIV':
                num_list.append(5)
            if j == 'SIX':
                num_list.append(6)
            if j == 'SVN':
                num_list.append(7)
            if j == 'EGT':
                num_list.append(8)
            if j == 'NIN':
                num_list.append(9)

    #새롭게 정렬한 것을 대입, .sort 써도 ㄱㅊ지만 그럼 딕셔너리도 맞게 변경해야함 패스~
    s_num_list = sorted(num_list)

    #이제 키값에 맞게 새로운 딕셔너리 만들고
    str_dict = {0:'ZRO',1:'ONE',2:'TWO',3:'THR',4:'FOR',5:'FIV',6:'SIX',7:'SVN',8:'EGT',9:'NIN'}
    f_list = []
    #키값에 맞게 밸류값 어팬드
    for k in s_num_list:
        f_list.append(str_dict[k])

    print(N) #번호 출력
    for num in f_list:
        print(num, end=' ') #for문으로 출력해야지 ''이거 없이 나옴 연속 출력
    print() # 이거 안하면 뭉쳐서 나옴 엔터 기준으로 나눠서 모든 케이스 출력하게 해줌


if __name__ == "__main__":
    T = int(input())
    for _ in range(1, T+1):
        solution()