'''
욱제는 결정장애야!!
'''
from sys import stdin

n = int(stdin.readline())
choice = list(map(int, stdin.readline().split()))
board = []
cnt = 0
max_cnt = 0

for i in choice:
    if i not in board:
        board.append(i)  # 스티커 붙이기
        cnt += 1
    else:
        cnt -= 1  # 스티커 떼기
    max_cnt = max(max_cnt, cnt)  # 가장 많이 스티커가 붙어있을 경우 비교

print(max_cnt)
