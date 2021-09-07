"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 문자열 압축
description : 슬라이싱
"""


def compression(i, now, length, s):
    count = 1
    result = ""

    for j in range(i, length, i):
        if now == s[j: j + i]:
            count += 1
        else:
            if count == 1:
                result += now
            else:
                result += str(count) + now
            count = 1
            now = s[j: j + i]

    if count != 1:
        result += str(count) + now

    return len(result)


def solution(s):
    answer = len(s)

    for i in range(1, len(s) - 1):
        now = s[0: i]
        answer = min(compression(i, now, len(s) + i, s), answer)

    return answer
