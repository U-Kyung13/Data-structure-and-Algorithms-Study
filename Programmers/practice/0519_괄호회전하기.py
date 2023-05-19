def solution(s):

    def solution1(s):
        match = {')':'(', '}':'{', ']':'['}
        stack = []
        for c in s:
            if c in '({[':
                stack.append(c)
            elif c in match:
                if stack == []:
                    return False
                else:
                    t = stack.pop()
                    if t != match[c]:
                        return False
        return stack == []
    
    
    answer = 0
    for i in range(len(s)):
        s = s[1:]+s[0]
        answer += solution1(s)

    return answer
