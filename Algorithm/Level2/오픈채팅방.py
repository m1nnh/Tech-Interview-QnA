"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 오픈채팅방
description : 딕셔너리
"""

from collections import defaultdict


def solution(record):
    answer = []
    dic = defaultdict(str)

    for i in range(len(record)):
        split_record = record[i].split()

        if split_record[0] in ["Enter", "Change"]:
            dic[split_record[1]] = split_record[2]

    for i in range(len(record)):
        split_record = record[i].split()

        if split_record[0] == "Enter":
            answer.append(dic[split_record[1]] + "님이 들어왔습니다.")
        elif split_record[0] == "Leave":
            answer.append(dic[split_record[1]] + "님이 나갔습니다.")

    return answer
