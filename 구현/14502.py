# 연구소
# 시간초과

import sys
import copy
from collections import deque

lab = []

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

max_result = 0  # 기준 값


def bfs():
    global max_result
    q = deque()
    matrix = copy.deepcopy(lab)
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 2:  # 바이러스 위치 저장
                q.append((i, j))
    while q:
        x, y = q.popleft()
        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # nx, ny가 범위 안에 있으면서 바이러스가 없을 때
            if 0 <= nx < n and 0 <= ny < m and matrix[nx][ny] == 0:
                matrix[nx][ny] = 2
                q.append((nx, ny))
    result = 0
    for i in range(n):
        result += matrix[i].count(0)

    max_result = max(max_result, result)


def wall(wall_cnt):
    if wall_cnt == 3:  # 벽 3개 다 세웠을 때
        bfs()
        return
    for i in range(n):
        for j in range(m):
            if lab[i][j] == 0:
                lab[i][j] = 1
                wall(wall_cnt + 1)
                lab[i][j] = 0


n, m = map(int, sys.stdin.readline().split())
for _ in range(n):
    lab.append(list(map(int, sys.stdin.readline().split())))
wall(0)
print(max_result)
