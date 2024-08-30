from collections import deque
from math import log2

def is_expressable(number: str) -> int:
    filters = [3, 7, 15, 31, 63]
    num_len = len(number)
    threshold = 0
    
    for i in range(5):
        threshold = i
        if num_len <= filters[i]:
            break
    number = ("0" * (filters[threshold] - num_len)) + number
    
    
    filter = filters[threshold]
    mid = filter // 2
    if number[mid] == "0": return 0 # 루트가 0
    else: # 루트가 1
        bfs_q = deque()
        bfs_q.append(mid)
        for h in range(int(log2(filter + 1)) - 1, 0, -1):
            bfs_q_len = len(bfs_q)
            for _ in range(bfs_q_len):
                mid = bfs_q.popleft() # mid 추출
                if mid - 2**(h-1) >= 0:  # 왼쪽 인덱싱 체크
                    if number[mid] == '0' and number[mid-2**(h-1)] == "1": # 내가 0인데 내 왼쪽 자식이 1이면
                        return 0 # 즉시 중단
                    else:# 내가 0이 아니거나, 내 왼쪽 자식이 0이라면
                        bfs_q.append(mid - 2**(h-1))
                if mid + 2**(h-1) <= filter:  # 오른쪽 인덱싱 체크
                    if number[mid] == '0' and number[mid+2**(h-1)] == "1": # 내가 0인데 내 오른쪽 자식이 1이면
                        return 0 # 즉시 중단
                    else: # 내가 0이 아니거나, 내 오른쪽 자식이 0이라면
                        bfs_q.append(mid + 2**(h-1))
        else: # 중단되지 않았다면? -> 검사 통과
            return 1



def solution(numbers) -> list:
    return [is_expressable(bin(n)[2:]) if n > 1 else 1 for n in numbers]

if __name__ == "__main__":
    # # print(solution([7, 42, 5]))  # [1, 1, 0]
    # # print(solution([63, 111, 95]))  # [1, 1, 0]
    # print(solution([423]))
    # print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 128, 129, 16512, 2147516555]))
    #              # [1, 1, 1, 0, 0, 1, 1, 1, 0, 1,  1,  0,  0,  1,  1,  0,  1,   0,   0,     1] : 정답
    #              # [1, 1, 1, 0, 0, 1, 1, 1, 0, 1,  1,  0,  0,  1,  1,  0,  1,   0,   0,     1] : 효원이 답
    # print(solution([138]))
    print(solution([i for i in range(129,1000)]))
    # print(solution([24, 26, 27, 30, 31, 32, 34, 35, 96, 98, 99]))    