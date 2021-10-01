import sys

N = int(sys.stdin.readline()) 

#기둥의 정보를 한번에 담을 list선언
Pillar = [] 

#입력받기
for i in range(N):
    L, H = list(map(int, sys.stdin.readline().split()))
    Pillar.append([L, H])


#0번째 인덱스에 대해서만 오름차순 정렬
Pillar.sort(key=lambda x: x[0])

#가장 높은 기둥 찾기
high_H = Pillar[0][1] 
for i in range(1, len(Pillar)):
    #다른 기둥이 더 클 경우
    if high_H <= Pillar[i][1]:
        high_H = Pillar[i][1] #더 큰 기둥으로 바꿔주기
        high_H_index = i #가장 큰 기둥의 인덱스 저장

#왼쪽 탐색
height = Pillar[0][1]
min_L = Pillar[0][0]
Area = Pillar[high_H_index][1]

for i in range(high_H_index + 1):     
    if height <= Pillar[i][1]:
        Area_L = Pillar[i][0] - min_L
        Area += (height * Area_L)
        height = Pillar[i][1]
        min_L = Pillar[i][0]

#오른쪽 탐색
height_R = Pillar[-1][1]  
max_L = Pillar[-1][0]

for i in range(len(Pillar)-1, high_H_index - 1, -1):
    if height_R <= Pillar[i][1]:
        Area_L = max_L - Pillar[i][0]
        Area += (height_R * Area_L)
        height_R = Pillar[i][1]
        max_L = Pillar[i][0]


print(Area)



