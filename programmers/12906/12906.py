def solution(arr):
    new_arr = []
    stack_arr = []
    for i in arr:
        if i not in stack_arr and stack_arr == []:
            stack_arr.append(i)
        elif i not in stack_arr and stack_arr != []:
            new_arr.append(stack_arr.pop())
            stack_arr.append(i)

    if stack_arr:
        new_arr.append(stack_arr.pop())

    return new_arr



if __name__ == '__main__':
    arr = [1,1,3,3,0,1,1]
    print(solution(arr))