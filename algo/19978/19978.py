def dfs(i, total, target, numbers):
    if i == len(numbers):
        if total == target:
            global answer
            answer += 1
        return
    dfs(i + 1, total + numbers[i], target, numbers)
    dfs(i + 1, total - numbers[i], target, numbers)
    return


def solution(numbers, target):
    global answer
    answer = 0
    dfs(0, 0, target, numbers)
    return answer

if __name__ == "__main__":
    print(solution([1, 1, 1, 1, 1], 3))
    print(solution([4, 1, 2, 1], 4))