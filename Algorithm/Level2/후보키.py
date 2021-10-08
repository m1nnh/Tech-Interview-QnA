"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 후보키
description : 조합, 구현
"""

from collections import defaultdict
from itertools import combinations


def validation(comb_list):
    global answer, dic
    set_comb = set(comb_list)
    flag = True

    for key, value in dic.items():
        for v in value:
            if set_comb.issuperset(v):
                flag = False
                break
        if flag is False:
            break

    if flag is True:
        dic[len(comb_list)].append(set_comb)
        answer += 1


def make_list(relation, i):
    # 인덱스를 가지고 만들 수 있는 조합
    for comb_list in list(combinations(range(len(relation[0])), i)):
        array = ["" for _ in range(len(relation))]
        # 조합을 가지고, 배열 생성
        for comb in comb_list:
            for j in range(len(relation)):
                array[j] += str(comb) + relation[j][comb]

        set_array = set(array)

        # 조합한 배열을 집합으로 만들어서 로우의 길이와 같은지 확인
        if len(set_array) == len(relation):
            validation(comb_list)


def solution(relation):
    global answer, dic
    answer = 0
    dic = defaultdict(list)

    for i in range(1, len(relation) + 1):
        make_list(relation, i)

    return answer
