"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 실패율
description : 정렬
"""

from collections import defaultdict


def calc_rate(dic, length, N):
    result = []

    for i in range(N):
        result.append([0, i + 1])

    for key, value in dic:
        if key > N:
            break
        else:
            result[key - 1] = [value / length, key]
            length -= value

    return result


def solution(N, stages):
    answer = []
    dic = defaultdict(int)

    for stage in stages:
        dic[stage] += 1

    sort_dic = sorted(dic.items())

    # 위에서 함수 결과 값을 정렬해서 반복문 실행
    for rate, idx in sorted(calc_rate(sort_dic, len(stages), N), key=lambda x: (-x[0], x[1])):
        answer.append(idx)

    return answer
