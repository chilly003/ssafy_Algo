def dfs(depth, target, numbers):
    if depth == len(numbers):
        if target == 0:
            return 1
        else :
            return 0

    result1 = dfs(depth + 1, target + numbers[depth], numbers)
    result2 = dfs(depth + 1, target - numbers[depth], numbers)
    return result1 + result2

def solution(numbers, target):
    return dfs(0, target, numbers)

if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3))
    print(solution([4, 1, 2, 1], 4))