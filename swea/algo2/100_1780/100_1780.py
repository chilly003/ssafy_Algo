import sys
sys.stdin = open('100_1780_input.txt')

def paper(N, arr):

    for i in range(0, N, N//3):
        for j in range(0, N, N//3):
            temp =[]
            for row in arr[i:i+N//3]:
                temp.append(row[j:j+N//3])

            set_temp = set(sum(temp, []))
            if len(set_temp) == 1:
                check(set_temp)
            else:
                paper(N//3, temp)


def check(check):
    global cnt__1, cnt_0, cnt_1
    if check == {-1}:
        cnt__1 += 1
        return
    elif check == {0}:
        cnt_0 += 1
        return
    elif check == {1}:
        cnt_1 += 1
        return


N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
cnt__1, cnt_0, cnt_1 = 0, 0, 0

#처음 받는 종이가 같은 숫자로 채워진 종이인지 검사.
first_check = []
for i in range(N):
    first_check += arr[i]

if len(set(first_check)) == 1:
    check(set(first_check))
else:
    paper(N, arr)

print(cnt__1)
print(cnt_0)
print(cnt_1)

