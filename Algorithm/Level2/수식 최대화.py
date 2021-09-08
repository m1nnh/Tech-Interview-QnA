"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 수식 최대화
description : 조합, 완전 탐색
"""

from itertools import permutations
from collections import deque


def calc(comb, expression_list):
    queue = deque(expression_list)

    for op in comb:
        flag = False
        num_stack = []
        op_stack = []

        while queue:
            now = queue.popleft()
            if type(now) == type(0):
                if flag is True:
                    total = 0
                    if op == "+":
                        num_stack.append(num_stack.pop() + now)
                    elif op == "-":
                        num_stack.append(num_stack.pop() - now)
                    else:
                        num_stack.append(num_stack.pop() * now)
                else:
                    num_stack.append(now)
            else:
                if now == op:
                    flag = True
                else:
                    flag = False
                    op_stack.append(now)

        for j in range(len(num_stack)):
            queue.append(num_stack[j])
            if j + 1 == len(num_stack):
                break
            queue.append(op_stack[j])

    return queue.popleft()


def solution(expression):
    answer = 0
    expression_list = []
    num = ""

    for s in expression:
        if s.isdigit():
            num += s
        else:
            expression_list.append(int(num))
            expression_list.append(s)
            num = ""

    expression_list.append(int(num))

    operations = ["+", "-", "*"]
    comb_op = list(permutations(operations, 3))

    for comb in comb_op:
        answer = max(answer, abs(calc(comb, expression_list)))

    return answer
