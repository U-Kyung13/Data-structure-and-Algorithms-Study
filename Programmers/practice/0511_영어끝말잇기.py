##########################
### 첫 풀이 (통과 못함) ###
##########################
def solution(n, words):
    answer = []
    
    # 규칙에 어긋난 인덱스
    wrong_idx = []
    for i in range(1, len(words)):
        if words[i-1][-1] != words[i][0]:
            wrong_idx.append(i)
            
    # 중복된 인덱스
    dup_idx = []
    for idx, word in enumerate(words):
        if word in words[idx+1:]:
            dup_idx.append(words[idx+1:].index(word) + idx + 1)
    
    # 끝말잇기가 끝나지 않은 경우
    # 규칙에 어긋난 적 X, words내 중복되는 단어 X
    if len(wrong_idx) == 0 and len(dup_idx) == 0 :
        answer = [0, 0]   
    
     
    # 규칙에 어긋난 적 O, words내 중복되는 단어 O
    # 둘 중 먼저 일어난 것으로 처리
    elif len(wrong_idx) != 0 and len(dup_idx) != 0:
        idx = min(wrong_idx[0], dup_idx[0])
        # 게임이 끝난 곳에서 words가 끊기도록 인덱싱 
        words = words[:idx+1]
        # 가장 먼저 탈락하는 사람의 번호
        answer.append(n - (len(words) % n)) 
        # 몇 번째 차례에서 탈락
        if len(words) % n != 0:
            answer.append(len(words)//n + 1)
        else:
            answer.append(len(words)//n)

    
    # 규칙에 어긋난 적 O, words내 중복되는 단어 X
    elif len(wrong_idx) != 0 and len(dup_idx) == 0:
        # 게임이 끝난 곳에서 words가 끊기도록 인덱싱
        words = words[:wrong_idx[0]+1]
        # 가장 먼저 탈락하는 사람의 번호
        answer.append(n - (len(words) % n)) 
        # 몇 번째 차례에서 탈락
        if len(words) % n != 0:
            answer.append(len(words)//n + 1)
        else:
            answer.append(len(words)//n)
    
    
    # 규칙에 어긋난 적 X, words내 중복되는 단어 O
    elif len(wrong_idx) == 0 and len(dup_idx) != 0:
        # 게임이 끝난 곳에서 words가 끊기도록 인덱싱
        words = words[:dup_idx[0]+1]
        # 가장 먼저 탈락하는 사람의 번호
        answer.append(n - len(words)%n) 
        # 몇 번째 차례에서 탈락
        if len(words) % n != 0:
            answer.append(len(words)//n + 1)
        else:
            answer.append(len(words)//n)

    return answer
  
  
  
#########################
### 두번째 풀이 (통과) ###
#########################
  
# 규칙에 어긋난 적 X, words내 중복되는 단어 X을 제외하고는 동일한 처리를 해줌 -> 묶자!
# 인덱스를 따로 저장해주면 묶을 수 없음
# for문으로 규칙에 어긋나거나 중복이 발생하는 경우 처리를 해줌
# 참고 자료: https://velog.io/@insutance/%ED%94%84%EB%A1%9C%EA%B7%B8%EB%9E%98%EB%A8%B8%EC%8A%A4Python-%EC%98%81%EC%96%B4-%EB%81%9D%EB%A7%90%EC%9E%87%EA%B8%B0

def solution(n, words):
    for i in range(1, len(words)):
        if words[i][0] != words[i-1][-1] or words[i] in words[:i]:
            return [(i%n)+1, (i//n)+1]
    return [0, 0]

