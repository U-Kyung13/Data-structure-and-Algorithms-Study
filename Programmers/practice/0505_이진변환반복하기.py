def solution(s):
    convert_cnt = 0
    remove_cnt = 0

    while s != "1":
        if '0' in s:
            remove_cnt += s.count('0')
            s = s.replace('0', '')

        length = len(s)

        s = str(bin(len(s)))[2:]
        convert_cnt += 1
        
    answer = [convert_cnt, remove_cnt]
    return answer
