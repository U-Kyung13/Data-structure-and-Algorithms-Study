def solution(n, s):
    if s // n == 0 :
        answer = [-1]
    else: 
        answer = [1]*n
        while sum(answer) <= s:
            answer = [x+1 for x in answer]
        answer = [x-1 for x in answer]
        mod = s % sum(answer)
        if mod != 0:
            answer = [x+1 for x in answer[:mod]] + answer[mod:]              
    return sorted(answer, reverse=False)
