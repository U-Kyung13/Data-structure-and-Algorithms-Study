def solution(brown, yellow):
    answer = []
    if yellow == 1:
        answer = [3,3]
    else:
        for i in range(1, yellow//2+1):
            if yellow % i == 0:
                yellow_x, yellow_y = yellow//i, i # yellow 카펫의 가로, 세로
                tot_x, tot_y = yellow_x+2, yellow_y+2 # 전체 카펫의 가로, 세로
                if brown == tot_x*tot_y - yellow:
                    answer = [tot_x, tot_y]
                    break
    return answer
