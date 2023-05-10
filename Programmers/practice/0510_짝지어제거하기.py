# 스택 - 성공
def solution(s):
    stack = []
    # 맞는 쌍이 나오면 pop
    for i in s:
        # stack에 아무것도 없을때는 stack에 현재 원소 추가
        if len(stack) == 0:
            stack.append(i)
        # 바로 이전 값과 현재 원소가 동일하면 stack에서 pop 
        elif stack[-1] == i:
            stack.pop()
        # 바로 이전 값과 현재 원소가 동일하지 않으면 stack에 원소 추가 
        else:
            stack.append(i)
    # 비어 있지 않으면 0 그렇지 않으면 1
    return 0 if stack else 1 


  
# 큐 - 실패  
import collections
def solution(n):
    queue = collections.deque()
    i = 0
    while queue:
        i += 1
        a = queue.popleft()
        b = queue.popleft()
        if a != b:
            queue.appendleft(b) 
            queue.append(a) 
        if i == len(s):
            break
    return int(len(queue) == 0)

# 큐 자료구조를 이용한건데 왜 틀린걸까?
# s = 'cdcd'를 넣었을때 1을 반환한다!
