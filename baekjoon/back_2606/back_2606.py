import sys
sys.stdin = open('test.txt')

#바이러스 전염 함수
def virus(x, y):
    x_root = find(x)
    y_root = find(y)

    if x_root == y_root:
        return

    if x_root < y_root:
        computer[y] = x_root
        for i in range(N + 1):
            if computer[i] == y_root:
                computer[i] = x_root
    else:
        computer[x] = y_root
        for i in range(N + 1):
            if computer[i] == x_root:
                computer[i] = y_root

def find(idx):
    if computer[idx] == idx:
        return idx

    return find(computer[idx])


N = int(input())    #컴퓨터 수
M = int(input())    #컴퓨터 짝들
computer = [i for i in range(N+1)]  #더미 0을 추가
for _ in range(M):
    information = list(map(int, input().split()))
    virus(information[0], information[1])

#1번 컴퓨터를 통해 바이러스에 걸린 컴의 개수(1번 컴은 빼야함)
print(computer.count(1) - 1)


if __name__ == "__main__":
    pass