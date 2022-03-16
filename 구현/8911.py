'''
거북이
'''

from sys import stdin

# 북 서 남 동
dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]

t = int(stdin.readline())
order = []
for i in range(t):
    move = stdin.readline()
    x = 0
    y = 0
    dir = 0
    location = [(x, y)]
    for j in move:
        if j == 'F':
            x += dx[dir]
            y += dy[dir]

        elif j == 'L':
            if dir == 3:
                dir = 0
            else:
                dir += 1

        elif j == 'B':
            x -= dx[dir]
            y -= dy[dir]

        elif j == 'R':
            if dir == 0:
                dir = 3
            else:
                dir -= 1

        location.append((x, y))
    width = max(location, key=lambda x: x[0])[
        0] - min(location, key=lambda x: x[0])[0]
    height = max(location, key=lambda x: x[1])[
        1] - min(location, key=lambda x: x[1])[1]
    print(width * height)
