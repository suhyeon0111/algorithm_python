'''
실험실에서 새로운 종의 벌레 한 마리가 탄생하였다. 
벌레는 스스로 분열하며, 분열하면 자기 자신과 같은 벌레를 한 마리 만들어 내게 된다. 벌레가 분열하는 규칙은 다음과 같다.

벌레는 기준년도 1년 2월에 1마리가 탄생한다.
벌레는 매년 1월이 되면 분열한다. 분열시 본래의 개체는 그대로, 새로운 개체가 하나 탄생하는 것으로 본다.
홀수년도에 탄생한 개체는 3번 분열시, 짝수년도에 탄생한 개체는 4번 분열시 사망한다.
예를 들어, 기준년도 1년 2월에 존재하던 벌레는, 2년 1월, 3년 1월, 4년 1월에 분열하고 사망하여 4년 말에는 존재하지 않게 된다. 이 때, N년 말에 존재하는 벌레의 수를 구하여라
'''

import sys

n = int(sys.stdin.readline())  # n년말에 존재하는 벌레의 수

dp = [0 for _ in range(50)]

dp[0] = 1  # 4년일 때 1년에 태어난 벌레 삭제하기 위해서
dp[1] = 1  # 1년 1마리 탄생

for i in range(2, n + 1):
    if i % 2 == 1:  # 홀수일 때
        dp[i] = dp[i - 1] * 2
    elif i % 2 == 0:  # 짝수일 때
        dp[i] = dp[i - 1] * 2 - (dp[i - 5] + dp[i - 4])
        
print(dp[n])
