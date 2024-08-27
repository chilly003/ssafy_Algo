# 파일 입력을 시스템 입력으로
import sys
sys.stdin = open('input (1).txt', 'r')
#이거 r이 뭐에여?????

# test case의 수 만큼 반복
for test_case in range(1, 11):
      T = int(input())
      N = 100
      ladders = [list(map(int, input().split())) for i in range(N)]

      # 도착점을 찾아서, 도착점부터 시작
      for j in range(N):
              if ladders[99][j] == 2:
                  break

      # 행이 0이 될 때까지 반복
      i = 99
      while i > 0:
              # 현재 위치가 왼쪽 끝이 아니고, 왼쪽이 1이라면
              if j != 0 and ladders[i][j-1] == 1:
                  # 더 이상 왼쪽이 1이 아닐 때까지 왼쪽으로 가자
                  while j != 0 and ladders[i][j-1] == 1:
                          j -= 1
                  # 왼쪽으로 다 갔으면 올라가자
                  i -= 1
              # 현재 위치가 오른쪽 끝이 아니고, 오른쪽이 1이라면
              elif j != 99 and ladders[i][j+1] == 1:
                  # 더 이상 오른쪽이 1이 아닐 때까지 오른쪽으로 가자
                  while j != 99 and ladders[i][j+1] == 1:
                          j += 1
                  # 오른쪽으로 다 갔으면 올라가자
                  i -= 1
              # 둘 다 아닌 경우에는 그냥 올라가자
              else:
                  i -= 1

      # 정답 출발지점 출력
      print(f"#{test_case} {j}")