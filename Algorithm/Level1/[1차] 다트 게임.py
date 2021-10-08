"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 1차 다트 게임
description : 구현
"""


def score_check(n, bonus):
    dic = {"S": 1, "D": 2, "T": 3}

    return n ** dic[bonus]


def solution(dartResult):
    answer = []
    num = ""

    for result in dartResult:
        if result.isdigit():
            num += result
        elif result in ["S", "D", "T"]:
            answer.append(score_check(int(num), result))
            num = ""
        elif result == "#":
            answer[-1] *= (-1)
        else:
            if len(answer) > 1:
                answer[-1] *= 2
                answer[-2] *= 2
            else:
                answer[-1] *= 2

    return sum(answer)
