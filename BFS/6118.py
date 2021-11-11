'''
재서기는 수혀니와 교외 농장에서 숨바꼭질을 하고 있다. 농장에는 헛간이 많이 널려있고 재서기는 그 중에 하나에 숨어야 한다. 
헛간의 개수는 N(2 <= N <= 20,000)개이며, 1 부터 샌다고 하자.  

재서기는 수혀니가 1번 헛간부터 찾을 것을 알고 있다. 
모든 헛간은 M(1<= M <= 50,000)개의 양방향 길로 이어져 있고, 그 양 끝을 A_i 와 B_i(1<= A_i <= N; 1 <= B_i <= N; A_i != B_i)로 나타낸다. 
또한 어떤 헛간에서 다른 헛간으로는 언제나 도달 가능하다고 생각해도 좋다. 

재서기는 발냄새가 지독하기 때문에 최대한 냄새가 안나게 숨을 장소를 찾고자 한다. 
냄새는 1번 헛간에서의 거리(여기서 거리라 함은 지나야 하는 길의 최소 개수이다)가 멀어질수록 감소한다고 한다. 
재서기의 발냄새를 최대한 숨길 수 있는 헛간을 찾을 수 있게 도와주자!
'''
# 인접 행렬로 풀이

import sys
from collections import deque

def bfs(node):
    queue = deque()
    queue.append(node)  # 해당 노드 넣어주고
    visit[node] = 1  # 방문했음을 1로 표시

    while queue:  
        node = queue.popleft()  # 다음 노드 꺼내주기
        
        # 다른 헛간들을 돌면서 방문하지 않았을 경우 방문표시해주기
        for x in barn[node]: 
            if visit[x] == 0:  # n번 헛간을 방문하지 않았다면 
                visit[x] = visit[node] + 1  # 방문함과 동시에 거리를 넣어줌
                queue.append(x)  # 다음 탐색을 위해 append

# 입력
n, m = map(int, input().split())
barn = [[] for _ in range(n + 1)]


# 인접 리스트로 구현
for _ in range(m):
    i, j = map(int, input().split())
    barn[i].append(j)
    barn[j].append(i)

visit = [0] * (n + 1)  # 방문 표시
bfs(1)  # 헛간 1번부터 시작

m = max(visit)  #가장 먼 거리
print(visit.index(m), m-1, visit.count(m))  # 가장 먼 거리의 인덱스, 처음 방문했음에 1을 넣어줬기때문에 m-1, 거리가 m인 헛간의 개수