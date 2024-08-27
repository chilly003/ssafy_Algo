# import sys
# sys.stdin = open('./4835_input (1).txt')
#
# T = 10
# for tc in range(1, T+1):
#     N = int(input())
#     arr = list(map(int, input().split()))
#     result = 0

Data=[0, 4, 1, 2, 3, 1, 2, 4]
count = [0]*5 #데이터가 0~4까지의 정수

N = len(Data)
Temp = [0] *N

#1단계
for x in Data:
    count[x] += 1

#2단계 카운트[1]부터 카운트[4]까지 개수
for i in range(1,5):
    count[i] = count[i-1] +count [i]

#3단계
for i in range(N-1, -1,-1):
    count[Data[i]] -= 1
    Temp[count[Data[i]]]= Data[i]

print(Temp)

#각 자리 수 추출하여 개수를 누적하기
num = 456789
c=[0]*12

for i in range(6):
    c[num % 10] +=1
    num //=10