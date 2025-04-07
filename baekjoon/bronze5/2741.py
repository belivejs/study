N = int(input())
if 0 <= N and N <= 100_000:
    for i in range(1, N+1):
        print(i)
else:
    raise Exception('입력값 조건 미충족')

"""
1. 아래와 같이 range 객체를 언패킹하여 출력하는 방법도 있다.
print(*range(1,int(input())+1))
"""