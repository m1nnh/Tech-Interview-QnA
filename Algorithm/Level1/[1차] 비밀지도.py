"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 1차 비밀지도
description : 진법 변환
"""


def check(bin_number1, bin_number2):
    result = ""

    for i in range(len(bin_number1)):
        if bin_number1[i] == "1" or bin_number2[i] == "1":
            result += "#"
        else:
            result += " "

    return result


def solution(n, arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        bin_number1 = format(arr1[i], "b")
        bin_number2 = format(arr2[i], "b")

        # 앞에 0이 없을 때
        if len(bin_number1) != n:
            bin_number1 = (n - len(bin_number1)) * "0" + bin_number1
        if len(bin_number2) != n:
            bin_number2 = (n - len(bin_number2)) * "0" + bin_number2

        answer.append(check(bin_number1, bin_number2))

    return answer
