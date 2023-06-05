def solution(operations):
    ans = []
    for oper in operations:
        if (oper == "D 1") & (ans != []):
            ans.pop(ans.index(max(ans)))
        elif (oper == "D -1") & (ans != []):
            ans.pop(ans.index(min(ans)))
        elif oper not in ["D 1", "D -1"]:
            ans.append(int(oper.split()[1]))
    if ans == []:
        answer = [0,0]
    else:
        answer = [max(ans), min(ans)]
    return answer
