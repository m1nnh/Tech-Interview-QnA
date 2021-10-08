"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : [1차] 뉴스 클러스터링
description : 딕셔너리
"""

from collections import defaultdict


def list_to_dict(string):
    dic = defaultdict(int)

    for i in range(0, len(string) - 1):
        if string[i].isalpha() and string[i + 1].isalpha():
            dic[string[i].lower() + string[i + 1].lower()] += 1

    return dic


def solution(str1, str2):
    str1_dic = list_to_dict(str1)
    str2_dic = list_to_dict(str2)

    if len(str1_dic) == 0 and len(str2_dic) == 0:
        return 65536

    count = 0

    for key, value in str1_dic.items():
        if key in str2_dic:
            if value > str2_dic[key]:
                count += str2_dic[key]
            else:
                count += value

    answer = int(65536 * (count / (sum(str1_dic.values()) + sum(str2_dic.values()) - count)))

    return answer
