"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : [3차] 압축
description : 딕셔너리
"""

from collections import defaultdict


def solution(msg):
    answer = []
    alphabet_dic = defaultdict(int)

    for i in range(26):
        alphabet_dic[chr(ord('A') + i)] = i + 1

    now = 27
    idx = 1
    result = msg[0]

    while idx < len(msg):
        if result + msg[idx] not in alphabet_dic:
            answer.append(alphabet_dic[result])
            alphabet_dic[result + msg[idx]] = now
            result, idx, now = msg[idx], idx + 1, now + 1
        else:
            result += msg[idx]
            idx += 1

    if result in alphabet_dic:
        answer.append(alphabet_dic[result])

    return answer
