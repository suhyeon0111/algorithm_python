'''
풍선맞추기
'''

from sys import stdin

n = int(stdin.readline())
balloon = list(map(int, stdin.readline().split()))
cnt = 0  # 화살 개수


arrow = [0] * 1000001
for i in range(n):
    if arrow[balloon[i]] == 0:  
        arrow[balloon[i] - 1] += 1  # 새로운 화살을 써서 화살 
        cnt += 1
    else:
        arrow[balloon[i]] -= 1  # 화살 높이가 -1이 되었으니 해당 인덱스에서 삭제
        arrow[balloon[i] - 1] += 1  # 화살의 개수 늘려주기


print(cnt)
