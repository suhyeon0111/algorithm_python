'''
겉넓이 구하기
'''
from sys import stdin


n, m = map(int, stdin.readline().split())
box = [list(map(int, stdin.readline().split())) for _ in range(n)]

up = n * m  # 위에서 바라봤을 때 넓이

left = 0
for i in range(n):
    for j in range(m):
        if j == 0:  # 맨 앞에 위치한 도형이라면
            left += box[i][j]  # 그 도형 높이만큼 더해주기
        else:
            if box[i][j-1] < box[i][j]:  # 앞에 있는 기둥보다 뒷 기둥의 높이가 높다면
                left += box[i][j] - box[i][j-1]  # 차이 나는 높이만큼 더해줌

front = 0
for j in range(m):
    for i in range(n):
        if i == 0:
            front += box[i][j]
        else:
            if box[i-1][j] < box[i][j]:
                front += box[i][j] - box[i-1][j]

result = 2 * (up + left + front)
print(result)
