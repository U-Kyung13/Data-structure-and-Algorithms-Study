def solution(elements):
    tot_sum = []
    for i in range(len(elements)):
        temp = elements + elements[:i]
        tot_sum += [sum(temp[j:j+i+1]) for j in range(len(temp)-i)]
    answer = len(set(tot_sum))
    return answer
