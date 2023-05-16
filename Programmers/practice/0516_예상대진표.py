def solution(n,a,b):
    temp1 = [0]*n
    temp1[a-1] = 1
    temp1[b-1] = 1
    answer = 0

    while True:
        answer += 1
        temp2 = []
        for i in range(0, len(temp1), 2):
            temp3 = temp1[i]+temp1[i+1]
            temp2.append(temp3)
        temp1 = temp2
        if 2 in temp1:
            break
    return answer
