"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 신규 아이디 추천
description : 구현
"""


def solution(new_id):
    answer = ''

    for str_id in new_id:
        if str_id in ["-", "_", "."]:
            if str_id == "." and len(answer) != 0:
                if answer[-1] == ".":
                    continue
                else:
                    answer += str_id
            else:
                answer += str_id
        elif str_id.isalpha():
            answer += str_id.lower()
        elif str_id.isdigit():
            answer += str_id

    if answer[0] == ".":
        if len(answer) == 1:
            answer = "a"
        else:
            answer = answer[1:]

    if len(answer) >= 15:
        answer = answer[:15]

    if answer[-1] == "." and len(answer) > 1:
        answer = answer[:-1]

    if len(answer) < 3:
        answer += answer[-1] * (3 - len(answer))

    return answer
