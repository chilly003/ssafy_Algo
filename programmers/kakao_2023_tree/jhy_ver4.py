def solution(numbers):
    answer = []
    dict_num = [1, 3, 7, 15, 31, 63]

    for number in numbers:  # numbers에 있는 숫자들을 검사
        real_num = bin(number)[2:]  # 이진수로 전환

        def find(real_num):
            for j in dict_num:  # [1, 3, 7, 15, 31, 63] 를 순회하면서
                if len(real_num) <= j:  # 확장해야하면
                    real_num = "0" * (j - len(real_num)) + real_num # 모자란 길이만큼 추가
                    return real_num

        real_num = find(real_num)

        ### 위로는 숫자 확장 로직

        # 조건이 되는 부모인지 확인.
        def check_validation(len_rn):
            for i in range(1, len_rn, 2):  # 부모가 0이지만 자식도 0인 경우를 찾음
                if real_num[i] == "0" and (real_num[i + 1] == "1" or real_num[i - 1] == "1"):
                    return 0
            else:
                return 1

        if not check_validation(len(real_num)):
            answer.append(0)
        else:
            answer.append(1)

    return answer


if __name__ == "__main__":
    # # print(solution([7, 42, 5]))  # [1, 1, 0]
    # # print(solution([63, 111, 95]))  # [1, 1, 0]
    # print(solution([423]))
    # print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 128, 129, 16512, 2147516555]))
    #              # [1, 1, 1, 0, 0, 1, 1, 1, 0, 1,  1,  0,  0,  1,  1,  0,  1,   0,   0,     1] : 정답
    #              # [1, 1, 1, 0, 0, 1, 1, 1, 0, 1,  1,  0,  0,  1,  1,  0,  1,   0,   0,     1] : 효원이 답
    # print(solution([138]))
    # print(solution([i for i in range(17,128)]))
    # print(solution([24, 26, 27, 30, 31, 32, 34, 35, 96, 98, 99]))
    print(solution([i for i in range(128)]))
