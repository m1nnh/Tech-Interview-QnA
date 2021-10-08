"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 메뉴 리뉴얼
description : 딕셔너리, 조합
"""

from collections import defaultdict
from itertools import combinations


def combination(orders, course):
    dic = defaultdict(int)

    for order in orders:
        sort_order = sorted(order)
        for j in course:
            if j > len(sort_order):
                break
            for comb in list(combinations(sort_order, j)):
                dic["".join(comb)] += 1

    list_dic = list(dic.items())
    sort_dic = sorted(list_dic, key=lambda x: (-x[1], x[0]))

    insert(sort_dic)


def insert(sort_dic):
    global answer
    count_dic = {}

    for key, value in sort_dic:
        if value == 1:
            break

        if len(key) not in count_dic:
            count_dic[len(key)] = value
            answer.append(key)
        else:
            if count_dic[len(key)] == value:
                answer.append(key)


def solution(orders, course):
    global answer
    answer = []

    combination(orders, course)

    if len(answer) != 0:
        answer.sort()

    return answer
