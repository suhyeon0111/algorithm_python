'''
파일 합치기3
'''

from sys import stdin
import heapq

t = int(stdin.readline())  # t개의 데이터
for _ in range(t):
    k = int(stdin.readline())  # k장
    file_size = list(map(int, stdin.readline().split()))  # 각 장 수의 크기
    heapq.heapify(file_size)  # 최소힙으로 변환
    result = 0

    while len(file_size) >= 2:  # 파일 크기가 1개가 될 때까지
        one = heapq.heappop(file_size)
        two = heapq.heappop(file_size)
        result += (one + two)  # 가장 작은 파일 크기 2개 빼서 더한 후 다시 힙에 넣기
        heapq.heappush(file_size, (one + two))
    
    print(result)