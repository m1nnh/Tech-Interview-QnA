"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : [3차] 프렌즈 4블록
description : 구현
"""

# 코드 문자별로 변환
def insert_code(info, idx):
    if idx + 1 != len(info) and info[idx + 1] == "#":
        return info[idx] + info[idx + 1], idx + 2
    else:
        return info[idx], idx + 1


def solution(m, musicinfos):
    answer = []
    music_info = []

    for info in musicinfos:
        split_info = info.split(",")
        start_time = split_info[0].split(":")
        end_time = split_info[1].split(":")
        play_time = (60 * int(end_time[0]) + int(end_time[1])) - (60 * int(start_time[0]) + int(start_time[1]))

        idx = 0
        new_code = []

        for i in range(play_time):
            if idx == len(split_info[-1]):
                idx = 0

            code, idx = insert_code(split_info[-1], idx)
            new_code.append(code)

        music_info.append([play_time, new_code, split_info[2]])

    org_code = []
    idx = 0

    while idx < len(m):
        code, idx = insert_code(m, idx)
        org_code.append(code)

    for i in range(len(music_info)):
        flag = False
        # 비교는 앞에서부터 슬라이싱으로 확인
        for j in range(len(music_info[i][1]) - len(org_code) + 1):
            if music_info[i][1][j: len(org_code) + j] == org_code:
                flag = True
                break

        if flag is True:
            if len(answer) > 0 and answer[0] < music_info[i][0]:
                answer = music_info[i]
            elif len(answer) == 0:
                answer = music_info[i]

    if len(answer) == 0:
        answer = "(None)"
    else:
        answer = answer[-1]

    return answer
