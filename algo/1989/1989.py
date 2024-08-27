import sys
sys.stdin = open('./input.txt')

def solution(t):
    is_pld = str(input())
    #빈 리스트 만들기
    fist_str = []
    last_str = []
    #찾을 문자 길이가 짝수인지 홀수인지 확인하고 각각의 조건 다르게 해서 검사.
    if len(is_pld)%2 == 0:
        #만약 짝수라면 중간을 기준으로 앞, 뒤 문자열 저장
        #앞 문자열과 뒤집은 뒤 문자열이 같으면 1 아니면 0
        fist_str = is_pld[:len(is_pld)//2]
        last_str = is_pld[len(is_pld)//2:len(is_pld)]
        if fist_str == last_str[::-1]:
            return 1
        else:
            return 0
    else:
        #홀수도 같은 방식으로 함
        #대신 범위는 주의해서 설정
        fist_str = is_pld[:len(is_pld) // 2]
        last_str = is_pld[len(is_pld) // 2 + 1:len(is_pld)]
        if fist_str == last_str[::-1]:
            return 1
        else:
            return 0

if __name__ == '__main__':
    T = int(input())
    for t in range(1,T+1):
        print(f'#{t} {solution(t)}')