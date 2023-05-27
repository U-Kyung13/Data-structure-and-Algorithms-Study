def solution(A, B):
    answer = []
    for A_row in A:
        row_temp = []
        for B_col in zip(*B):
            row_temp.append(sum(x*y for x, y in zip(A_row, B_col)))
        answer.append(row_temp)
    return answer
  
