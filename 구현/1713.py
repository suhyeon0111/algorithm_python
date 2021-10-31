# 월드초등학교 학생회장 후보는 일정 기간 동안 전체 학생의 추천에 의하여 정해진 수만큼 선정된다. 그래서 학교 홈페이지에 추천받은 학생의 사진을 게시할 수 있는 사진틀을 후보의 수만큼 만들었다. 추천받은 학생의 사진을 사진틀에 게시하고 추천받은 횟수를 표시하는 규칙은 다음과 같다.

# 학생들이 추천을 시작하기 전에 모든 사진틀은 비어있다.
# 어떤 학생이 특정 학생을 추천하면, 추천받은 학생의 사진이 반드시 사진틀에 게시되어야 한다.
# 비어있는 사진틀이 없는 경우에는 현재까지 추천 받은 횟수가 가장 적은 학생의 사진을 삭제하고, 그 자리에 새롭게 추천받은 학생의 사진을 게시한다. 이때, 현재까지 추천 받은 횟수가 가장 적은 학생이 두 명 이상일 경우에는 그러한 학생들 중 게시된 지 가장 오래된 사진을 삭제한다.
# 현재 사진이 게시된 학생이 다른 학생의 추천을 받은 경우에는 추천받은 횟수만 증가시킨다.
# 사진틀에 게시된 사진이 삭제되는 경우에는 해당 학생이 추천받은 횟수는 0으로 바뀐다.
# 후보의 수 즉, 사진틀의 개수와 전체 학생의 추천 결과가 추천받은 순서대로 주어졌을 때, 최종 후보가 누구인지 결정하는 프로그램을 작성하시오.


import sys
from collections import deque


n = int(sys.stdin.readline()) #사진 틀 개수
m = int(sys.stdin.readline()) #전체 학생의 총 추천 횟수
recommend_num = list(map(int, sys.stdin.readline().split()))#추천받은 학생을 나타내는 번호

cnt = 0 #사진틀 개수
frame = deque([]) #액자에 들어간 후보 집어넣을 리스트
recommend = [0] * 10 #추천횟수 집어넣을 리스트

    
for x in recommend_num:
    
    if x in frame: # 사진틀에 존재한다면
        recommend[x] += 1 #추천횟수 증가

    else: #사진틀에 존재하지않다면
        if len(frame) == 3: #사진틀이 차있다면
            small = min(frame) #추천수가 가장 작은 액자의 추천수
            i = frame.index(small) #가장 작은 추천수의 액자 인덱스

            if recommend[x] > small: #현재 추천수와 가장 작은 추천수의 액자의 비교
                frame.remove(small) #더 작은 추천수 액자 지우기
                recommend[i] = 0 #추천횟수 초기화
                continue


            elif recommend[x] == small: #작은 추천수가 같다면
                frame.popleft() #가장 오래된 액자 지우기
                recommend[i] = 0 #추천횟수 초기화
                continue

        frame.append(x) #사진틀 개시
        recommend[x] += 1 #추천수 증가


print(frame)
