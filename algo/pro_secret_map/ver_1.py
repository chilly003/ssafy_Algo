def solution(n, arr1, arr2):
    answer = []

    #받아온 리스트에 숫자를 2진수로 바꿔주고 숫자부분만 저장
    for i in range(n):
        arr1[i] = bin(arr1[i])[2:]
        arr2[i] = bin(arr2[i])[2:]

    #문제발생-> | 연산은 앞에부터 순서대로 작동? 하기에 길이 안맞으면 결과 값이 달라짐
    #해결 -> 이중포문으로 or 돌려야하나 싶었으나 zfill이란 함수 확인
    #문자열에 n의 길이를 맞춰서 0넣어준다.
    #맞춰진 문자열대로 글자 확인 후 벽, 공백 바꿔주기
    for i in range(n):
        answer.append(bin(int(arr1[i], 2) | int(arr2[i], 2))[2:])
        answer[i] = answer[i].zfill(n)
        answer[i] = answer[i].replace('1','#')
        answer[i] = answer[i].replace('0', ' ')

    return answer

if __name__ == '__main__':
    n = 6
    arr1 = [46, 33, 33 ,22, 31, 50]
    arr2 = [27 ,56, 19, 14, 14, 10]
    print(solution(n, arr1, arr2))