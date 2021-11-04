'''
상근이는 어렸을 적에 "봄보니 (Bomboni)" 게임을 즐겨했다.

가장 처음에 N×N크기에 사탕을 채워 놓는다. 사탕의 색은 모두 같지 않을 수도 있다.
 상근이는 사탕의 색이 다른 인접한 두 칸을 고른다. 그 다음 고른 칸에 들어있는 사탕을 서로 교환한다. 
 이제, 모두 같은 색으로 이루어져 있는 가장 긴 연속 부분(행 또는 열)을 고른 다음 그 사탕을 모두 먹는다.

사탕이 채워진 상태가 주어졌을 때, 상근이가 먹을 수 있는 사탕의 최대 개수를 구하는 프로그램을 작성하시오.
'''

# 상근이가 먹을 수 있는 사탕의 최대 개수 구하기

import sys
import copy

n = int(sys.stdin.readline())                      # 보드의 크기 n
board = [list(input()) for _ in range(n)]           # 보드 입력


def count(board):
    cnt = 1
    for i in range(n):
        candy_r = 1                         # 가로 사탕 개수
        candy_c = 1                         # 세로 사탕 개수
        for j in range(n - 1):
            # 가로로 사탕의 색이 같다면
            if board[i][j] == board[i][j + 1]:
                candy_r += 1
            # 가로로 사탕의 색이 다르다면
            if board[i][j] != board[i][j + 1]:
                cnt = max(cnt, candy_r)
                candy_r = 1                 # 다른 색을 만났기 때문에 사탕 색 1로 초기화
            
            # 세로로 사탕의 색이 같다면
            if board[j][i] == board[j + 1][i]:
                candy_c += 1
            # 세로로 사탕의 색이 다르다면
            if board[j][i] != board[j + 1][i]:
                cnt = max(cnt, candy_c)
                candy_c = 1                 # 다른 색을 만났기 때문에 사탕 색 1로 초기화
            
        cnt = max(cnt, candy_r, candy_c)

    return cnt


cnt_r = 1
cnt_c = 1

for i in range(n):
    for j in range(n - 1):

        # 가로가 다른 색일 경우 가로로 바꿔주기
        if board[i][j] != board[i][j + 1]:
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]  # 바꿔주기
            cnt_r = max(cnt_r, count(board))
            board[i][j], board[i][j + 1] = board[i][j + 1], board[i][j]  # 원상복귀
        # 세로가 다른 색일 경우 세로로 바꿔주기
        if board[j][i] != board[j + 1][i]:
            board[j][i], board[j + 1][i] = board[j + 1][i], board[j][i]  # 바꿔주기
            cnt_c = max(cnt_c, count(board))
            board[j][i], board[j + 1][i] = board[j + 1][i], board[j][i]  # 원상복귀

candy = max(cnt_r, cnt_c)
print(candy)