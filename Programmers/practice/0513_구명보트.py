# TLE
def solution(people, limit):
    people.sort(reverse = True) # 무거운 순으로 정렬
    answer = 0
    while people:
        answer += 1
        temp = people.pop() # 남은 사람 중 가장 가벼운 사람
        for i, x in enumerate(people):
            if temp + x <= limit: # 가장 무거운 사람부터 더해가며 무게 제한 이하인 경우 people에서 제거 
                people.pop(i)
                break
    return answer

  
  # 투포인터
  
