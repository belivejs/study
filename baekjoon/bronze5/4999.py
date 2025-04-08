import re

jae = input()
docter = input()

# 두 문자열은 모두 a와 h로만 이루어져 있다.
pattern = '[^ah]'
jae_result = re.findall(pattern=pattern, string=jae)
docter_result = re.findall(pattern=pattern, string=docter)

if jae_result:
    raise Exception('재환이의 입력값은 a와 h로만 이루어져야 합니다')

if docter_result:
    raise Exception('의사의 입력값은 a와 h로만 이루어져야 합니다')

# a의 개수는 0보다 크거나 같고, 99보다 작거나 같다.
if not (0 <= len(jae[0:-1]) and len(jae[0:-1]) <= 999):
    raise Exception('재환이의 입력값의 길이 조건을 미충족')

if not (0 <= len(docter[0:-1]) and len(docter[0:-1]) <= 999):
    raise Exception('재환이의 입력값의 길이 조건을 미충족')

#  항상 h는 마지막에 하나만 주어진다.
if 'h' in jae[0:-1] or 'h' in docter[0:-1]:
    raise Exception('h는 마지막에만 들어갈 수 있습니다.')

if jae[-1] != 'h' or docter[-1] != 'h':
    raise Exception('입력값 마지막은 h이어야 합니다.')

if len(jae[:-1]) >= len(docter[:-1]):
    print('go')
else:
    print('no')


"""
1. 아래와 같이 할 경우 문자열의 첫 번째 문자부터 차례대로 유니코드 순서로 비교한다.
2. a보다 h가 크기 때문에, a<=b로 할 경우 a는 아직 a이지만 b는 h인 경우를 알 수 있다.

a=input()
b=input()
if a <= b:
  print('go')
else:
  print('no')
"""