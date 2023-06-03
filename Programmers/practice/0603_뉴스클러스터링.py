import collections
def solution(str1, str2):
    str1 = collections.Counter([str1[i:i+2].lower() for i in range(len(str1)-1) if str1[i:i+2].isalpha()])
    str2 = collections.Counter([str2[i:i+2].lower() for i in range(len(str2)-1) if str2[i:i+2].isalpha()])
    print(str1)
    print(str2)
    union = len(list((str1|str2).elements()))
    inter = len(list((str1&str2).elements()))
    return 65536 if union == 0 and inter == 0 else int((inter/union)*65536) 
