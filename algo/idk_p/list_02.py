arr = list(map(int, input().split()))
N = 617

k = 0
while k == N + 1:
    max_s = max(arr)
    min_s = min(arr)

    max_s -= 1
    min_s += 1
    k += 1

print(max_s - min_s)


