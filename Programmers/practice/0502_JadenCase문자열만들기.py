def solution(s):  
    answer = [x.capitalize() for x in s.split(" ")]
    answer = ' '.join(answer)
    return answer
  
  
# a = 'unfollowed  me'
# [x for x in a.split()] -> ['unfollowed', 'me']
# [x for x in a.split(" ")] -> ['unfollowed', '', 'me']

# capitalize() : 첫글자는 대문자로, 나머지는 소문자로 
