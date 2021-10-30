import sys

board = input() 

board = board.replace('XXXX', 'AAAA')           
board = board.replace('XX', 'BB')

if board.count('X') > 0:                # 남아있는 x가 있을 경우
    board = -1

print(board)
