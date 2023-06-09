import math
def solution(n, k):
    # k 진수로 변환
    rev_base = ''
    while n > 0:
        n, mod = divmod(n, k)
        rev_base += str(mod)
        
    # 0을 포함하면 안되므로 0을 기준으로 split
    ans = rev_base[::-1].split('0')
    ans = [x for x in ans if x != '']

    # 소수 판별 알고리즘
    def is_prime_number(x):
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False
        return True
    
    # 소수만 저장
    ans = [x for x in ans if is_prime_number(int(x)) and x != '1']
    
    return len(ans)
