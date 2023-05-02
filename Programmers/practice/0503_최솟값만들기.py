# 가장 작은 수 * 가장 큰 수를 누적한다는 아이디어

def solution(A,B):
    answer = 0

    A.sort(reverse=True)
    B.sort()
    
    for i in range(len(A)):
        answer += A.pop() * B.pop()

    return answer
 
