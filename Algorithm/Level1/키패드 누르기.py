"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 키패드 누르기
description : 구현
"""


def check(left_and_right, dic_number):
    return abs(left_and_right[0] - dic_number[0]) + abs(left_and_right[1] - dic_number[1])


def solution(numbers, hand):
    answer = ''

    index_dic = {1: [0, 0], 2: [0, 1], 3: [0, 2],
                 4: [1, 0], 5: [1, 1], 6: [1, 2],
                 7: [2, 0], 8: [2, 1], 9: [2, 2],
                 "*": [3, 0], 0: [3, 1], "#": [3, 2]}

    left, right = index_dic["*"], index_dic["#"]

    for number in numbers:
        if number in [1, 4, 7]:
            answer += "L"
            left = index_dic[number]
        elif number in [3, 6, 9]:
            answer += "R"
            right = index_dic[number]
        else:
            if check(left, index_dic[number]) < check(right, index_dic[number]):
                answer += "L"
                left = index_dic[number]
            elif check(left, index_dic[number]) > check(right, index_dic[number]):
                answer += "R"
                right = index_dic[number]
            else:
                if hand == "right":
                    answer += "R"
                    right = index_dic[number]
                else:
                    answer += "L"
                    left = index_dic[number]

    return answer
