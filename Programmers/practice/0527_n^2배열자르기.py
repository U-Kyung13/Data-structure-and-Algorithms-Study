def solution(n, left, right):
    ans = []
    for idx in range(left, right+1):
        # 몫과 나머지 중 더 큰 수 + 1
        a, b = divmod(idx, n)
        ans.append(max(a, b) + 1)
    return ans
