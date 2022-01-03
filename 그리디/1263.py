'''
시간 관리

진영이는 캠프 조교를 온 후 효율적으로 시간 관리를 해야 한다는 것을 깨달았다. 
진영이는 하루에 해야 할 일이 총 N개가 있고 이 일들을 편하게 1번부터 N번까지 차례대로 번호를 붙였다.

진영이는 시간을 효율적으로 관리하기 위해, 할 일들에 대해 끝내야할 시간과 걸리는 시간을 적은 명단을 만들었다. 
즉, 이 명단은 i번째 일은 일을 처리하는데 정확히 Ti 시간이 걸리고 Si 시 내에 이 일을 처리하여야 한다는 것을 담고 있다. 
진영이는 0시부터 활동을 시작할 수 있고, 두 개 이상의 일을 같은 시간에 처리할 수 없다.

진영이가 바라는 점은 최대한 늦잠을 자는 것이다. 
문제는 이러한 진영이를 도와 일들은 모두 마감시간 내에 처리할 수 있는 범위 내에서 
최대한 늦게 일을 시작할 수 있는 시간이 몇 시인지 알아내는 것이다.
'''

import sys

n = int(sys.stdin.readline())   

time = []
for _ in range(n):
    t, s = map(int, sys.stdin.readline().split())  # t시간 소요, s시 시작
    time.append((s, t))
    
time.sort(reverse=True)  # s시간 내림차순 정렬

start = time[0][0] - time[0][1]  # 시작시간

# 가장 첫번째 인덱스인 0은 위에서 이미 계산해줬기에 1부터 시작
for i in range(1, n):
    if start < time[i][0]:  # 마감시간이 start보다 늦다면
        start -= time[i][1]  # 소요시간만큼 빼줌

    elif start > time[i][0]:  
        start = time[i][0] - time[i][1]  # 시작시간 다시 설정

if start >= 0:
    print(start)

else:
    print(-1)





# time = []
# for _ in range(n):
#     t, s = map(int, sys.stdin.readline().split())  # t시간 소요, s시 시작
#     time.append((t, s))
    
# time.sort(key=lambda x:(x[1], x[0]))  # s시간 순서대로 정렬

# start = time[n - 1][1] - time[n - 1][0] # 시작시간
# for i in range(n-1, -1, -1):
#     if time[i][1] > start:  # 마감시간이 start보다 늦다면








# 최대한 일을 늦게 시작하기를 원함 -> 가장 늦은 시작시간 출력
# 일을 끝낼 수 없다면 -1

