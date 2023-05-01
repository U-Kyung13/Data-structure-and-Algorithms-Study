def solution(s):
    s_int = [int(i) for i in s.split(' ')] 
    answer = str(min(s_int)) + ' ' + str(max(s_int))
    return answer


# split()의 default는 공백이다 -> s.split()이라고 써도 됨
# list comprehension 대신 list(map(int, s.split()))으로 할 수 있음
