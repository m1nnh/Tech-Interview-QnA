"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 크레인 인형뽑기 게임
description : 스택
"""


def solution(board, moves):
    answer = 0
    stack = []
    new_board = []

    for i in range(len(board[0])):
        temp = []
        for j in range(len(board)):
            if board[j][i] != 0:
                temp.append(board[j][i])
        new_board.append(temp)

    for move in moves:
        if len(new_board[move - 1]) != 0:
            now = new_board[move - 1].pop(0)

            if len(stack) != 0:
                if stack[-1] == now:
                    answer += 2
                    stack.pop()
                else:
                    stack.append(now)
            else:
                stack.append(now)
        else:
            continue

    return answer
