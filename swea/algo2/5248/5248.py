import sys
sys.stdin = open('5248_sample_input.txt')


#지나치는 아이들 없게 person을 다시 돌면서
#같은 조인 애들이면 전부 새로운 대표자로 바꾸는 작업 실행
def union(x, y):
    #아이들의 대표가 누구인지 파악한다.
    x_root = find_root(x)
    y_root = find_root(y)

    if x_root == y_root:    #만약 대표가 서로 같으면 같은 조이니 리턴
        return

    if x_root < y_root:     #기존 대표보다 적은 숫자를 가진 대표가 나타나면
        person[y] = x_root  #바꿔주고
        for i in range(len(person)):    #기존대표에 포함된 조원들도 새로운 대표로 고쳐준다.
            if person[i] == y_root:
                person[i] = x_root
    else:
        person[x] = y_root
        for i in range(len(person)):
            if person[i] == x_root:
                person[i] = y_root


#대표 찾기 함수
def find_root(idk):
    if person[idk] == idk:      #만약 대표가 자기 자신이면 자기 자신을 리턴
        return idk

    return find_root(person[idk])   #아니라면 인덱스를 기준으로 대표 다시 찾아라


T = int(input())
for t in range(1, T + 1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    #자기 자신이 대표인 리스트
    person = [i for i in range(N + 1)]

    #M번의 요청 유니온함수로 전달
    for i in range(M):
        union(arr[i * 2], arr[i * 2 + 1])

    #대표자만 남게 하기(중복 제거)
    result = set(person)

    print(f'#{t} {len(result) - 1}')    #-1을 하는 이유는 더미 대표 0이 들어갔기 때문


if __name__ == "__main__":
    pass