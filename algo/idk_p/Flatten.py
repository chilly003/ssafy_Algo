import sys

sys.stdin = open("./input.txt")


def solution(t: int) -> int:
    # input
    dump = int(input())
    boxes = list(map(int, input().split()))

    boxes.sort(reverse=True)
    max_i = 0
    min_i = len(boxes) - 1
    while dump:
        # check if dump needed
        if boxes[max_i] <= boxes[min_i] + 1:
            break
        # do dump
        boxes[max_i] -= 1
        boxes[min_i] += 1
        dump -= 1
        max_i = boxes.index(max(boxes))
        min_i = boxes.index(min(boxes))

    print(f"#{t} {max(boxes) - min(boxes)}")


if __name__ == "__main__":
    for t in range(1, 11):
        solution(t)
