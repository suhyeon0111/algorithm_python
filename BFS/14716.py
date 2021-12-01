'''
현수막 문제

ANT가 처음 알고리즘 대회를 개최하게 되면서 현수막을 내걸었다.

저번 학기 영상처리 수업을 듣고 배웠던 지식을 최대한 응용 해보고 싶은 혁진이는 이 현수막에서 글자가 몇 개인지 알아보는 프로그램을 만들려 한다.

혁진이는 우선 현수막에서 글자인 부분은 1, 글자가 아닌 부분은 0으로 바꾸는 필터를 적용하여 값을 만드는데 성공했다.

그런데 혁진이는 이 값을 바탕으로 글자인 부분 1이 상, 하, 좌, 우, 대각선으로 인접하여 서로 연결되어 있다면 한 개의 글자라고 생각만 하였다.

혁진이가 필터를 적용하여 만든 값이 입력으로 주어졌을 때, 혁진이의 생각대로 프로그램을 구현하면 글자의 개수가 몇 개인지 출력하여라.
'''

import sys
from collections import deque

# 입력
m, n = map(int, sys.stdin.readline().split())
letter = [list(map(int, sys.stdin.readline().split())) for _ in range(m)]

dx = [1, -1, 0, 0, 1, 1, -1, -1]
dy = [0, 0, 1, -1, 1, -1, 1, -1]


# BFS함수
def bfs(i, j):
    q = deque()
    q.append([xi, yj])
    letter[xi][yj] = 0

    while q:
        x, y = q.popleft()
        
        for i in range(8):
            nx = x + dx[i]  
            ny = y + dy[i]  
            if 0 <= nx < m and 0 <= ny < n and letter[nx][ny] == 1:
                q.append([nx, ny])
                letter[nx][ny] = 0


cnt = 0  # 글자 횟수
for i in range(m):
    for j in range(n):
        if letter[i][j] == 1:
            bfs(i, j) 
            cnt += 1  


print(cnt)