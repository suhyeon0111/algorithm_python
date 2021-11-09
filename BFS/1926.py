'''
어떤 큰 도화지에 그림이 그려져 있을 때, 그 그림의 개수와, 그 그림 중 넓이가 가장 넓은 것의 넓이를 출력하여라. 
단, 그림이라는 것은 1로 연결된 것을 한 그림이라고 정의하자. 가로나 세로로 연결된 것은 연결이 된 것이고 
대각선으로 연결이 된 것은 떨어진 그림이다. 
그림의 넓이란 그림에 포함된 1의 개수이다.

첫째 줄에 도화지의 세로 크기 n(1 ≤ n ≤ 500)과 가로 크기 m(1 ≤ m ≤ 500)이 차례로 주어진다. 
두 번째 줄부터 n+1 줄 까지 그림의 정보가 주어진다.
 (단 그림의 정보는 0과 1이 공백을 두고 주어지며, 0은 색칠이 안된 부분, 1은 색칠이 된 부분을 의미한다)
'''


import sys
from collections import deque

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

# 입력
n, m = map(int, sys.stdin.readline().split())
paper = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]

 
def bfs(x, y):
    queue = deque()  # 차례로 좌표를 확인해야함으로 fifo를 해야하기에 deque이용
    queue.append((x, y))

    paper[x][y] = 0  # 1을 만나면 0으로 바꿔서 방문했음을 표시
    cnt = 1  # 1의 개수를 저장할 cnt (1을 만났으니 1개부터 시작)
 
    while queue:
        x, y = queue.popleft()          

        # 4방향 탐색
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            
            # nx, ny가 범위내에 존재하면서 그림이 존재할 경우
            if 0 <= nx < n and 0 <= ny < m and paper[nx][ny] == 1:
                paper[nx][ny] = 0  # 그림(1)을 만나면 0으로 바꿔서 방문했음을 표시
                queue.append((nx, ny))  # 다음을 위해 해당 좌표 저장
                cnt += 1  # 그림의 개수 1증가
    
    return cnt  # 연결된 총 1의 개수 리턴
 


paint = []  # 그림의 넓이를 저장할 리스트

for i in range(n):
    for j in range(m):
        # 만약 그림이 존재한다면 
        if paper[i][j] == 1:
            area = bfs(i, j)  # 그림이 있는 좌표를 인자로 넘겨서 그림의 넓이(area) 저장
            paint.append(area)  # 그림의 개수를 리스트에 저장   
 

# 시간초과
if len(paint) == 0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))