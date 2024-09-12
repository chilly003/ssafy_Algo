import sys
sys.stdin = open('sample_input (2).txt')

def dfs(month, sum_cost):
    global min_price

    if month > 12:
        min_price = min(min_price, sum_cost)
        return

    dfs(month + 1, sum_cost + (days[month] * cost[0]))
    dfs(month + 1, sum_cost + cost[1])
    dfs(month + 3, sum_cost + cost[2])
    dfs(month + 12, sum_cost + cost[3])


T  = int(input())
for t in range(1, T+1):
    cost = list(map(int, input().split()))
    days = [0] + list(map(int, input().split()))
    min_price = 1e9

    dfs(1,0)
    print(f'#{t} {min_price}')

if __name__ == '__main__':
    pass