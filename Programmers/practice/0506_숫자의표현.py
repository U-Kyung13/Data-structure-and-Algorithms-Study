# 내 풀이 : 투 포인터
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


# 다른 풀이 
def solution(n):
    anwer = 0 
    for i in range(1, n+1):
        sum_n = 0 
        while sum_n < n:
            sum_n += i 
            i += 1
        if sum_n == n:
            answer += 1
    return answer
