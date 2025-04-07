def answer(a,b):
    diff = a-b

    if diff>0:
        print('>')
    elif diff<0:
        print('<')
    elif diff==0:
        print('==')

a,b = map(int,input().split(sep=' '))
answer(a,b)

"""
1. 삼항 연산자를 사용하는 방법도 있음
2. '><'라는 문자열을 선언한 후 A<B로 True 혹은 False를 계산한 후 index로 사용해버림
A,B = map(int,input().split())
print("==" if A == B else "><"[A<B])
"""