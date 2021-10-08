"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 튜플
description : 정렬
"""

from collections import defaultdict


def solution(s):
    dic = defaultdict(int)
    number = ""

    for string in s:
        if string.isdigit():
            number += string
        else:
            if len(number) > 0:
                dic[int(number)] += 1
                number = ""

    answer = [key for key, value in sorted(dic.items(), key=lambda x: -x[1])]

    return answer
