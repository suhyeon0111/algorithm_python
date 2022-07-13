# 미로탐색

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
matrix = [list(map(int, ' '.join(input()).split())) for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

q = deque()
q.append((0, 0))  # 출발

while q:
    x, y = q.popleft()

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < n and 0 <= ny < m:
            if matrix[nx][ny] == 1:
                matrix[nx][ny] = matrix[x][y] + 1
                q.append((nx, ny))

print(matrix[n - 1][m - 1])
