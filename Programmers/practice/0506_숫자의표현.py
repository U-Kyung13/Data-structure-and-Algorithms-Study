# 투 포인터
def solution(n):
    n_list = [i for i in range(1, n+1)]
    answer = 0
    left = 0
    right = 1
    while left < n:
        target = sum(n_list[left:right+1])
        if target < n:
            right += 1
        elif target == n:
            answer += 1
            left += 1
            right = left + 1
        elif target > n:
            left += 1
            right = left + 1
    return answer
