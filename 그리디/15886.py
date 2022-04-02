from sys import stdin

n = int(stdin.readline())
apple = stdin.readline()
cnt = 1
for i in range(1, n):
    if apple[i]=='E':
        if apple[i-1]=='W':
            cnt +=1
print(cnt)