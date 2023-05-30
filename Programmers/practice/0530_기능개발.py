import math, collections
def solution(progresses, speeds):
    result = collections.deque([math.ceil((100-progresses[i])/speeds[i]) for i in range(len(progresses))]) # 기능별 배포 가능일 
    answer = []
    while result:
        i = 1
        a = result.popleft()
        while result and a >= result[0]:
            i += 1
            result.popleft()
        answer.append(i)
    return answer
