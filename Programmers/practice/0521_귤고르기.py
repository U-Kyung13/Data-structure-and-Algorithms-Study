import collections
def solution(k, tangerine):
    ans = 0
    t_cnt = collections.Counter(tangerine)
    t_cnt = t_cnt.most_common()
    for cnt in t_cnt:
        if k > 0:
            ans += 1
            k -= cnt[1]
        else:
            break
    return ans
