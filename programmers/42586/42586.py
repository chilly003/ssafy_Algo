def solution(arr, speeds):
    end_dict = {}
    #딕셔너리로 각 일이 며칠이 있어야 끝나는지 만들기
    for i in range(len(arr)):
        cnt = 0
        while True:
            if arr[i] >= 100:
                end_dict[i] = cnt
                break
            arr[i] += speeds[i]
            cnt += 1

    cnt = 0     #배포할 일 개수
    temp = []   #정답
    idx = end_dict[0] #기준이 되는 일처리 일자
    for i in range(len(arr)):
        #만약 자신보다 앞에 있는 일이 더 크거나 같다면 카운트 올리기
        if end_dict[i] <= idx:
            cnt += 1
        #그게 아니라면 정답에 숫자 넣어주고 카운트 1, 기준 바꿔주기
        else:
            temp.append(cnt)
            cnt = 1
            idx = end_dict[i]
    #마지막으로 넣지 못한 일 숫자도 넣어주기
    if cnt:
        temp.append(cnt)

    return temp


if __name__ == '__main__':
    arr = [95, 90, 99, 99, 80, 99]
    speeds = [1, 1, 1, 1, 1, 1]
    print(solution(arr, speeds))