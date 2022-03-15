'''
모두의 마블
'''

from sys import stdin

n = int(stdin.readline())
level = list(map(int, stdin.readline().split()))

level.sort(reverse=True)

gold = 0
high_level = level[0]
for i in range(1, n):
    if high_level < level[i]:
        high_level = level[i]
    g = high_level + level[i]
    gold += g

print(gold)
