"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : [3차] 파일명 정렬
description : 정렬
"""


def div_file(files, i):
    flag = True
    head, number = "", ""

    for j in range(len(files[i])):

        if files[i][j].isdigit():
            number += files[i][j]
            flag = False
        elif flag is False:
            break
        else:
            head += files[i][j]

    return head.lower(), int(number)


def solution(files):
    answer = []
    temp_files = []

    for i in range(len(files)):
        temp_files.append((div_file(files, i), i, files[i]))

    sort_files = sorted(temp_files, key=lambda x: (x[0], x[1], x[2]))

    for i in range(len(sort_files)):
        answer.append(sort_files[i][-1])

    return answer
