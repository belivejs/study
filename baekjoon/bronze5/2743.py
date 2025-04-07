import re

_input = input()
pattern = '^[a-zA-Z]+$'
result = re.fullmatch(pattern=pattern, string=_input)
if result:
    print(len(_input))
else:
    raise Exception('입력값 조건 미충족')