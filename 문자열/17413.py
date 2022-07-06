# 단어뒤집기2
import sys

s = list(map(str, sys.stdin.readline().strip()))

result = ""
word = ""
reverse = True

for x in s:
    if x == '<':
        reverse = False
        result += word
        word = x

    elif x == '>':
        reverse = True
        result += (word + '>')
        word = ""

    elif x == ' ':
        result += word + x
        word = ""

    elif reverse:
        word = x + word

    else:
        word += x

result += word
print(result)
