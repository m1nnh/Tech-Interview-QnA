"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : [1차] 프렌즈 4블록
description : 구현
"""

import copy


def destroy_block(board):
    cp_board = copy.deepcopy(board)

    for i in range(1, len(cp_board)):
        for j in range(1, len(cp_board[0])):
            if board[i][j] == -1:
                continue

            if board[i][j] == board[i - 1][j] == board[i][j - 1] == board[i - 1][j - 1]:
                cp_board[i][j], cp_board[i - 1][j], cp_board[i][j - 1], cp_board[i - 1][j - 1] = 0, 0, 0, 0

    total = 0
    for i in range(len(cp_board)):
        count = cp_board[i].count(0)
        if count == 0:
            continue

        col_list = [-1] * count
        total += count

        for j in range(len(cp_board[0])):
            if cp_board[i][j] != 0:
                col_list.append(cp_board[i][j])

        cp_board[i] = col_list

    return cp_board, total


def solution(m, n, board):
    answer = 0
    new_board = [list(b) for b in zip(*board)]

    while True:
        new_board, count = destroy_block(new_board)

        if count == 0:
            break

        answer += count

    return answer
