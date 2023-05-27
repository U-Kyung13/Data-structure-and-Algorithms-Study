import collections, functools
def solution(clothes):
    clothes_num = collections.Counter([x[1] for x in clothes])
    # 옷 종류별로 아무것도 착용 안하는 경우 포함하여 (x+1)!
    # 아예 아무것도 착용 안하는 경우는 없으니 -1 
    return functools.reduce(lambda a, b: a*b, [i+1 for i in clothes_num.values()]) - 1 
