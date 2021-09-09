"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : [1차] 캐시
description : 큐
"""

from collections import deque


def solution(cacheSize, cities):
    answer = 0
    cache = deque()

    if cacheSize == 0:
        return len(cities) * 5

    for city in cities:
        city = city.lower()

        if city not in cache:
            if len(cache) == cacheSize:
                cache.popleft()

            cache.append(city)
            answer += 5

        else:
            cache.remove(city)
            cache.append(city)
            answer += 1

    return answer
