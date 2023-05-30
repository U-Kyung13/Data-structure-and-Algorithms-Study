import collections
def solution(s):
    dict = s.split('}')
    dict = dict[:-2]
    dict = [x[2:].split(',') for x in dict]
    dict = [int(y) for x in dict for y in x]
    dict = collections.Counter(dict)
    answer = sorted(dict, key = dict.get, reverse=True)
    return answer
