'''
사과나무
'''

from sys import stdin

n = int(stdin.readline())
tree = list(map(int, stdin.readline().split()))
cnt = sum(tree) // 3  # 1과 2의 개수

if sum(tree) % 3 == 0:
    for x in tree:
        cnt -= (x // 2)  # 2의 개수 세기
    if cnt > 0:
        print('NO')
    else:
        print('YES')

else:
    print('NO')
