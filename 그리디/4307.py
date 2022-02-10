'''
개미
'''

from sys import stdin

t = int(stdin.readline())
for _ in range(t):
    l, n = map(int, stdin.readline().split())
    stick = [0 for _ in range(l + 1)]
    ants = [int(stdin.readline()) for _ in range(n)]
    short_time = 0
    long_time = 0
    for x in ants:
        if x > l - x:
            if short_time < l - x:
                short_time = l - x
            if long_time < x:
                long_time = x
        else:
            if short_time < x:
                short_time = x
            if long_time < l - x:
                long_time = l - x
    print(short_time, long_time)
