import math
def solution(arr):
    ans = arr[0]
    for x in arr:
        ans = ans*x // math.gcd(ans, x)
    return ans
