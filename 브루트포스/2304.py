import sys


N = int(sys.stdin.readline()) 

#기둥의 정보를 한번에 담을 list선언
Pillar = [] 

for i in range(N):
    L, H = list(map(int, sys.stdin.readline().split()))
    Pillar.append([L, H])


#1번째 인덱스에 대해서만 내림차순 정렬(높이에 대해 오름차순)
Pillar.sort( key=lambda x: -x[1])


max_height = Pillar[0][1]#가장 높은 기둥의 높이
min_height = Pillar[1][1]#그 다음 높은 기둥의 높이

L_start = Pillar[0][0] #가장 높은 기둥의 가로 시작점
#max_l = max(Pillar[0][0],Pillar[0][1]) #그 다음 기둥의 가로 시작점

Area = max_height - min_height
print(Area)

for i in range(1, len(Pillar)):
    h = Pillar[i][1]
    l = Pillar[i][0]    

    if  L_start > l and l < max_l:
        continue
    else:
        max_l = l
        L_area = abs(max_l - L_start) + 1 #직사각형의 가로 길이

        if max_l == Pillar[-1][0]:
            Area += ((min_height) * L_area) #직사각형의 넓이
            break

        else:
            Area += ((max_height - min_height) * L_area) #직사각형의 넓이

            max_height = min_height 
            min_height = h

        


print(Area)

