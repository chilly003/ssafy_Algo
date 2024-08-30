def solution(numbers):
    answer = []
    dict_num = [1,3,7,15,31,63]

    for t in numbers:
        result_num = []
        a = bin(t)
        real_num = a[2:]
        temp = 0

        def find(real_num,temp):
            for j in dict_num:
                if len(real_num) <= j:
                    temp = j - len(real_num)
                    real_num = '0' * temp + real_num
                    result_num.append(real_num)
                    return temp, real_num
                
        temp, real_num = find(real_num, temp)

        ##조건이 되는 부모인지 확인.
        result = []
        len_rn = len(result_num[0])
        #아 이거 뭔데 진짜
        for i in range(1, len_rn, 2):
            if result_num[0][i] == '1' and i >= temp:
                result.append(1)
            #더미 수 이상의 범위이면서 부모가 0이지만 자식도 0인 경우
            elif result_num[0][i] == '0' and i >= temp: 
                if result_num[0][i+1] == '0' and result_num[0][i-1] == '0':
                    result.append(1)
                else:
                    result.append(0)

        if 0 in result:
            answer.append(0)
        else:
            answer.append(1)

    return answer