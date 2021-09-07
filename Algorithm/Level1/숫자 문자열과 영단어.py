"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 숫자 문자열과 영단어
description : 딕셔너리
"""


def solution(s):
    answer = ""
    number_dic = {"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4",
                  "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    result = ""

    for st in s:
        if st.isdigit():
            answer += st
        else:
            result += st
            if result in number_dic:
                answer += number_dic[result]
                result = ""

    return int(answer)
