'''
회문(回文) 또는 팰린드롬(palindrome)은 앞 뒤 방향으로 볼 때 같은 순서의 문자로 구성된 문자열을 말한다. 
예를 들어 ‘abba’ ‘kayak’, ‘reviver’, ‘madam’은 모두 회문이다. 만일 그 자체는 회문이 아니지만 한 문자를 삭제하여
 회문으로 만들 수 있는 문자열이라면 우리는 이런 문자열을 “유사회문”(pseudo palindrome)이라고 부른다. 
 예를 들어 ‘summuus’는 5번째나 혹은 6번째 문자 ‘u’를 제거하여 ‘summus’인 회문이 되므로 유사회문이다.

여러분은 제시된 문자열을 분석하여 그것이 그 자체로 회문인지, 또는 한 문자를 삭제하면 회문이 되는 “유사회문”인지, 
아니면 회문이나 유사회문도 아닌 일반 문자열인지를 판단해야 한다. 만일 문자열 그 자체로 회문이면 0, 유사회문이면 1, 
그 외는 2를 출력해야 한다. 
'''
def palindrome(word, left, right):
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1
        else:
            return 2
    return 1

def judge_palindrome(word, left, right):
    cnt = 0  # 유사회문 구별해줄 변수
    # 회문 검사
    while left < right:
        if word[left] == word[right]:
            left += 1
            right -= 1

        # 회문이 아니므로 유사회문인지 검사
        else:
            result1 = palindrome(word, left + 1, right)
            result2 = palindrome(word, left, right - 1)
            if result1 == 1 or result2 == 1:
                return 1
            else:
                return 2 
    return 0


t = int(input())
str_arr = [list(input()) for _ in range(t)]

for x in str_arr:
    left = 0
    right = len(x) - 1
    result =  judge_palindrome(x, left, right)
    print(result)











# # 회문 판단하는 함수
# def judge_palindrome(input1):
#     length = len(input1)  # 문자열 길이
#     for i in range(int(length/2)):
#         if input1[i] == input1[length - 1 - i]:
#             continue
        
#         # 문자열이 다르다면
#         else:
#             # 유사회문인지 검사
#             if input1[i] == input1[length - 2 - i] or input1[i + 1] == input1[length - 1 - i]:
#                 return 1
#             else:
#                 return 2
#     # 회문일 때
#     return 0


# result = []
# for x in str_arr:
#     a =  judge_palindrome(x)
#     print(a)


    