'''
배열돌리기1
반시계방향으로 돌림
r번 회전시킨 결과출력
'''


import sys

n, m, r = map(int, sys.stdin.readline().split())
matrix = [list(map(int, sys.stdin.readline.split())) for _ in range(n)]

# r번 회전
for _ in range(r):
    # 돌려지는 네모 개수 만큼 for루프 돌음
    for i in range(min(n, m) // 2):
        x, y = i, i
        temp = matrix[x][y]
        # 내부에 있는 네모를 위해 n-i랑 m-i까지 범위 설정

        for j in range(i + 1, n - i):  # 왼쪽 면
            x = j
            pre_temp = matrix[x][y]
            matrix[x][y] = temp
            temp = pre_temp

        for j in range(i + 1, m - i):  # 아래 면
            y = j
            pre_temp = matrix[x][y]
            matrix[x][y] = temp
            temp = pre_temp

        for j in range(i + 1, n - i):  # 오른쪽 면
            x = n - j - 1
            pre_temp = matrix[x][y]
            matrix[x][y] = temp
            temp = pre_temp

        for j in range(i + 1, m - i):  # 윗 면
            y = m - j - 1
            pre_temp = matrix[x][y]
            matrix[x][y] = temp
            temp = pre_temp

for i in range(n):
    for j in range(m):
        print(matrix[i][j], end=' ')
    print()