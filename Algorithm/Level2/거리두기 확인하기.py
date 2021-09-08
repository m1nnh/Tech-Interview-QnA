"""
author : Park Min Hyeok
github : https://github.com/m1nnh
e-mail : alsgur9784@naver.com

title : 거리두기 확인하기
description : BFS, 완전 탐색
"""

from collections import deque


def check(x, y, place):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))
    visited = [[False for _ in range(5)] for _ in range(5)]
    visited[x][y] = True

    while queue:
        now_x, now_y = queue.popleft()

        for i in range(4):
            nx = now_x + dx[i]
            ny = now_y + dy[i]
            if 0 <= nx < 5 and 0 <= ny < 5:
                if visited[nx][ny] is False:
                    dist = abs(nx - x) + abs(ny - y)
                    if place[nx][ny] != "X" and dist <= 2:
                        if place[nx][ny] == "P":
                            return False
                        else:
                            queue.append((nx, ny))
                            visited[nx][ny] = True

    return True


def solution(places):
    answer = []

    for place in places:
        flag = True
        for i in range(5):
            for j in range(5):
                if place[i][j] == "P":
                    if check(i, j, place) is False:
                        flag = False
                        break
            if flag is False:
                break

        if flag is True:
            answer.append(1)
        else:
            answer.append(0)

    return answer
