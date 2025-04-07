def answer(N):
    if 1<=N and N<=100:
        for i in range(1,N+1):
            for j in range(i):
                print('*', end='')
            print()
    else:
        raise Exception('입력값의 범위 조건이 틀렸습니다.')

N = int(input())
answer(N)

"""
1. '*'문자열에 곱을 하여 문자열을 반복한 후 출력할 수도 있다.
for i in range(int(input())):
    print((i+1)*"*")
"""