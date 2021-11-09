'''
미키의 뒷마당에는 특정 수의 양이 있다. 그가 푹 잠든 사이에 배고픈 늑대는 마당에 들어와 양을 공격했다.

마당은 행과 열로 이루어진 직사각형 모양이다. 글자 '.' (점)은 빈 필드를 의미하며, 글자 '#'는 울타리를, 'o'는 양, 'v'는 늑대를 의미한다.

한 칸에서 수평, 수직만으로 이동하며 울타리를 지나지 않고 다른 칸으로 이동할 수 있다면, 두 칸은 같은 영역 안에 속해 있다고 한다. 마당에서 "탈출"할 수 있는 칸은 어떤 영역에도 속하지 않는다고 간주한다.

다행히 우리의 양은 늑대에게 싸움을 걸 수 있고 영역 안의 양의 수가 늑대의 수보다 많다면 이기고, 늑대를 우리에서 쫓아낸다. 그렇지 않다면 늑대가 그 지역 안의 모든 양을 먹는다.

맨 처음 모든 양과 늑대는 마당 안 영역에 존재한다.

아침이 도달했을 때 살아남은 양과 늑대의 수를 출력하는 프로그램을 작성하라.
'''


import sys
from collections import deque

# 탐색
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

# 입력
r, c = map(int,sys.stdin.readline().split())
yard = [list(input()) for _ in range(r)]


# dfs함수
def bfs(x, y):
    queue = deque()  # fifo를 해야하기에 deque를 씀
    queue.append((x,y))
    wolf = sheep = 0

    if yard[x][y] == 'o':  # 양 발견
        sheep += 1
                    
    if yard[x][y] == 'v':  # 늑대 발견
        wolf += 1  

    yard[x][y] = '#'  # 방문 표시


    while queue:
        i, j = queue.popleft()  # 큐에서 좌표 빼주기

        # 4방향 탐색
        for k in range(4):
            nx = i + dx[k]
            ny = j + dy[k]

            # nx와 ny가 범위내에 존재하고 울타리가 없다면
            if 0 <= nx < r and 0 <= ny < c and yard[nx][ny] != "#":
                if yard[nx][ny] == 'o':  # 양 발견
                    sheep += 1
                    
                if yard[nx][ny] == 'v':  # 늑대 발견
                    wolf += 1  

                yard[nx][ny] = '#'  # 방문함
                queue.append((nx, ny))  # 다음 탐색을 위해 좌표저장

    # 울타리 안에 있는 양과 늑대의 마리 수 결정됨
    # 양의 수가 늑대 수보다 많다면 늑대를 쫓아냄
    if sheep > wolf:                          
        wolf = 0

    # 양의 수가 늑대 수보다 적다면 늑대한테 잡아먹힘
    elif sheep <= wolf:
        sheep = 0

    return sheep, wolf


# 결과 출력할 양과 늑대 수를 저장할 변수
result_sheep = 0
result_wolf = 0


for i in range(r):
    for j in range(c):
        
        # 양 또는 늑대를 발견했을 때
        if yard[i][j] == 'o' or yard[i][j] == 'v':
                sheep, wolf = bfs(i, j)  # bfs돌고 난 후 같은 필드에 있는 양과 늑대의 개수 저장
                result_sheep += sheep
                result_wolf += wolf
            

# 결과 출력
print(result_sheep, result_wolf)