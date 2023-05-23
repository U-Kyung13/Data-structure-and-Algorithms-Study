# 처음 코드
def solution(citations):
    citations.sort()
    answer = 0
    
    while True:
        if len([x for x in citations if x >= answer]) < answer:
            break
        answer += 1
    return answer-1
    
    
    # 다른 사람 코드 참고
    def solution(citations):
    h = 0
    citations.sort(reverse=True)
    for i, x in enumerate(citations):
        if i+1 <= x:
            h = i+1
        else:
            break
    return h
