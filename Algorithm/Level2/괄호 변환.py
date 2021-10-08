"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 괄호 변환
description : 백트레킹
"""

from collections import deque


def check(p):
    stack = []

    for pare in p:
        if pare == "(":
            stack.append(pare)
        else:
            if len(stack) > 0:
                stack.pop()
            else:
                return False

    if len(stack) == 0:
        return True
    else:
        return False


def reverse(u):
    result = ""
    for p in u:
        if p == "(":
            result += ")"
        else:
            result += "("

    return result


def div_patch(p):
    queue = deque(p)
    left, right = 0, 0
    u = ""

    while queue:
        u += queue.popleft()

        if u[-1] == "(":
            left += 1
        else:
            right += 1

        if left == right:
            break

    v = "".join(list(queue))

    return u, v


def recursive(p):
    if len(p) == 0:
        return ""

    u, v = div_patch(p)

    if check(u) is True:
        return u + recursive(v)
    else:
        return "(" + recursive(v) + ")" + reverse(u[1: -1])


def solution(p):
    if check(p) is True:
        return p
    else:
        return recursive(p)
