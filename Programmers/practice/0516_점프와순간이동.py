def solution(n):
    ans = 0 
    while n > 0:
        q, r = divmod(n, 2)
        n = q
        if r != 0:
            ans += 1
    return ans
  
  
  # 참고한 링크 : https://inspirit941.tistory.com/232
