import re

_input = input()
pattern1 = '^[a-zA-Z]+$'
result = re.fullmatch(pattern=pattern1, string=_input)
if result:
    _len = len(_input)
    
    if _len > 100:
        raise Exception('최대 길이 초과')
    
    print(_input.swapcase())

else:
    raise Exception('입력값 조건 미충족')

"""
1. 문자열 내장 함수에는 swapcase라는 대소문자를 바꾸는 함수가 있다.
"""