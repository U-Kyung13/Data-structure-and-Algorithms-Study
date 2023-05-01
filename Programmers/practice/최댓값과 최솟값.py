def solution(s):
    s_int = [int(i) for i in s.split(' ')] 
    answer = str(min(s_int)) + ' ' + str(max(s_int))
    return answer
