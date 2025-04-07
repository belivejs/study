def minus(a,b):
    if a>0 and b<10:
        print(a-b)
    else:
        raise Exception('입력 값의 조건이 틀렸습니다.')

a, b = map(int,input().split(sep=' '))
minus(a,b)

"""
함수를 정의하기 전에 먼저 호출하는게 실수를 줄일 수 있을 것 같다.
"""