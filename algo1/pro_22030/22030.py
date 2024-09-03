def solution():

    enroll = ["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"]
    referral = ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"]
    #인롤하고 리퍼럴 관계 부모 자식
    seller = ["young", "john", "tod", "emily", "mary"]
    amount = [12, 4, 2, 5, 10]
    N = len(enroll)

    #판매한 사람, 판매 개수
    seller_dict = {}
    for i in range(len(seller)):
        seller_dict[seller[i]] = amount[i]

    #이익 담을 곳
    profit_dict = {}
    for i in range(N):
        profit_dict[enroll[i]] = 0

    #부모 자식 관계 만들기
    root_child = []
    for i in range(N):
        root_child.append([referral[i], enroll[i]])


    #재귀 함수
    def find_root(root_child, profit_dict, profit, p):
        # 종료 조건 부모가 "-"이 나온 경우 or 줄 이익이 1이하
        if p == "-" or profit <= 1:
            return

        #부모에게 자식의 10% 이익 주기
        profit_dict[p] += (profit // 10)

        p_next = None
        #탐색 부모에게 조상이 있다면 조상 저장
        for i in range(len(root_child)):
            if p == root_child[i][1]:
                p_next = root_child[i][0]

        #조상이 있다면 부모의 이익에서 조상 몫을 빼야함
        if p_next:
            profit_dict[p] -= profit // 10 // 10
            find_root(root_child, profit_dict, profit // 10, p_next)


    #자식이 돈을 벌었으면 부모 찾아서 이익 주기
    #재귀로 부모에게 또 부모가 있는지 확인 및 이익 주기
    for i in range(len(root_child)):
        if root_child[i][1] in seller_dict:
            #이익 분배
            profit = seller_dict[root_child[i][1]]*100
            profit_dict[root_child[i][1]] = profit - (profit // 10)
            #함수 부르기
            find_root(root_child, profit_dict, profit, root_child[i][0])

    print(list(profit_dict.values()))

if __name__ == '__main__':
    solution()
