def solution(n, s):
    if s // n == 0 :
        answer = [-1]
    else: 
        answer = [s//n]*n
        mod = s % sum(answer)
        if mod != 0:
            answer = answer[:n-mod] + [x+1 for x in answer[n-mod:]]       
    return answer
