'''
바닥 장식
형택이는 건축가이다. 지금 막 형택이는 형택이의 남자 친구 기훈이의 집을 막 완성시켰다. 형택이는 기훈이 방의 바닥 장식을 디자인했고, 이제 몇 개의 나무 판자가 필요한지 궁금해졌다. 나무 판자는 크기 1의 너비를 가졌고, 양수의 길이를 가지고 있다. 기훈이 방은 직사각형 모양이고, 방 안에는 벽과 평행한 모양의 정사각형으로 나누어져 있다.

이제 ‘-’와 ‘|’로 이루어진 바닥 장식 모양이 주어진다. 만약 두 개의 ‘-’가 인접해 있고, 같은 행에 있다면, 두 개는 같은 나무 판자이고, 두 개의 ‘|’가 인접해 있고, 같은 열에 있다면, 두 개는 같은 나무 판자이다.

기훈이의 방 바닥을 장식하는데 필요한 나무 판자의 개수를 출력하는 프로그램을 작성하시오.
'''

from sys import stdin


n, m = map(int, stdin.readline().split())
bottom = [list(stdin.readline()) for _ in range(n)]
cnt = 0  # 나무 판자 개수

# 가로 체크
check = 0  # 연달아 존재하는지 체크
for i in range(n):
    for j in range(m):
        if bottom[i][j] == '-':
            check += 1
        elif bottom[i][j] != '-' and check > 0:
            cnt += 1
            check = 0
    if check > 0:
        cnt += 1
        check = 0

# 세로 체크
check = 0  # 연달아 존재하는지 체크
for i in range(m):
    for j in range(n):
        if bottom[j][i] == '|':
            check += 1
        elif bottom[j][i] != '|' and check > 0:
            cnt += 1
            check = 0
    if check > 0:
        cnt += 1
        check = 0

print(cnt)


# for i in range(n - 1):
#     for j in range(m):
#         if bottom[i][j] == '|' and bottom[i + 1][j] == '|':  # '|'이 같은 행에 연속으로 2개가 있다면
#             bottom[i][j] = '.'
#             bottom[i + 1][j] = '.'  # 방문 했음
#             cnt += 1  # 판자 개수 늘려주기
#         elif bottom[i][j] == '|':
#             bottom[i][j] = '.'
#             cnt += 1
# print(cnt)

# cnt = 0  # 나무 판자 개수
# for i in range(n):
#     for j in range(m):
#         if bottom[i][j] == '-' and bottom[i][j + 1] == '-':
#             bottom[i][j] = '.'
#             bottom[i][j + 1] = '.'  # 방문 했음
#             cnt += 1  # 판자 개수 늘려주기

#         elif bottom[i][j] == '|' and bottom[i + 1][j] == '|':
#             bottom[i][j] = '.'
#             bottom[i + 1][j] = '.'  # 방문 했음
#             cnt += 1

#         else:
#             bottom[i][j] = '.'

# print(cnt)
