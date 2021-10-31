import sys

#상근이 카드 N개
N = int(sys.stdin.readline())
N_card = list(map(int, sys.stdin.readline().split()))
#새로운 카드 M개
M = int(sys.stdin.readline())   
M_card = list(map(int, sys.stdin.readline().split()))

#정렬
N_card.sort()

#새로 담아줄 list
result = []

#비교해주기
for i in range(len(M_card)):
    start = 0
    end = len(N_card) - 1

    #무조건 0을 넣어주기
    result.append(0)    
    while start <= end:
        #중간 값을 중심으로 탐색하기
        mid = (start + end) // 2
    
        #중간 값과 같은 값이 있다면 0을 빼주고 1을 넣어줌, 다음 M_card를 탐색하기 위해 루프를 탈출
        if N_card[mid] == M_card[i]: 
            result.pop()
            result.append(1) 
            break     
        
        #중간 값이 M_card보다 크다면 end를 감소 후, 다시 탐색
        elif N_card[mid] > M_card[i]:
            end = mid - 1 #end 위치 바꿔주기

        #중간 값이 M_card보다 작다면 start를 증가 후, 다시 탐색
        elif N_card[mid] < M_card[i]:
            start = mid + 1 #start 위치 바꿔주기

#list출력 시 괄호, 쉼표 없이 출력
cardresult = " ".join(map(str, result))
print(cardresult)