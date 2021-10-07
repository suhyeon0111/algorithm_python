'''

자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오.

1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
'''

import sys

n, m = map(int, sys.stdin.readline().split()) #n:자연수 , m개를 고르기
number = []


 #깊이, 
def backtracking(number, n, m):
    #종료
    if len(number) == m:
        #출력
        result = " ".join(map(str, number)) 
        print(result)
       
    else:
        for i in range(1, n + 1):
            number.append(i)
            backtracking(number, n, m)
            number.pop() #초기화


backtracking(number, n, m)



