"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 순위 검색
description : 구현, 조합, 이진 탐색
"""

from collections import defaultdict
from itertools import combinations
from bisect import bisect_left


def make_comb(info):
    result = []

    for i in range(5):
        for comb in list(combinations([0, 1, 2, 3], i)):
            temp = ""
            for j in range(4):
                if j not in comb:
                    temp += info[j]
                else:
                    temp += "-"
            result.append(temp)
    return result


def solution(info, query):
    answer = []
    info_dic = defaultdict(list)

    for developer_info in info:
        split_info = developer_info.split()
        comb_info = make_comb(split_info)

        for comb in comb_info:
            info_dic[comb].append(int(split_info[-1]))

    for key in info_dic.keys():
        info_dic[key].sort()

    for qry in query:
        split_query = qry.split()
        result_query = split_query[0] + split_query[2] + split_query[4] + split_query[6]

        if result_query in info_dic:
            answer.append(len(info_dic[result_query]) - bisect_left(info_dic[result_query], int(split_query[-1])))
        else:
            answer.append(0)

    return answer
