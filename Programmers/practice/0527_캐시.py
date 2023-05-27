def solution(cacheSize, cities):
    cities = [x.lower() for x in cities]
    cache = []
    answer = 0 
    if cacheSize == 0:
            return len(cities)*5
    for city in cities:
        if not city in cache:
            if len(cache) < cacheSize:
                cache.append(city)
                answer += 5
            else:
                cache.pop(0)
                cache.append(city)
                answer += 5
        else:
            cache.pop(cache.index(city))
            cache.append(city)
            answer += 1
    return answer
